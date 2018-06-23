# TeamGreenTech
UCB DATA  - team project 1

1) Project Title: Solar Adoption Analysis for New York State Between 2000 and 2017 

2) Team Members: Dipesh, Josh, Aubrey, Vish

3) Project Description/ Outline: 
  To analyze the proliferation of solar energy projects in New York state across an 18 year period 
  factoring in project costs, socio-economic factors per zipcode, and the introduction of financial innovations in the market as    influences on area of adoption per zipcode and concentration of projects. 

  
4) Reserach Questions to Answer:
  (1) How solar adoption--and its associated costs--have evolved over time. 
    - How has the penetration of solar energy evolved over time for residential, non-residential, and utility scale solar energy projects? 
    - Where is the adoption of solar concentrated (display this as a heat map with adoption per 1000 as a heatmap)? 
    - How has the cost of rooftop solar equipment changed over time w/ and w/o incentives?
  (2) What the relationship is between several socio-economic (SEC) factors and solar penetration within various zipcodes.
    - How are income levels related to solar adoption? (Analysis at zip level. Use census data to analyze relationship between % home   ownership, income, and solar adoption)
  (3) Whether or not solar adoption changes are correlated with the introduction of finacial innovations in the market
    - Did solar adoption change with the introduction of financial innovations (lease/power purchase agreements versus own)?
  (4) A sentiment analysis re: how social media users feel about the top 10 solar panel contractors in NY. 
    - How do Twitter users feel about the top 10 solar contractors w/in New York?

5) Data Sets to be Used:
  - Rooftop solar installation data (data.ny.gov) - data on 83.7k projects, with lots of detail
  - US Census Bureau Data (for socieconomic indicators by zip code)
  - Twitter API data
  - IEA/ NYISO data (www.eia.gov) (Based on narrower set of questions, we may not need this)

6) Rough Breakdown of Tasks: 
Solar Data	
  1   Read in NY solar data	
  2		Narrow down to analysis data	
  3		Produce a dataset summaryizing key variables by year-month and customer type	
  4		Produce a dataset summarizing key variables by zip code	
  5		Identify the top 10 solar installer in NY	
  
Census Data	Read census documentation	
	7		Read in relevant variables for NY zip code	
	8		store zip level dataset	
  
Prepare zip-code level shape files	

Twitter Data collection	Read in 500 tweets each for each of the top 10 installers in NY	
	11		Filter data (if needed - e.g. avoid tweets by installer)	
	12		Perform sentiment analysis	
Address research questions	
  13    What is the penetration of solar (the S-curve) and is it still growing? Does it vary for residential rooftop, non-residential rooftop, and solar farms?	2
	14		How does it vary by location (kw per 10,000)? Is it concentrated in specific locations?	3, 9
	15		How have the costs of solar changed over time? with and without incentives?	2
	16		Did solar adoption change with the introduction of financial innovations (lease/ppa versus own)	2
	17		How are income levels related to solar penetration?	4, 8
	18		How are home ownership rates related to solar penetration (and income levels)?	4,8
	19		How do NY twitter users feel about the top solar installer in NY?	12

Quality checks on code	Swap code and review			
Merge code			

Prepare presentation	Intro	2
	26		Key research questions	2
	27		Data sources	2
	28		Results	2
	29		Additional research	2

Practice presentation		

7) What each team member wants to get from this project:
  - Dipesh: wants to get hands-on experience working with data (collection, processing/ analysis).
  - Josh: wants to work on the plotting/ visualizations. 
  - Aubrey: wants to improve coding skills as well as create a portfolio piece.
  - Vish: wants to do participate in data collectin, cleaning, analysis, and visualiztion using python.





