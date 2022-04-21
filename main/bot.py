import telebot 
import random
bot = telebot.TeleBot('5368004449:AAF548vepfU__G5KpSV1Tz1LkpMkg6LuKVc')

@bot.message_handler(func= lambda message: True)
def start(message):
	bank = [' и что теперь? -мне без разницы 🤐',
			' мм классно! 😪',
			'рассказывай, рассказывай.... Очень интересно 😴']
	bot.reply_to(message, '"' + str(message.text) + '"' + bank[random.randint(0,2)])
bot.polling()