import pandas as pd
import datetime as dt
import os
import glob
import json
import os, sys
import json
import geopandas as gpd
import numpy as np
import requests, io
import urllib.request
import fiona
import matplotlib.pyplot as plt
from collections import defaultdict
import mapConfiguration

replaceNorwayWithRegions=True
dirName= "totalPowerCapacities"
mType="Power Capacity [GW]"
csvDir="totalPowerCapacities"


def mapData(csvDir,mType,scenario="Gradudal Development"):
  os.chdir(csvDir)
  extension = 'csv'
  try:
      combined_df = pd.read_csv("Combined.csv")
  except:
      all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
      dfs=[]
      for f in all_filenames:
          df=pd.read_csv(f)
          if f[-5].isnumeric():
              df["Region"]=f[-7:-4]
          else:
              df["Region"]=f[-6:-4]

          dfs.append(df)
          combined_df = pd.concat(dfs)
          combined_df.to_csv( "Combined.csv", index=False, encoding='utf-8-sig')

  os.chdir('..')
  combined_df["2054"]=combined_df["2050"]

  colNames=list(combined_df.columns)
  id_vars=colNames[0:2]+["Region"]
  value_vars=colNames[2:-2]+[colNames[-1]]
  yearsMelted=combined_df.melt(id_vars=id_vars,
          var_name="Year",
          value_vars=value_vars,
          value_name="GW")

  yearsMelted["Year"]=pd.to_datetime(yearsMelted.Year, format='%Y')
  yearsMelted['Timestamp'] = (yearsMelted.Year.astype('int64')//10**6)#.astype(str)
  yearsMelted["Year"]=yearsMelted["Year"].dt.year

  coolNames=['Scenario','Region', 'Year', 'Timestamp']
  techPivoted=yearsMelted.pivot_table(index=coolNames, columns='Technology',values="GW")
  techPivoted=techPivoted.reset_index(drop=False)

  techPivoted["Share Renewable"]=1-techPivoted.Thermal/techPivoted.Sum
  techPivoted["Percent Renawable"]=techPivoted["Share Renewable"].apply(lambda x: "{0:.1f}%".format(x*100))

  #Add Geomitry
  coordinates = pd.read_csv("countryCoordinates.csv", sep=";")
  name2code=defaultdict(str)
  for index, row in coordinates.iterrows():
      country=row["country"]
      name2code[row["name"]]=country

  name2code["United Kingdom"]="UK"

  try:
      world = gpd.read_file("World.geojson")
  except:
      url = "https://opendata.arcgis.com/datasets/a21fdb46d23e4ef896f31475217cbb08_1.geojson"
      world = gpd.read_file(url)
      world["Region"]=world.apply(lambda row: name2code[row["CNTRY_NAME"]], axis=1)
      del world["OBJECTID"]
      world.to_file("World.geojson", driver="GeoJSON")
      world = gpd.read_file("World.geojson")

  if replaceNorwayWithRegions:
      priceRegions=gpd.read_file("NOpriceRegions.geojson")
      world = world[world.Region != "NO"]
      world=world.append(priceRegions, ignore_index = True)

  newWorld = world.merge(techPivoted, on='Region', how='left').dropna()
  newWorld=newWorld.rename(columns={"CNTRY_NAME":"Country"})
  newWorld["Value Type"]=mType
  crs = {'init': 'epsg:4326'}
  newWorld=gpd.GeoDataFrame(newWorld, crs=crs, geometry='geometry')
  newWorld.to_csv("mapData\\"+scenario+" "+mType+".csv")
  return newWorld
