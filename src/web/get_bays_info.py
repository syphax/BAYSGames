from bs4 import BeautifulSoup
import urllib.request as ur
import pandas as pd

def get_town_table(town):
	'''
		This function takes a 3-letter town code as an argument and returns a pandas dataframe with key stats
	'''

	url_bays_town = 'https://bays.org/bays/organizations/view/' + town

	# Get the standings table from the town pabe

	df_tbl = pd.read_html(url_bays_town, attrs={"id":"footable--2"}, flavor = 'bs4')[0]

	# Compute additional stats

	'''
	df_tbl['W'] = df_tbl['W'].astype(int)	
	df_tbl['L'] = df_tbl['L'].astype(int)	
	df_tbl['T'] = df_tbl['T'].astype(int)	
	df_tbl['PTS'] = df_tbl['PTS'].astype(int)	
	'''

	# Key stats
	# TODO: Account for forfeits?

	df_tbl['gp'] = (df_tbl['W'] + df_tbl['L'] + df_tbl['T']) 

	# Points per game
	
	df_tbl['ppg'] = 0
	df_tbl.loc[df_tbl['gp'] > 0, 'ppg'] = df_tbl['PTS'] / df_tbl['gp']

	# Winning pct, tie = 1/2

	df_tbl['wpct'] = 0
	df_tbl.loc[df_tbl['gp'] > 0, 'wpct'] = (df_tbl['W'] + df_tbl['T'] / 2) / df_tbl['gp']	

	# Gender, div, section info

	#df_tbl['gender'] = df_tbl['GADS'].str[:1]

	df_t1 = df_tbl['GADS'].str.split(' ', expand=True)
	df_t1 = df_t1.rename(columns={0:'gender', 1:'grade', 2:'div_sec'})

	df_t2 = df_t1['div_sec'].str.split('/', expand=True)
	df_t2 = df_t2.rename(columns={0:'division', 1:'section'})
	
	df_tbl = pd.concat([df_tbl, df_t1, df_t2], axis = 1)

	'''
	# Determine string slice offsets by gender (because 'Girls' is longer than 'Boys')
	df_tbl.loc[df_tbl['gender']=='B', 'to'] = 0
	df_tbl.loc[df_tbl['gender']=='G', 'to'] = 1

	# TODO: Find a cleaner way 
	# Grade
	df_tbl.loc[df_tbl['gender'=='B','grade'] = df_tbl['GADS'].str[5:7].astype(int)
	#df_tbl['division'] = df_tbl['GADS'].str[to+8:to+9].astype(int)
	'''

	return df_tbl

