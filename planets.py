planet_list = ["Mercury", "Mars"]

# planet_list.append("Jupiter")
# planet_list.append("Saturn")

planet_list.extend(["Jupiter", "Saturn"])
planet_list.insert(4, "Earth")
planet_list.insert(5, "Venus")
planet_list.append("Pluto")
print(planet_list)