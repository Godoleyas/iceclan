import logging
logger = logging.getLogger(__name__)

import asyncio
from pyrogram import filters
from bot import feedback
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from translation import Translation
from config import Config

@feedback.on_message(filters.text)
async def text(c, m):
      if m.from_user.id in Config.LOGIN:
         if m.text == Config.PASS:
            Config.LOGIN.remove(m.from_user.id)
            Config.OWNER.append(m.from_user.id)
            await m.reply_text(text="Fair enough. From now on you will recieve message from users but if this bot restarts you have to enter the password again :)")
         if m.text != Config.PASS:
            Config.LOGIN.remove(m.from_user.id)
            await m.reply_text(text="**Ur impostor? if ur real ice u could have entered the password correct lmao**", parse_mode="markdown")
      if m.from_user.id in Config.feedback:
         button = [[
                   InlineKeyboardButton("Sure", callback_data="yes"),
                   InlineKeyboardButton("Nah", callback_data="cancel")
                  ]]
         markup = InlineKeyboardMarkup(button)
         await m.reply_text(text="Do you really want to send this?",
                            reply_markup=markup,
                            quote=True)
      try:
          if Config.SEND is not None:
             id = Config.SEND[0]
             await c.send_message(chat_id=int(id), text=m.text, parse_mode="markdown")
             Config.SEND.remove(id)
             await c.send_message(chat_id=m.chat.id, text="Sent")
      except:
          pass

@feedback.on_message(filters.command(["start"]))
async def start(c, m):
      button = [[
                InlineKeyboardButton("Register", callback_data="register"),
                InlineKeyboardButton("Rules", callback_data="rules"),
                ],
                [
                InlineKeyboardButton("About", callback_data="about"),
                InlineKeyboardButton("Login", callback_data="login"),
               ]]
      markup = InlineKeyboardMarkup(button)
      await c.send_message(chat_id=m.chat.id,
                           text=Translation.START,
                           disable_web_page_preview=True,
                           reply_to_message_id=m.message_id,
                           reply_markup=markup)
