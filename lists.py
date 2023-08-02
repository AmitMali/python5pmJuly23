cities=['nashik','mumbai','pune','vadodara','delhi','kolkata','nashik']
newCities=list(('hydrabaad','chennai','punjab'))

# print(newCities)
# print(cities[0:4])
# print( "dubai" in cities )

cities.append("Kolhapur")
cities.insert(3,'sangali')
cities.extend(['city1','city2'])

cities[2]="Pune"
cities.remove("Pune")
# print(popedItem)
cities.clear()



print(cities)