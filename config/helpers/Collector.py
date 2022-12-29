import mechanicalsoup
from bs4 import BeautifulSoup
from persiantools.jdatetime import JalaliDateTime, JalaliDate
import re
import calendar
import datetime

month_dict = {'فروردین':'01', 'اردیبهشت':'02', 'خرداد':'03', 'تیر':'04', 'مرداد':'05',
         'شهریور':'06', 'مهر':'07', 'آبان':'08', 'آذر':'09', 'دی':'10', 'بهمن':'11', 'اسفند':'12'}

dictionary = {
            # Currencies
            'دلار':'USD', 'یورو':'EUR', 'درهم امارات ':'AED', 'پوند انگلیس':'GBP', 'لیر ترکیه ':'TRY',
            'فرانک سوئیس ':'CHF', 'یوان چین ':'CNY', 'ین ژاپن (100 ین) ':'JPY', 'وون کره جنوبی':'KRW', 'دلار کانادا ':'CAD',
            'دلار استرالیا ':'AUD', 'دلار نیوزیلند ':'NZD', 'دلار سنگاپور ':'SGD', 'روپیه هند ':'INR', 'روپیه پاکستان ':'PKR',
            'دینار عراق ':'IQD', 'پوند سوریه':'SYP', 'افغانی ':'AFN', 'کرون دانمارک ':'DKK',
            'کرون سوئد ':'SEK', 'کرون نروژ ':'NOK', 'ریال عربستان ':'SAR', 'ریال قطر ':'QAR', 'ریال عمان ':'OMR',
            'دینار کویت ':'KWD','دینار بحرین ':'BHD', 'رینگیت مالزی ':'MYR', 'بات تایلند ':'THB', 'دلار هنگ کنگ ':'HKD',
            'روبل روسیه ':'RUB', 'منات آذربایجان ':'AZN', 'درام ارمنستان ':'AMD', 'لاری گرجستان ':'GEL', 'سوم قرقیزستان':'KGS',
            'سامانی تاجیکستان':'TJS','منات ترکمنستان':'TMT',
            # Gold
            'طلای 18 عیار / 750':'gold18/750', 'طلای 18 عیار / 740':'gold18/740', 'طلای ۲۴ عیار':'gold24',
            'طلای دست دوم':'secgold', 'آبشده نقدی':'meltedcash', 'آبشده بنکداری ':'meltedbanking',
            'آبشده کمتر از کیلو ':'meltedkilo', 'آبشده معاملاتی':'meltedtransactional', 'مثقال طلا ':'goldmesghal',
            'مثقال / بدون حباب':'bubble', 'حباب آبشده':'melted bubble', 'مثقال / بر مبنای سکه':'coinbased',
            'صندوق طلای مفید':'mofidgold', 'صندوق طلای لوتوس':'lotosgold', 'صندوق طلای زر':'rosegold',
            'گرم نقره ۹۹۹':'silver', 'صندوق طلای گوهر':'gohargold',
            # Crypto
            'Bitcoin':'BTC', 'Ethereum':'ETH', 'Tether':'USDT', 'BNB':'BNB', 'USD Coin':'USDC', 'Binance USD':'BUSD',
            'XRP':'XRP', 'Dogecoin':'DOGE', 'Cardano':'ADA', 'Polygon':'MATIC', 'Dai':'DAI', 'Polkadot':'DOT',
            'Litecoin':'LTC', 'TRON':'TRX', 'Shiba Inu':'SHIB', 'Solana':'SOL', 'Uniswap':'UNI', 'Avalanche':'AVAX',
            'UNUS SED LEO':'SED', 'Wrapped Bitcoin':'WBTC', 'Chainlink':'LINK', 'Cosmos':'ATOM', 'Monero':'XMR',
            'Ethereum Classic':'ETC', 'Toncoin':'TON', 'Stellar':'XLM', 'Bitcoin Cash':'BCH', 'Cronos':'CRO',
            'Algorand':'ALGO', 'ApeCoin':'APE', 'Filecoin':'FIL', 'Quant':'QNT', 'VeChain':'VET', 
            'NEAR Protocol':'NEAR', 'OKB':'OKB', 'Hedera':'HBAR', 'Internet Computer':'ICP', 'Trust Wallet Token':'TWT',
            'EOS':'EOS', 'MultiversX (Elrond)':'EGLD', 'Terra Classic':'LUNC', 'Flow':'FLOW', 'Huobi Token':'HT',
            'Pax Dollar':'USDP', 'Tezos':'XTZ', 'Chiliz':'CHZ', 'Bitcoin SV':'BSV', 'The Sandbox':'SAND',
            'Aave':'AAVE', 'Theta Network':'THETA','TrueUSD':'TUSD','USDD':'USDD', 'Axie Infinity':'AXS','KuCoin Token':'KCS',
            }

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


def timestamp(y,m,d):
        date = JalaliDate(int(y),int(m),int(d)).to_gregorian()
        time_tuple = date.timetuple()
        time_stamp = calendar.timegm(time_tuple)
        return str(time_stamp)


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
    
    for tag in result :

        res = tag.text.strip().split('\n')[0:]
        result_dict = dict(zip(currency_info, res))
        
        if re.fullmatch(regex,result_dict['updated_date']) :
            date_jalali = str(JalaliDate.today())+' '+p2e(result_dict['updated_date'])
            date_miladi = str(datetime.datetime.today().strftime('%Y-%m-%d'))+' '+p2e(result_dict['updated_date'])
            s_datetime = datetime.datetime.strptime(date_miladi, '%Y-%m-%d %H:%M:%S')
            time_tuple = s_datetime.timetuple()
            result_dict['time_stamp'] = calendar.timegm(time_tuple)
            result_dict['updated_date'] = date_jalali
            print(result_dict['updated_date'])

        else :
            date1 = result_dict['updated_date'].split()
            date = str(JalaliDate.today().strftime('%Y'))+' '+ month_dict[date1[1]]+' '+ p2e(date1[0])
            date = date.split()
            result_dict['updated_date'] = str(JalaliDate.today().strftime('%Y'))+'-'+ month_dict[date1[1]]+'-'+ p2e(date1[0]) + ' ' + '00:00:00'
            result_dict['time_stamp'] = timestamp(date[0],date[1],date[2])
         
        result_dict['rate'] = re.findall(r"\((.*?)\)", result_dict['rate'])[0]
        result_dict['code'] = dictionary[result_dict['name']]
        result_dict['price'] = result_dict.get('price').replace(',','')
        result_dict['high'] = result_dict.get('high').replace(',','')
        result_dict['low'] = result_dict.get('low').replace(',','')
        result_dict['requested_date'] = JalaliDateTime.now().isoformat()
        result_list.append(result_dict)
    return result_list



def cryptoLeech(): 
    crypto_list = list()
    browser = mechanicalsoup.Browser()
    url = "https://arzdigital.com/coins/"
    page = browser.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    result = soup.find_all("tr")[1:]
    
    for tag in result :
        input_tag = tag.findAll('td')
        crypto_dict = {}
        for attr in input_tag :
            print(attr.text)
            try :
                crypto_dict[attr['data-sort-name']] = attr['data-sort-value']
            except :
                pass
        crypto_dict['code'] = dictionary[crypto_dict['name']]
        crypto_dict['rial_price'] = crypto_dict.pop('rial-price')
        crypto_dict['daily_swing'] = crypto_dict.pop('daily-swing')
        crypto_dict['weekly_swing'] = crypto_dict.pop('weekly-swing')
        crypto_list.append(crypto_dict)
    return crypto_list