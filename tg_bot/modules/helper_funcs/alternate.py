import telegram
from telegram.error import BadRequest
from functools import wraps
from telegram import error, ChatAction
from telegram import User, Chat, ChatMember, Update, Bot

def send_message(message, text, *args, **kwargs):
    try:
        return message.reply_text(text, *args, **kwargs)
    except BadRequest as err:
        if str(err) == "Reply message not found":
            return message.reply_text(text, quote=False, *args, **kwargs)


def typing_action(func):
    """Sends typing action while processing func command."""

    @wraps(func)
    def command_func(bot: Bot, update: Update, *args, **kwargs):
        bot.send_chat_action(
            chat_id=update.effective_chat.id, action=ChatAction.TYPING)
        return func(bot, update, *args, **kwargs)

    return command_func
