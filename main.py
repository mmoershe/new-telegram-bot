from telegram import Update
from telegram.ext import ApplicationBuilder, Application, filters, ContextTypes, CommandHandler, MessageHandler

from modules.CONST import TOKEN, CHAT_ID
from modules.ollama_llm import generate_response

import logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def startup(application: Application): 
    prompt: str = '''
    Generate a very very short and brief message (maximum one sentence!) articulating that you have just woken up or just started working or are now in my service. The message should be in the style of fromsoftware games, such as Dark Soul 1, Dark Souls 2, Dark Souls 3, Bloodborne or Elden Ring, using the fantasy old english these games typical use. Just output the message as a plain string without any surrounding quotation marks or anything else. 
    '''
    # message: str = generate_response(prompt)
    message: str = "meddl!"
    await application.bot.send_message(chat_id=CHAT_ID, text=message)


async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=CHAT_ID, text="bot running.")


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
    application = ApplicationBuilder().token(TOKEN).post_init(startup).build()

    application.add_handler(CommandHandler('status', status))
    application.add_handler(CommandHandler('yt', yt))

    message_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), regular_message)
    application.add_handler(message_handler)

    application.run_polling()
