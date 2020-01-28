#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler


def hello(update, context):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


def start(update, context):
    keyboard = [[InlineKeyboardButton("Option 1", callback_data='1'),
                 InlineKeyboardButton("Option 2", callback_data='2')],

                [InlineKeyboardButton("Option 3", callback_data='3')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Please choose:', reply_markup=reply_markup)

updater = Updater('1078478278:AAHLLs2LJpTFBt19ppcb0_I9kfANo3cb5gA', use_context=True)

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('start', start))

echo_handler = MessageHandler(Filters.text, echo)
v = echo_handler.__dict__
print(v)
updater.dispatcher.add_handler(echo_handler)

updater.start_polling()
updater.idle()

