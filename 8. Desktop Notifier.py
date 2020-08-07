import datetime
import requests
from win10toast import ToastNotifier

try:
    url = requests.get("https://api.covid19api.com/summary")   
except:
    print("Check your internet connection!")
    url = None
    
    
if url is not None:
    data = url.json()
    for country in data['Countries']:
        if country['CountryCode']=='RU':
            text = 'COVID 19 in Russia/ {}'.format(datetime.date.today())
            message = 'New Cases for today {}, New Deaths {}, Cases in total {}, Cases recovered in total {}'.format(
                country['NewConfirmed'],country['NewDeaths'], country['TotalConfirmed'], country['TotalRecovered'])
            print(country)
            toaster = ToastNotifier()
            toaster.show_toast(title=text,msg=message,icon_path='./icon.ico',duration=10)
