
cities=('nashik','mumbai','pune','vadodara','delhi','kolkata','nashik')
newCities=tuple(('dubai','singapore'))

# print(type(cities))
# print(type(newCities))

# for city in cities:
#     print(city)

cities=list(cities)
cities[0]="Dhule"
cities=tuple(cities)
print(cities)
print(type(cities))