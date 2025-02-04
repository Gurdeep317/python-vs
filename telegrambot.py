from typing import final
from telegram import Update
from telegram.ext import Application,CommandHandler,MessageHandler,filters,ContextTypes
TOKEN: Final ='7282707731:AAFAmQhkopcARz3Vk5Bp41tB-4zpRY8IwMQ'
BOT_USERNAME:Final = 'aa_applebot'
async def start_command(update:Update,context:ContextTypes.Default_Type):
    await update.message.reply_text('Hello! Thanks for chatting with me! I am a apple')