from web.get_bays_info import get_town_table 
import pandas as pd
import datetime

def main():
	'''
		Compute key stats for neighboring teams
	'''

	list_towns = ['CON', 'ACT', 'ARL', 'BED', 'BSC', 'BRO', 'DOV', 'LEX', 'LIN', 'NAT', 'NEE', 'NEB', 'NEG', 'SUD', 'WAY', 'WEL', 'WSC', 'WIN']
	#list_towns = ['CON', 'ACT']

	df_columns = ['Town', 'Teams', 'Teams > 1 PPG', 'Pct', 'Avg. PPG', 'GD per Game']
	df_summary = pd.DataFrame(columns=df_columns)

	print('Town, Teams, Teams > 1 PPG, Pct., PPG')
	for t in list_towns:
		df_town = get_town_table(t)

		#print(df_town.columns.values)

		ppg = df_town.loc[df_town['gp'] > 0, 'ppg'].mean()
		cnt_ppg_g1 = df_town.loc[(df_town['gp'] > 0) & (df_town['ppg'] >= 1), 'ppg'].count()
		cnt_teams = df_town.loc[df_town['gp'] > 0, 'ppg'].count()
		pct_ppg_g1 = cnt_ppg_g1 / cnt_teams
		gdpg = df_town['+/-'].sum() / df_town['gp'].sum()

		df_tmp = pd.DataFrame([[t, cnt_teams, cnt_ppg_g1, pct_ppg_g1, ppg, gdpg]], columns=df_columns)
		df_summary = df_summary.append(df_tmp)

		# print(t, cnt_teams, cnt_ppg_g1, pct_ppg_g1, ppg)
		print('{0} {1:02d} {2:02d} {3:.2f} {4:.2f}'.format(t, cnt_teams, cnt_ppg_g1, pct_ppg_g1, ppg))

	#print(a)

	ts = datetime.date.today().strftime("%Y-%m-%d")
	print(ts)

	print(df_summary)
	df_summary.to_csv('./results/town-summary-results-'+ts+'.csv')

if __name__ == '__main__':
    main()
