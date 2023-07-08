import os
import telegram.ext


from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("""
    /start      -> Displaying welcome message. 
    /help       -> Get information of basic usage of this bot. 
    /contact    -> Contact information.""")

async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Instagram : sir.n3wt0n_")

async def hayatanjing(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("hayat anjing")

async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Instagram : sir.n3wt0n_")

app = ApplicationBuilder().token("6320416802:AAEFPX1kePXFNt8o-ohSvtzINdsFaNrpOps").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("contact", contact))
app.add_handler(CommandHandler("hayatanjing", hayatanjing))

app.run_polling()
