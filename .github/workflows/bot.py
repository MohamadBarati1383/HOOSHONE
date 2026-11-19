import logging
import asyncio
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

TOKEN =Done! Congratulations on your new bot. You will find it at t.me/Mrbarati1383bot. You can now add a description, about section and profile picture for your bot, see /help for a list of commands. By the way, when you've finished creating your cool bot, ping our Bot Support if you want a better username for it. Just make sure the bot is fully operational before you do this.

Use this token to access the HTTP API:
9016880516:AAGc1c740bR_9lHjk1jczT-8rXk4uDqOOpE
Keep your token secure and store it safely, it can be used by anyone to control your bot.

For a description of the Bot API, see this page: https://core.telegram.org/bots/api

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "سلام! 👋\n"
        "به ربات HOOSHONE خوش اومدی. ❤️\n\n"
        "ربات با موفقیت فعاله.\n"
        "پیامت رو ارسال کن."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "راهنمای ربات HOOSHONE 🤖\n\n"
        "/start - شروع ربات\n"
        "/help - راهنما\n"
        "/id - نمایش شناسه کاربری\n\n"
        "می‌تونی پیام متنی خودت رو هم ارسال کنی."
    )


async def user_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"شناسه کاربری شما:\n{update.effective_user.id}"
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message.text

    await update.message.reply_text(
        "پیامت با موفقیت دریافت شد. ✅\n\n"
        f"پیام شما: {message}\n\n"
        "ممنون که از HOOSHONE استفاده می‌کنی ❤️"
    )


async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    logger.error("An error occurred:", exc_info=context.error)


async def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("id", user_id))
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    )

    app.add_error_handler(error_handler)

    print("HOOSHONE BOT IS RUNNING...")

    await app.initialize()
    await app.start()
    await app.updater.start_polling()

    try:
        await asyncio.Event().wait()
    finally:
        await app.updater.stop()
        await app.stop()
        await app.shutdown()


if __name__ == "__main__":
    asyncio.run(main())
