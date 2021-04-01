import keplergl
from capacityConfiguration import c
from productionConfiguration import c2
from makeMap import mapData

csvDir1="totalPowerCapacities"
csvDir2="totalPowerProductions"
mType1="Power Capacity [GW]"
mType2="Power Productions [TWh]"

myMap = keplergl.KeplerGl(height=500, config=c)
capacityData=mapData(csvDir1,mType1,scenario="Gradual Development")
myMap2 = keplergl.KeplerGl(height=500, config=c2)
prodictionData=mapData(csvDir2,mType2,scenario="Gradual Development")

myMap.add_data(data=capacityData, name='Power Capacities')
myMap2.add_data(data=prodictionData, name='Power Productios')
myMap.save_to_html(file_name='GENeSYS_Capacity_Results.html')
myMap2.save_to_html(file_name='GENeSYS_Productions_Results.html')