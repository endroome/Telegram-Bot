from telebot.types import Message
from loader import bot
from config_data.config import command

@bot.message_handler(commands=['hello_world'])
def greeting(message: Message) -> None:
    bot.send_message(message.chat.id, f'Приветствую тебя, {message.from_user.first_name}!')

    command[message.from_user.username].append(message.text)
