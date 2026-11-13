
import os
import logging
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

# تنظیمات اولیه
TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "سلام! 👋\n\n"
        "من HOOSHONE هستم؛ دستیار هوشمند شما 🤖\n\n"
        "برای شروع، پیام خودت رو برام بفرست. ❤️"
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 راهنمای HOOSHONE\n\n"
        "/start - شروع ربات\n"
        "/help - راهنما\n\n"
        "پیامت رو ارسال کن تا باهات گفتگو کنم."
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return

    await update.message.reply_text(
        "پیامت رو دریافت کردم! ❤️\n\n"
        "موتور هوش مصنوعی HOOSHONE در مرحله اتصال قرار داره. 🤖"
    )


async def main():
    if not TOKEN:
        raise ValueError("BOT_TOKEN environment variable is missing!")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    )

    logger.info("HOOSHONE is starting...")

    await app.initialize()
    await app.start()
    await app.updater.start_polling()

    import asyncio
    await asyncio.Event().wait()


if __name__ == "__main__":
    import asyncio
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("HOOSHONE stopped.")
