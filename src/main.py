from web.get_bays_info import get_town_table 

def main():

	list_towns = ['CON', 'ACT', 'ARL', 'BSC', 'BRO', 'LEX', 'NEB', 'WIN']

	for t in list_towns:
		df_town = get_town_table(t)
		ppg = df_town.loc[df_town['gp'] > 0, 'ppg'].mean()
		cnt_teams = df_town.loc[df_town['gp'] > 0, 'ppg'].count()
		print(t, cnt_teams, ppg)

	#print(a)

if __name__ == '__main__':
    main()
