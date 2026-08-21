import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "سلام! 👋\n"
        "زه د کمپیوټر ساینس بوټ یم.\n\n"
        "دا موضوعات راسره زده کولی شې:\n"
        "1️⃣ Python\n"
        "2️⃣ Programming\n"
        "3️⃣ Algorithms\n"
        "4️⃣ Database\n"
        "5️⃣ Computer basics\n\n"
        "یوه موضوع ولیکه، زه به معلومات درکړم."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "د کارولو لپاره /start ولیکه.\n"
        "بیا Python، Programming، Algorithms یا Database ولیکه."
    )


async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    answers = {
        "python": "🐍 Python یوه اسانه او مشهوره Programming ژبه ده.",
        "programming": "💻 Programming د کمپیوټر لپاره د پروګرامونو جوړولو طریقه ده.",
        "algorithms": "🧠 Algorithm د یوې ستونزې د حل لپاره منظم ګامونه دي.",
        "database": "🗄️ Database د معلوماتو د ذخیره او تنظیم لپاره کارېږي.",
        "computer": "🖥️ Computer یو برېښنايي سیستم دی چې معلومات اخلي، پروسس کوي او نتیجه ورکوي.",
    }

    reply = answers.get(
        text,
        "📚 دا موضوع مې لا نه ده زده کړې. Python، Programming، Algorithms، Database یا Computer ولیکه."
    )

    await update.message.reply_text(reply)


def main():
    if not TOKEN:
        raise ValueError("BOT_TOKEN is not set")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))

    app.run_polling()


if __name__ == "__main__":
    main()
