import html
import random
import  SaitamaRobot.modules.abuse_string as abuse_string
from SaitamaRobot import dispatcher
from telegram import ParseMode, Update, Bot
from SaitamaRobot.modules.disable import DisableAbleCommandHandler
from telegram.ext import CallbackContext, run_async

@run_async
def abuse(update: Update, context: CallbackContext):
    args = context.args
    update.effective_message.reply_text(random.choice(abuse_string.ABUSE))

ABUSE_HANDLER = DisableAbleCommandHandler("abuse", abuse)

dispatcher.add_handler(abuse_HANDLER)
