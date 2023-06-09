import telebot
import requests 
#bot=Session
#tele=@OS74_Tools
bot = telebot.TeleBot("6195074120:AAGEBqGE_RICXkB1fb47lZyH_F5KGn8uh6k")


import requests
import telebot

@bot.message_handler(commands=["start"])
def message(message):
	
	bot.send_message(message.chat.id,f"*Welcome, \n\nSend Sessionid  To Check \n\n\n\nBY: @q5_u8 | *",parse_mode='markdown')
@bot.message_handler(func=lambda message:True)
def sta(message):
	msg = message.text
	url = requests.get(f"https://nouredinekn-api-v1.herokuapp.com/api/?sessionid={msg}").text
	print(url)
	if 'false' in url:
	   bot.reply_to(message,f"[❌] Expired or Wrong Session \n\n Press /start To Start Again")
	if 'true' in url:
		bot.reply_to(message,f"[✅] Worked Sessionid  \n\n Press /start If You Want To Start Again")
bot.polling(True)
