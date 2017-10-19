from web.get_bays_info import get_town_table 

def main():
	'''
		Compute key stats for neighboring teams
	'''

	list_towns = ['CON', 'ACT', 'ARL', 'BSC', 'BRO', 'LEX', 'NEB', 'WIN']

	for t in list_towns:
		df_town = get_town_table(t)
		ppg = df_town.loc[df_town['gp'] > 0, 'ppg'].mean()
		cnt_ppg_g1 = df_town.loc[(df_town['gp'] > 0) & (df_town['ppg'] >= 1), 'ppg'].count()
		cnt_teams = df_town.loc[df_town['gp'] > 0, 'ppg'].count()
		pct_ppg_g1 = cnt_ppg_g1 / cnt_teams
		print(t, cnt_teams, cnt_ppg_g1, pct_ppg_g1, ppg)

	#print(a)

if __name__ == '__main__':
    main()
