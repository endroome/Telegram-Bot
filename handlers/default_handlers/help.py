from telebot.types import Message
from config_data.config import DEFAULT_COMMANDS
from loader import bot
from config_data.config import command


@bot.message_handler(commands=['help'])
def help_command(message: Message) -> None:
    bot.send_message(message.chat.id, '\n'.join(DEFAULT_COMMANDS))

    command[message.from_user.username].append(message.text)
