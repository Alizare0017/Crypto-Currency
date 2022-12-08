import mechanicalsoup
from bs4 import BeautifulSoup
from persiantools.jdatetime import JalaliDateTime, JalaliDate
import re

month_dict = {'فروردین':'01', 'اردیبهشت':'02', 'خرداد':'03', 'تیر':'04', 'مرداد':'05',
         'شهریور':'06', 'مهر':'07', 'آبان':'08', 'آذر':'09', 'دی':'10', 'بهمن':'11', 'اسفند':'12'}

dictionary = {
            # currencies
            'دلار':'USD', 'یورو':'EUR', 'درهم امارات ':'AED', 'پوند انگلیس':'GBP', 'لیر ترکیه ':'TRY',
            'فرانک سوئیس ':'CHF', 'یوان چین ':'CNY', 'ین ژاپن (100 ین) ':'JPY', 'وون کره جنوبی':'KRW', 'دلار کانادا ':'CAD',
            'دلار استرالیا ':'AUD', 'دلار نیوزیلند ':'NZD', 'دلار سنگاپور ':'SGD', 'روپیه هند ':'INR', 'روپیه پاکستان ':'PKR',
            'دینار عراق ':'IQD', 'پوند سوریه':'SYP', 'افغانی ':'AFN', 'کرون دانمارک ':'DKK',
            'کرون سوئد ':'SEK', 'کرون نروژ ':'NOK', 'ریال عربستان ':'SAR', 'ریال قطر ':'QAR', 'ریال عمان ':'OMR',
            'دینار کویت ':'KWD','دینار بحرین ':'BHD', 'رینگیت مالزی ':'MYR', 'بات تایلند ':'THB', 'دلار هنگ کنگ ':'HKD',
            'روبل روسیه ':'RUB', 'منات آذربایجان ':'AZN', 'درام ارمنستان ':'AMD', 'لاری گرجستان ':'GEL', 'سوم قرقیزستان':'KGS',
            'سامانی تاجیکستان':'TJS','منات ترکمنستان':'TMT',
            # gold
            'طلای 18 عیار / 750':'gold18/750', 'طلای 18 عیار / 740':'gold18/740', 'طلای ۲۴ عیار':'gold24',
            'طلای دست دوم':'secgold', 'آبشده نقدی':'meltedcash', 'آبشده بنکداری ':'meltedbanking',
            'آبشده کمتر از کیلو ':'meltedkilo', 'آبشده معاملاتی':'meltedtransactional', 'مثقال طلا ':'goldmesghal',
            'مثقال / بدون حباب':'bubble', 'حباب آبشده':'melted bubble', 'مثقال / بر مبنای سکه':'coinbased',
            'صندوق طلای مفید':'mofidgold', 'صندوق طلای لوتوس':'lotosgold', 'صندوق طلای زر':'rosegold',
            'گرم نقره ۹۹۹':'silver', 'صندوق طلای گوهر':'gohargold'
            }

gold_code = {'طلای 18 عیار / 750':'gold18/750', 'طلای 18 عیار / 740':'gold18/740', 'طلای ۲۴ عیار':'gold24',
             'طلای دست دوم':'secgold', 'آبشده نقدی':'meltedcash', 'آبشده بنکداری ':'meltedbanking',
              'آبشده کمتر از کیلو ':'meltedkilo', 'آبشده معاملاتی':'meltedtransactional', 'مثقال طلا ':'goldmesghal',
               'مثقال / بدون حباب':'bubble', 'حباب آبشده':'melted bubble', 'مثقال / بر مبنای سکه':'coinbased',
               'صندوق طلای مفید':'mofidgold', 'صندوق طلای لوتوس':'lotosgold', 'صندوق طلای زر':'rosegold',
                'گرم نقره ۹۹۹':'silver'}

def currencyLeech(RateType):
    result_list = list()
    regex = r"(\d{2}):(\d{2}):(\d{2})"

    
    browser = mechanicalsoup.Browser()
    if RateType == 'gold' :
        url = "https://www.tgju.org/" + RateType + '-chart'
    else :
        url = "https://www.tgju.org/" + RateType
    page = browser.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    result = soup.find_all(attrs={'class':'pointer'})    
    currency_info = ['name','price', 'rate','low', 'high', 'updated_date']
    
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
        result_dict = dict(zip(currency_info, res))
        
        if re.fullmatch(regex,result_dict['updated_date']) :
            result_dict['updated_date'] = str(JalaliDate.today())+' '+p2e(result_dict['updated_date'])
        else :
            date = result_dict['updated_date'].split()
            result_dict['updated_date'] = str(JalaliDate.today().strftime('%Y'))+'-'+ month_dict[date[1]]+'-'+ p2e(date[0])
        result_dict['code'] = dictionary[result_dict['name']]
        result_dict['price'] = result_dict.get('price').replace(',','')
        result_dict['high'] = result_dict.get('high').replace(',','')
        result_dict['low'] = result_dict.get('low').replace(',','')
        result_dict['requested_date'] = JalaliDateTime.now().isoformat()
        result_list.append(result_dict)
        print(result_list)
    return result_list
