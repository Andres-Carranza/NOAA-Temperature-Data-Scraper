from requests import get
from bs4 import BeautifulSoup

base_url = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/'
token = 'dSDOnpGAaiYXCfJsZSASQKQDPCanznIn'


def selectCity():
    city = input('enter city: ')
    
    url = base_url + 'locations?locationcategoryid=CITY&limit=1000'
    data = get(url, headers={'token': token})
    
    city_info = {}
    
    for item in data.json()['results']:
        if city.lower() in str(item['name']).lower():
            city_info = item
            
    url = base_url + 'locations?locationcategoryid=CITY&limit=1000&offset=1000'
    data = get(url, headers={'token': token})

    for item in data.json()['results']:
        if city.lower() in str(item['name']).lower():
            city_info = item
            
    if not city_info:
        print('city not found')
        return 0
    
    print('name: ' + city_info['name'])
    print('mindate: ' + city_info['mindate'])
    print('maxdate: ' + city_info['maxdate'])
    print('id: ' + city_info['id']+'\n')
    return(city_info)
    
def getAvgMonthTempsPerDecade(city_info):   
    
    month = '9'
    for year in ['1910','1920','1930','1940','1950','1960','1970','1980','1990','2000','2010']:
        url = base_url +'data?datasetid=GSOM&datatypeid=TAVG&locationid='+city_info['id']+'&units=metric&startdate='+year+'-09-01&enddate='+year+'-09-30&limit=1000'

    
        data = get(url, headers={'token': token})

        if not data.json():
            print('no temperature data for '+year+ '\n')
        else:
            print('year: '+year)
            print('station: '+data.json()['results'][0]['station'])
            print('avg temp: '+str(data.json()['results'][0]['value']) +'\n')
        

    
city_info = selectCity()

if id != 0:
    getAvgMonthTempsPerDecade(city_info)
    
    