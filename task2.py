import requests
from datetime import date

now = date.today()
dt_string = now.strftime('%d-%m-%y')

def currency_rates(*name_cent):
    r = requests.get('https://www.cbr-xml-daily.ru/latest.js')
    cent = r.json()
    
    for name in name_cent:
        result = f"1 RUB = {cent['rates'][name]} {name}, сегодня {dt_string}"
        print(result)
        
    return result
    
    
if __name__ == "__main__":
    currency_rates('USD', 'AMD', 'CAD')