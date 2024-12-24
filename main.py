from telegram import Update
from telegram.ext import ApplicationBuilder, filters, ContextTypes, CommandHandler, MessageHandler

from modules.CONST import TOKEN, CHAT_ID
from modules.ollama_llm import generate_response

import logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=CHAT_ID, text="I'm a bot, please talk to me!")


async def yt(update: Update, context: ContextTypes.DEFAULT_TYPE): 
    url: str = update.message.text.replace("/yt", "").strip()
    print(f"{url = }")
    await context.bot.send_message(chat_id=CHAT_ID, text=f"{url = }")


async def regular_message(update: Update, context: ContextTypes.DEFAULT_TYPE): 
    message: str = update.message.text
    response: str = generate_response(message)
    # await context.bot.send_message(chat_id=CHAT_ID, text="[AI RESPONSE]")
    await context.bot.send_message(chat_id=CHAT_ID, text=response)


if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    youtube_handler = CommandHandler('yt', yt)
    application.add_handler(youtube_handler)

    message_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), regular_message)
    application.add_handler(message_handler)

    application.run_polling()
