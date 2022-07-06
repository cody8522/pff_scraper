import requests
import pandas as pd

url_temp = 'https://premium.pff.com/api/v1/games?league=nfl&season=2021&week={}'
url_list = []
games = []
games_1 = []
weeks = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18']
payload={}
headers = {}

for week in weeks:
    url = url_temp.format(week)
    url_list.append(url)
    
for url in url_list:
    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.json()
    for x in data['games']:
        games_1.append(x)
    
df = pd.json_normalize(games_1)

df1 = df[['id', 'season', 'week', 'away_franchise_id', 'home_franchise_id', 'away_team.abbreviation', 'home_team.abbreviation', 'score.away_team', 'score.home_team']]
df1

## make list of game IDs from df1
ids = df1.id.values.tolist()
id_list = [str(ids) for ids in ids]

url_temp_2 = "https://premium.pff.com/api/v1/facet/offense/summary?game_id={}"
url_list_2 = []
offense_summary = []


## make list of urls with game IDs plugged in
for id in id_list:
    url_2 = url_temp_2.format(id)
    url_list_2.append(url_2)
    
 
 ## iterate through url list to pull data table from each game ID
 headers = {
  'Cookie': '_gcl_au=1.1.1795153852.1655385867; prism_651055355=3028700c-5a74-4a05-879c-9ffd677052b2; _fbp=fb.1.1655385867210.116495345; _gid=GA1.2.1568067501.1657029085; _clck=1t9fb05|1|f2x|0; _hp2_ses_props.2100373990={"r":"https://premium.pff.com/","ts":1657120588207,"d":"premium.pff.com","h":"/nfl/games/2021"}; _clsk=16z3k4z|1657120599185|5|1|l.clarity.ms/collect; _dc_gtm_UA-21858063-7=1; _hp2_id.714504125={"userId":"569437218020475","pageviewId":"6454371586942102","sessionId":"7613858168913866","identity":null,"trackerVersion":"4.0"}; _hp2_ses_props.714504125={"r":"https://premium.pff.com/","ts":1657120871055,"d":"auth.pff.com","h":"/"}; _gali=sign-in; _premium_key=SFMyNTY.g3QAAAABbQAAABZndWFyZGlhbl9kZWZhdWx0X3Rva2VubQAAAlxleUpoYkdjaU9pSklVelV4TWlJc0luUjVjQ0k2SWtwWFZDSjkuZXlKaGRXUWlPaUpRY21WdGFYVnRJaXdpWlhod0lqb3hOalUzTVRJME5EY3pMQ0pwWVhRaU9qRTJOVGN4TWpBNE56TXNJbWx6Y3lJNklsQnlaVzFwZFcwaUxDSnFkR2tpT2lKbU16VXdNMlJpT1MxbE5HWXpMVFE0WVRNdFlXSXdZeTAwTnpjMlltVmxPVFk0TlRraUxDSnVZbVlpT2pFMk5UY3hNakE0TnpJc0luQmxiU0k2ZXlKaFlXWWlPakVzSW01bWJDSTZNU3dpZUdac0lqb3hmU3dpYzNWaUlqb2llMXdpWlcxaGFXeGNJanBjSW1OaFoyOW5aMmx1TWtCbmJXRnBiQzVqYjIxY0lpeGNJbVpsWVhSMWNtVnpYQ0k2VzEwc1hDSm1hWEp6ZEY5dVlXMWxYQ0k2WENKRGIyUjVYQ0lzWENKc1lYTjBYMjVoYldWY0lqcGNJa2R2WjJkcGJsd2lMRndpZFdsa1hDSTZYQ0kwTkRrMFpHRmxOQzB3T0RNNUxUUXlZakl0WVRnd05pMDRZbU5pTnpaaU9EVXpPVEpjSWl4Y0luWmxjblJwWTJGc1hDSTZYQ0pEYjI1emRXMWxjbHdpZlNJc0luUjVjQ0k2SW1GalkyVnpjeUo5Llo5X0MtVVBseXZ1Uk80N3JtVEVrOW9tMERqWExvd3lDUGdkWFNZc3h3bjlsTEhsRWMweDRRajM5OE9vWE0tbUNGOUdkTm4tLUNZeEdOclVPLVZzcVVn.M1iE4aFgP7YmNVHD1mtxEqAja_uFsd4xcaI6WjiPgI0; c_groot_access_token=ppy_JTBL6xEqQkwphdfJDoo_7A4r0g5gFOP9nZyxbP7kjY2MXKC3fwnd-mwpsWTv; c_groot_access_ts=2022-07-06T15:21:13Z; c_groot_refresh_token=jcGIypR7rkhxiX7jBBeRpwgdPXSjzdVF6LL6tUTlANpNdGg9BTd-3ZmRS-eLRnEZ; _ga_8Y6RN784SW=GS1.1.1657120543.6.1.1657120874.55; _ga=GA1.2.638636532.1655385867; _dc_gtm_UA-21858063-1=1; _hp2_id.2100373990={"userId":"454859690199216","pageviewId":"7386493549113000","sessionId":"8835975735556051","identity":"4494dae4-0839-42b2-a806-8bcb76b85392","trackerVersion":"4.0","identityField":null,"isIdentified":1,"oldIdentity":null'
}

for url in url_list_2:
    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.json()
    for x in data['offense_summary']:
        offense_summary.append(x)

df_2 = pd.json_normalize(offense_summary)   
