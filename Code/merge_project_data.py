# Import dependencies
import pandas as pd

# Locate files
file1 = 'census_raw.csv'
file2 = 'Solar_installation_data.csv'

# Read files
census_df = pd.read_csv(file1)
solar_df = pd.read_csv(file2)

# Change Zipcode column name in census_df to match Zip Code column name in solar_df
census_df = census_df.rename(columns={'Zipcode':'Zip Code'})

# Merge solar_df and census_df
df = solar_df.merge(census_df, on = 'Zip Code', how='left')
df = df.drop(columns=['Unnamed: 0'])
df 

# Save df as csv
output_file = 'project_data.csv'
df.to_csv(output_file)