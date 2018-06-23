# Import US Census Bureau module and api keys
from census import Census
from us import states
from apikeys import census_api
import pandas as pd

# Access Census API
c = Census(census_api, year=2016)

# Pull data from Census Bureau
census_data = c.acs5.get(("NAME", "B19013_001E", "B01003_001E",
                          "B01002_001E", "B19301_001E", "B17001_002E"),
                         {'for': 'zip code tabulation area:*'})

# Convert to DataFrame
census_pd = pd.DataFrame(census_data)

# Column Reordering
census_pd = census_pd.rename(columns={
    "B01003_001E": "Population",
    "B01002_001E": "Median Age",
    "B19013_001E": "Household Income",
    "B19301_001E": "Per Capita Income",
    "B17001_002E": "Poverty Count",
    "zip code tabulation area": "Zipcode"
})

census_pd