import os import logging
from telegram import Update from telegram.ext import ( Application, CommandHandler, MessageHandler, ContextTypes, filters, )
======
CONFIGURATION
======
TOKEN = os.getenv("BOT_TOKEN")
logging.basicConfig( format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO, )
logger = logging.getLogger(name)
======
START COMMAND
======
async def start( update: Update, context: ContextTypes.DEFAULT_TYPE ): await update.message.reply_text( "سلام! 👋\n\n" "من HOOSHONE هستم؛ دستیار هوشمند شما 🤖\n\n" "خوش اومدی! ❤️\n" "پیامت رو بفرست تا با هم گفتگو کنیم." )
======
HELP COMMAND
======
async def help_command( update: Update, context: ContextTypes.DEFAULT_TYPE ): await update.message.reply_text( "🤖 راهنمای HOOSHONE\n\n" "/start - شروع ربات\n" "/help - نمایش راهنما\n\n" "پیامت رو ارسال کن. ❤️" )
======
MESSAGE HANDLER
======
async def handle_message( update: Update, context: ContextTypes.DEFAULT_TYPE ): if not update.message or not update.message.text: return
await update.message.reply_text(
    "پیامت رو دریافت کردم! ❤️\n\n"
    "موتور هوش مصنوعی HOOSHONE "
    "هنوز به این ربات متصل نشده است. 🤖"
)
======
ERROR HANDLER
======
async def error_handler( update: object, context: ContextTypes.DEFAULT_TYPE ): logger.error( "An error occurred:", exc_info=context.error )
======
MAIN FUNCTION
======
def main():
if not TOKEN:
    raise ValueError(
        "BOT_TOKEN environment variable is missing!"
    )

app = Application.builder().token(TOKEN).build()

app.add_handler(
    CommandHandler("start", start)
)

app.add_handler(
    CommandHandler("help", help_command)
)

app.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        handle_message
    )
)

app.add_error_handler(error_handler)

logger.info("HOOSHONE is starting...")

app.run_polling(
    drop_pending_updates=True
)
======
RUN BOT
======
if name == "main": main()
