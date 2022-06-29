counties_dict = dict()
counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
for county, voters in counties_dict.items():
    print(county +" county has "+ str(voters) +" registered voters.")