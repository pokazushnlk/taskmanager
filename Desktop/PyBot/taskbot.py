import telebot

bot = telebot.TeleBot("5567068620:AAFrHc6H13tMt_ja1z3SK9a7VoFlmD2R5Cs")

@bot.message_handler(commands=["start"])
def start(message):
	bot.send_message(message.chat.id, "<b>Привет, это бот для записи задач и дедлайнов по ним!</b>", parse_mode="html")

bot.polling(none_stop=True)