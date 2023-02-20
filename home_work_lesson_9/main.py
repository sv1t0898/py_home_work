from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *


app = ApplicationBuilder().token("5893227796:AAHj9t6W1epzcjmNCBn_4zpx0YuOIDAViLg").build()

app.add_handler(CommandHandler("hello", aloxa))
app.add_handler(CommandHandler("time", time_cmd))
app.add_handler(CommandHandler("help", help_cmd))
app.add_handler(CommandHandler("sum", sum_cmd))
app.add_handler(CommandHandler("moon", phase_moon))
app.add_handler(CommandHandler("newyear", new_year))
app.add_handler(CommandHandler("joke", joke))
print("server started")
app.run_polling()