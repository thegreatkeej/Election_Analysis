# retrieve data
import csv
dir (csv)
import os
dir (os)
file_to_save = "C:\Users\kijah\Documents\Data_Bootcamp\Election_Analysis\Resources\election_results.csv"
election_data = open(file_to_save, "w")
#
file_to_save = os.path.join("analysis", "election_analysis.txt")
outfile = open(file_to_save, "w")
outfile.write("Hello World")
outfile.close


# create a library with "Canidate" as key and "Ballot ID" as value
# List the keys
# Count the length of each key's value
# sum the lengths of each key's value or count the length of all the values in the data set
# find the max length of each keys value
# create percentages by dividing each canidates count by total # of votes
# print the key of the max length value