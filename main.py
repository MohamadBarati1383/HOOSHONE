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

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)
TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "سلام! 🤖\n"
        "من HOOSHONE هستم.\n"
        "دستیار هوشمند مدیریت تلگرام.\n"
        "برای مشاهده دستورات /help را بزنید."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📌 دستورات ربات:\n"
        "/start - شروع ربات\n"
        "/help - راهنما\n"
        "/id - نمایش شناسه\n"
        "/admin - بررسی مدیر بودن\n"
    )


async def get_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id

    await update.message.reply_text(
        f"شناسه چت: {chat_id}\n"
        f"شناسه کاربر: {user_id}"
    )


async def check_admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    user = update.effective_user

    if chat.type == "private":
        await update.message.reply_text("این دستور مخصوص گروه‌هاست.")
        return

    try:
        member = await context.bot.get_chat_member(chat.id, user.id)

        if member.status in ("administrator", "creator"):
            await update.message.reply_text("✅ شما مدیر این گروه هستید.")
        else:
            await update.message.reply_text("❌ شما مدیر این گروه نیستید.")

    except Exception:
        logger.exception("Admin check failed")
        await update.message.reply_text("خطا در بررسی دسترسی مدیر.")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return

    text = update.message.text.strip()

    if text:
        await update.message.reply_text(f"پیامت دریافت شد: {text}")


async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    logger.error("An error occurred", exc_info=context.error)


 def main():
    if not TOKEN:
        raise RuntimeError("لطفاً متغیر محیطی BOT_TOKEN را تنظیم کنید.")

    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("id", get_id))
    application.add_handler(CommandHandler("admin", check_admin))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.add_error_handler(error_handler)

    logger.info("HOOSHONE bot is running...")
    application.run_polling()


if __name__ == "__main__":
    main()
