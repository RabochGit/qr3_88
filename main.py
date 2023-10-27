import telebot
import random
from telebot import types

bot = telebot.TeleBot("6385127193:AAHl32HUa0Ituz9yiMSSbSKGZTl1q86q-n0")

interesting_facts = [
    "Зубы бобров никогда не перестают расти.",
    "Морской конёк — самая медленная рыба на Земле!",
    "В 1938 году журнал «Таймс» признал Гитлера «Человеком года»."
]

proverbs = [
    "Был бы лес, соловьи прилетят.",
    "Кто не сажал дерева, тому не лежать в тени.",
    "Дважды в год лето не бывает"
]

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    fact_button = types.KeyboardButton("Факты")
    proverb_button = types.KeyboardButton("Поговорки")
    exit_button = types.KeyboardButton("Выход")
    markup.add(fact_button, proverb_button, exit_button)
    bot.send_message(message.chat.id, "Привет! Что будем делать?", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "Факты")
def send_fact(message):
    fact = random.choice(interesting_facts)
    bot.send_message(message.chat.id, fact)

@bot.message_handler(func=lambda message: message.text == "Поговорки")
def send_proverb(message):
    proverb = random.choice(proverbs)
    bot.send_message(message.chat.id, proverb)

@bot.message_handler(func=lambda message: message.text == "Выход")
def send_goodbye(message):
    bot.send_message(message.chat.id, "До свидания!")

bot.polling()
