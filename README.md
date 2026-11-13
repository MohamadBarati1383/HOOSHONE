# HOOSHimport os import logging from telegram import Update from telegram.ext import ( Application, CommandHandler, MessageHandler, ContextTypes, filters )
logging.basicConfig( format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO )
BOT_TOKEN = os.getenv("BOT_TOKEN")
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE): await update.message.reply_text( "سلام! ❤️\n" "من HooshOne هستم؛ دستیار هوشمند شما! 🤖\n\n" "چطور می‌تونم کمکت کنم؟" )
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE): await update.message.reply_text( "راهنمای HooshOne 📚\n\n" "/start - شروع ربات\n" "/help - راهنما\n\n" "پیامت رو برام بفرست!" )
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE): user_message = update.message.text
await update.message.reply_text(
    f"پیامت رو دریافت کردم! ❤️\n\n"
    f"نوشتی:\n{user_message}\n\n"
    "من HooshOne هستم و به‌زودی هوشمندتر می‌شم! 🚀"
)
def main(): if not BOT_TOKEN: raise RuntimeError("BOT_TOKEN is not configured!")
app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(
    MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
)

print("HooshOne is running! 🤖")
app.run_polling()
if name == "main": main()
