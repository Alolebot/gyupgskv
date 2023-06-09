import requests
import telebot
from uuid import uuid4
  
token = input('6031420561:AAHT_H0TpZpvTPt3Ucb-6bg76QeLGt9zru8') 

bot = telebot.TeleBot(token)
@bot.message_handler(commands = ['greet','start'])
def start(message):
 zix = f'''
 • مرحبأ اهلين نورت بوت المبرمج زيد 
ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
• بوت توصـيل ريست ايميـل انستكرام 
ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
@OPP0Y
'''
 bot.send_message(message.chat.id, f"{zix}")
 ffe = f'''
 ارسـل الايميل او اليوزر لتوصـيل الريست
ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
'''
 bot.send_message(message.chat.id, f"{ffe}")

 @bot.message_handler(func=lambda followinG:True )
 def re(message):
  zood =(message.text)
  user=f'{zood}'
  P_2_9=str(uuid4())
  he = {
'accept': '*/*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'ar',
'cookie': 'csrftoken=qLKG0H8Y4BavlpaeJLS8mXsbjyaYWUdI;mid=Yw2UXgAEAAE4Z0qqjhY5LAruCxGL;ig_did=581A8852-CB4E-4DCE-8112-8DBD48CFA6DF;ig_nrcb=1',
'origin': 'https://www.instagram.com',
'referer': 'https://www.instagram.com/',
'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-site',
'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
'x-asbd-id': '198387',
'x-csrftoken': 'qLKG0H8Y4BavlpaeJLS8mXsbjyaYWUdI',
'x-ig-app-id': '936619743392459',
'x-ig-www-claim': '0',
}
  try:
   urlg = f'https://i.instagram.com/api/v1/users/web_profile_info/?username={user}'
   re =requests.get(urlg,headers=he).json()
   id = re['data']['user']['id'] 
   url = 'https://i.instagram.com/api/v1/accounts/send_password_reset/'
   he = {
 'User-Agent': 'Instagram 6.12.1 Android (30/11; 480dpi; 1080x2004; HONOR; ANY-LX2; HNANY-Q1; qcom; ar_EG_#u-nu-arab)',
 'Cookie': 'mid=YwsgcAABAAGsRwCKCbYCaUO5xej3; csrftoken=u6c8M4zaneeZBfR5scLVY43lYSIoUhxL',
 'Cookie2': '$Version=1',
 'Accept-Language': 'ar-EG, en-US',
 'X-IG-Connection-Type': 'MOBILE(LTE)',
 'X-IG-Capabilities': 'AQ==',
 'Accept-Encoding': 'gzip',
 }
   data = {
 "user_id":id,"device_id":P_2_9,
 }
   zaid = requests.post(url,headers=he, data=data).json()
   rest = zaid["obfuscated_email"]
   rek = f'''
 ✅ Done Send Rest ⚠️
 _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
 
 Email : {rest}
 
 _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
 @P_2_9
 '''
   bot.send_message(message.chat.id, f"{rek}")
  except:
   err = f'''
❌ Error Send Rest ❗
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

Email : Bad 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
@P_2_9'''
   bot.send_message(message.chat.id, f"{err}")
bot.polling(none_stop=True)
