# Election_Analysis
Python Module 3 see "Pypoll_Challenge.py"
## Overview of Election Audit
-	In this module, I am doing an election audit from data contained in a csv
	file and automating this audit using Python. This audit contains the total
	number of votes, total votes and percentage of votes for each canidate, 
	total votes and percentage of votes for each county, election winner and
	county with the most votes. Once the audit is complete, my job is to 
	generate a vote count report that could be used to certify other voting 
	areas.
	
## Election-Audit Results
-	There were 369711 votes cast
### County Vote Breakdown:
-	Jefferson: 10.5% (38,855)
-	Denver: 82.8% (306,055)
-	Arapahoe: 6.7% (24,801)
-	Denver had the largest vote count
### The canidates and their vote counts were:
-	Charles Casper Stockham: got 23.0% of the votes (85,213)
-	Diana DeGette: got 73.8% of the votes (272,892)
-	Raymon Anthony Doane: got 3.1% of the votes (11,606)
-	The winner was Diana DeGette:  who got 73.8% of the votes for a total of 
	272,892 votes

## Election_Audit Summary
-	In summary, this coding script could be used for any voting county or 
	municipality. All that is needed is a csv file formated in the same way
	as the Colorado precinct file: "election_results.csv." If the new csv file
	is not formatted like the one used in this project this script can be
	altered by:
1) Creating a for loop that serches columns in the new csv file that contain: 
   county, canidate, and vote count.
2) Or, if the new script looks at state vote totals or city vote totals, this
   script can be adjusted to iterate through the data looking for those keys.
