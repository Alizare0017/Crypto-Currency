import mechanicalsoup
from bs4 import BeautifulSoup
import jdatetime
import re
from persiantools.jdatetime import JalaliDate
from django.utils import timezone

def currencyLeech():
    currency_list = list()
    regex = r"(\d{2}):(\d{2}):(\d{2})"
    currenciesISO = {'دلار':'USD', 'یورو':'EUR', 'درهم امارات ':'AED', 'پوند انگلیس':'GBP', 'لیر ترکیه ':'TRY',
                'فرانک سوئیس ':'CHF', 'یوان چین ':'CNY', 'ین ژاپن (100 ین) ':'JPY', 'وون کره جنوبی':'KRW', 'دلار کانادا ':'CAD',
                'دلار استرالیا ':'AUD', 'دلار نیوزیلند ':'NZD', 'دلار سنگاپور ':'SGD', 'روپیه هند ':'INR', 'روپیه پاکستان ':'PKR',
                'دینار عراق ':'IQD', 'پوند سوریه':'SYP', 'افغانی ':'AFN', 'کرون دانمارک ':'DKK',
                'کرون سوئد ':'SEK', 'کرون نروژ ':'NOK', 'ریال عربستان ':'SAR', 'ریال قطر ':'QAR', 'ریال عمان ':'OMR',
                'دینار کویت ':'KWD','دینار بحرین ':'BHD', 'رینگیت مالزی ':'MYR', 'بات تایلند ':'THB', 'دلار هنگ کنگ ':'HKD',
                'روبل روسیه ':'RUB', 'منات آذربایجان ':'AZN', 'درام ارمنستان ':'AMD', 'لاری گرجستان ':'GEL', 'سوم قرقیزستان':'KGS',
                'سامانی تاجیکستان':'TJS','منات ترکمنستان':'TMT'
                }
    
    browser = mechanicalsoup.Browser()
    url = "https://www.tgju.org/currency"
    page = browser.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    result = soup.find_all(attrs={'class':'pointer'})    
    currency_info = ['name','price', 'rate','high', 'low', 'updated_date']
    
    def p2e(persiannumber):    
        number={
            '0':'۰',
            '1':'۱',
            '2':'۲',
            '3':'۳',
            '4':'۴',
            '5':'۵',
            '6':'۶',
            '7':'۷',
            '8':'۸',
            '9':'۹',
            ':':':',
        }
        for i,j in number.items():
            persiannumber=persiannumber.replace(j,i)
        
        return persiannumber
    
    for tag in result :
        res = tag.text.strip().split('\n')[0:]
        currency_dict = dict(zip(currency_info, res))
        
        if re.fullmatch(regex,currency_dict['updated_date']) :
            currency_dict['updated_date'] = p2e(currency_dict['updated_date'])
        else :
            currency_dict['updated_date'] = str(jdatetime.date.today().isoformat())+' '+'00:00:00'
        currency_dict['code'] = currenciesISO[currency_dict['name']]
        currency_dict['price'] = currency_dict.get('price').replace(',','')
        currency_dict['high'] = currency_dict.get('high').replace(',','')
        currency_dict['low'] = currency_dict.get('low').replace(',','')
        currency_list.append(currency_dict)
        
    return currency_list
