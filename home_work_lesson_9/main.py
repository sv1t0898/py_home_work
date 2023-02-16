# from isOdd import isOdd


# print(isOdd(0)) 
# print(isOdd(4))
# print(isOdd(10)) 
# print(isOdd(43))

# import emoji

# print(emoji.emojize('Python is :thumbs_up:'))

import matplotlib.pyplot as plt
import numpy as np

# # Fixing random state for reproducibility
# np.random.seed(19680801)


# plt.rcdefaults()
# fig, ax = plt.subplots()

# # Example data
# people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
# y_pos = np.arange(len(people))
# performance = 3 + 10 * np.random.rand(len(people))
# error = np.random.rand(len(people))

# ax.barh(y_pos, performance, xerr=error, align='center')
# ax.set_yticks(y_pos, labels=people)
# ax.invert_yaxis()  # labels read top-to-bottom
# ax.set_xlabel('Performance')
# ax.set_title('How fast do you want to go today?')

# plt.show()

# list = [1,2,3,2,7,10]
# plt.plot(list)

# plt.show()

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *

app = ApplicationBuilder().token("5893227796:AAHj9t6W1epzcjmNCBn_4zpx0YuOIDAViLg").build()

app.add_handler(CommandHandler("hello", aloxa))
app.add_handler(CommandHandler("time", time_cmd))
app.add_handler(CommandHandler("help", help_cmd))
app.add_handler(CommandHandler("sum", sum_cmd))
print("server started")
app.run_polling()