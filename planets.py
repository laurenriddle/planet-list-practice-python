planet_list = ["Mercury", "Mars"]

# planet_list.append("Jupiter")
# planet_list.append("Saturn")

planet_list.extend(["Jupiter", "Saturn"])
planet_list.insert(2, "Earth")
planet_list.insert(3, "Venus")
planet_list.append("Pluto")
print(planet_list)
rocky_planets = planet_list[0:4]
print(rocky_planets)
del planet_list[6]
print(planet_list)