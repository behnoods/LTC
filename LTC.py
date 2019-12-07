from telethon import TelegramClient, sync, events
from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest
from telethon.errors import SessionPasswordNeededError
from bs4 import BeautifulSoup
from time import sleep
import requests, json, re, sys, os
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)
hijau = Style.RESET_ALL+Style.BRIGHT+Fore.GREEN
hijau2 = Style.NORMAL+Fore.GREEN
putih = Style.RESET_ALL
abu = Style.DIM+Fore.WHITE
ungu = Style.RESET_ALL+Style.BRIGHT+Fore.MAGENTA
ungu2 = Style.NORMAL+Fore.MAGENTA
yellow = Style.RESET_ALL+Style.BRIGHT+Fore.YELLOW
yellow2 = Style.NORMAL+Fore.YELLOW
red = Style.RESET_ALL+Style.BRIGHT+Fore.RED
red2 = Style.NORMAL+Fore.RED

xnhac= '\033[1;96m'
den='\033[1;90m'
do='\033[1;91m'
luc='\033[1;92m'
vang='\033[1;93m'
xduong='\033[1;94m'
hong='\033[1;95m'
trang='\033[1;97m'
#logo
os.system('clear')
print('\n')
sleep(0.1)
print('\n\n',hong +'════════════════════════════════════════════════')
sleep(0.1)
print(vang +'  Creator:',luc +'[DAG Tricks] ',do +'[●] ',vang +'Youtube:',luc +'[DAG Tricks]')
sleep(0.1)
print(do +'    ____  ___   ______   ______     _      __');
sleep(0.1)
print(do +'   / __ \/   | / ____/  /_  __/____(_)____/ /_______');
sleep(0.1)
print(trang +'  / / / / /| |/ / __     / / / ___/ / ___/ //_/ ___/');
sleep(0.1)
print(xnhac +' / /_/ / ___ / /_/ /    / / / /  / / /__/ ,< (__  ) ');
sleep(0.1)
print(xnhac +'/_____/_/  |_\____/    /_/ /_/  /_/\___/_/|_/____/  ');
sleep(0.1)
print('\n',hong +'════════════════════════════════════════════════');
sleep(0.1)
print(luc +'Phiên Bản V1')
sleep(0.1)
print(hong +'TÍNH NĂNG:')
sleep(0.1)
print('\n')
print(do +'Hỗ Trợ Tiếng Việt')
sleep(0.1)
print(vang +'Tự Động Click Skip Doge.click')
sleep(0.1)
print(vang +'Không Cần Cài Pip')
sleep(0.1)
print(vang +'Tự Động Bỏ Qua Captcha')
sleep(0.1)
print(vang +'Dễ Dàng Sử Dụng')
sleep(0.1)
print('\n\n')
#Script
print(xnhac +'Nhập Số Điện Thoại Của Bạn Theo Mẫu +84XXXXXXXX')
print(hong +'Ví Dụ\x20\x2b\x38\x34\x33\x39\x33\x34\x31\x37\x36\x39\x35')
sdt=input(xnhac +'Nhập Số Điện Thoại ●>>\033[1;95m')

api_id = '1189987'
api_hash = 'e38dfd394158c00c1a2e41de88e9e57a'
phone_number = sdt

client = TelegramClient('session/'+phone_number,api_id,api_hash)
client.connect()
if not client.is_user_authorized():
    try:
        client.send_code_request(phone_number)
        me = client.sign_in(phone_number,input('Nhập Code Trong Telegram ●>> '.format(hijau,abu,putih)))
    except SessionPasswordNeededError:
        password = input('Code Sai. Làm Lại'.format(hijau,abu,putih))
        me = client.start(phone_number,password)

channel_username = '@Litecoin_click_bot'


c = requests.session()

ua = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
}

channel_entity = client.get_entity(channel_username)
try:
    for ulang in range(999999999):
        sys.stdout.write('\r                                                        \r')
        sys.stdout.write('\r Đang Lấy URL'.format(yellow2))
        client.send_message(entity=channel_entity,message='Visit sites')
        sleep(1)
        message_history = client(GetHistoryRequest(peer=channel_entity,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
        channel_id = message_history.messages[0].id
        if message_history.messages[0].message.find('Hết Site Xiu Quay Lại Làm Tiếp Nhé.') != -1:
            sys.stdout.write('\r                                                     \r')
            sys.stdout.write('\r Đã Thực Hiện Trước Đó\n'.format(red2))
            break
        url = message_history.messages[0].reply_markup.rows[0].buttons[0].url
        sys.stdout.write('\r                                                     \r')
        sys.stdout.write('Đến Site'.format(luc,putih)+url)

        r = c.get(url,headers=ua)
        soup = BeautifulSoup(r.text,"html.parser")

        if soup.find('div',class_='g-recaptcha') is None and soup.find('div',id='headbar') is None:
            sleep(1)
            message_history = client(GetHistoryRequest(peer=channel_entity,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
            message = message_history.messages[0].message
            sys.stdout.write('\r                                                     \r')
            if message_history.messages[0].message.find('Trở Lại') != -1 or message_history.messages[0].message.find('Quay Lại') != -1:
                timer = re.findall(r'([\d.]*\d+)',message)
                sleep(int(timer[0]))
                sleep(1)
                message_history = client(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0,add_offset=0, hash=0))
                sys.stdout.write('\r                                                     \r')
                sys.stdout.write('\r{}'.format(hijau)+message_history.messages[0].message+'\n')

        elif soup.find('div',id='headbar') is not None:
            for data in soup.find_all('div',class_='container-fluid'):
                code = data.get('data-code')
                timer = data.get('data-timer')
                token = data.get('data-token')
                sleep(int(timer))
                r = c.post('https://dogeclick.com/reward',data={'code': code, 'token': token},headers=ua)
                jsn = json.loads(r.text)
                sys.stdout.write('\r                                                     \r')
                print(hijau+"\r Bạn Đã Nhận Được"+jsn['reward']+" LTC Từ Site\n")
        else:
            sys.stdout.write('\r                                                     \r')
            sys.stdout.write(red+'\r Xóa Captcha')
            sleep(2)
            client(GetBotCallbackAnswerRequest(channel_username,channel_id,data=message_history.messages[0].reply_markup.rows[1].buttons[1].data))
            sys.stdout.write('\r                                                     \r')
            print (red+'\r Bỏ Qua Captcha\n')

except:
    print(red+"Lỗi Không Mong Đợi")
    sys.exit()
