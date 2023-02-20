import datetime
import requests
import telegram


from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bs4 import BeautifulSoup as b

from spy import *


async def aloxa(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'ALOXA {update.effective_user.first_name}')

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'/hello\n/time\n/sum\n/help\n/moon\n/newyear\n/joke')

async def time_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    
    await update.message.reply_text(f'{datetime.datetime.now().time()}')

async def sum_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split() # sum 123 56789
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f"{x} + {y} = {x + y}", reply_markup=mar)

async def phase_moon(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = datetime.datetime.now().date().isoformat()
    day = data.split("-")[2]
    ph_moon = ("Растущая луна", "Полнолуние", "Убывающая луна", "Последняя четверть", 
               "Старая луна", "Новолуние", "Молодая луна", "Первая четверть")
    await update.message.reply_text(f'Фаза луны - "{ph_moon[int(float(day)//3.6913)]}"')

async def new_year(update: Update, context: ContextTypes.DEFAULT_TYPE):
    day_year = 365 - int(datetime.datetime.now().strftime("%j"))
    await update.message.reply_text(f'До нового года осталось {day_year} дней')

async def joke(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = "https://www.anekdot.ru/random/anekdot/"
    read = requests.get(url)
    soup = b(read.text, 'html.parser')
    s = soup.find('div', class_="text")
    await update.message.reply_text(f"{s.text}")
    
