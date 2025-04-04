from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv
import os


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("logged start")
    await update.message.reply_text("Hello, bot!")

def main():
    load_dotenv()
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    print(BOT_TOKEN)
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__== "__main__":
    main()