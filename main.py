import telebot
from telebot import types

bot = telebot.TeleBot("7222498602:AAEKMjVB6nb_N69WmUQpIZziKt8XSrd01DY")

@bot.message_handler(commands=["start"])
def main(message):
	bot.send_message(message.chat.id, "Здравствуй, дружище! Пора скрасить твою жизнь смехом))", parse_mode="Markdown")

@bot.message_handler(commands=["shutka 1"])
def maine(message):
	bot.send_message(message.chat.id, "-Не питон, а пайтон, читайте википедию\n -Не пайтон, а питон, не читайте википедию", parse_mode="Markdown")

@bot.message_handler(commands=["shutka 2"])
def mainee(message):
	bot.send_message(message.chat.id, "Как бы вы объяснили своей бабушке, что вы Python-разработчик?\n -Я пишу на Питоне. Нет, не в цирке. Питон - это язык программирования. Программирование? Это когда пишешь заказы для компьютеров, а они их выполняют. Да, я - начальник. Начальник компьютера.", parse_mode="Markdown")

bot.infinity_polling()