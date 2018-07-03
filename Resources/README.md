**data exploration and cleanup**

DATA ACQUISITION

SOLAR ELECTRIC PROGRAMS API (solar installation data for New York)
- Use API to pull relevant data from website
- used .drop() to remove data that had NaN or NULL values
- used .loc()  to filter out solar projects that are currently in the pipeline and haven't been completed

US CENSUS BUREAU API/ WEBSITE
- Use API to pull relevant demographic data for only zip codes in NY
- Create new data from from csv with only the census fields we were interested in looking at
- merge resulting data fram with solar project data frame to create final project data frame from which all resulting analyses will be based from.

DATA ANALYSIS
- starting with our ANALYSIS DATA FRAME, each team member created their own branch on github where they would perform their assigned analyses. 


