import keplergl
from mapConfiguration import c
from makeMap import mapData

parDir="C:\\Users\\ahsor\\Dropbox\\Masteroppgave\\PlotData\\Rdomain\\Tables\\AllNations\\"
csvDir1=parDir+"totalPowerCapacities"
csvDir2=parDir+"totalPowerProductions"
mType1="Power Capacity [GW]"
mType2="Power Productions [TWh]"

myMap = keplergl.KeplerGl(height=500, config=c)
myMap2 = keplergl.KeplerGl(height=500, config=c)
capacityData=mapData(csvDir1,mType1,scenario="Gradual Development")
prodictionData=mapData(csvDir2,mType2,scenario="Gradual Development")

myMap.add_data(data=capacityData, name='Power Capacities')
myMap2.add_data(data=prodictionData, name='Power Productios')
myMap.save_to_html(file_name='GENeSYS_Capacity_Results.html')
myMap.save_to_html(file_name='GENeSYS_Productions_Results.html')