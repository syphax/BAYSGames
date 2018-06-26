from bs4 import BeautifulSoup
import urllib.request as ur
import pandas as pd
import re
import requests

def get_town_table(town):
    """
        This function takes a 3-letter town code as an argument and returns a pandas dataframe with key stats
    """

    url_bays_town = 'https://bays.org/bays/organizations/view/' + town
    # print(url_bays_town)

    # Get the standings table from the town page

    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers = {'User-Agent': user_agent, }

    df_tbl = pd.read_html(requests.get(url_bays_town, headers={'User-agent': 'Mozilla/5.0'}).text, attrs={"id":"footable--2"}, flavor = 'bs4')[0]

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


def get_section_names_one_division(year, season, gender, grade, division):
    '''
        Returns the names of sections in a division 
        names = get_section_names_one_division(year, season, gender, grade, division)
    '''

    url = 'https://bays.org/bays/standings_by_placement/' + season + '%20' + str(year) + '/' + gender + '/' + str(grade) +'/' + str(division) + '/Any'
    print(url)

    div_page = ur.urlopen(url).read()
    #print(div_page)

    # Get section counts and names

    # Target string: Standings for Fall 2017 Girls Grade 8 Division 4 Section A

    section_string = b"Standings for .* Section (.*)</a>"

    results = re.findall(section_string,div_page)

    #print(len(results))

    list_section_names = []
    for i in results:
        section_name = gender + ' ' + str(grade) + ' ' + str(division) + '/' + i.decode("utf-8")
        list_section_names.append(section_name)
        #print(section_name)

    return list_section_names


