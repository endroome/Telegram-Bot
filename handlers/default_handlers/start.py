from telebot.types import Message
from loader import bot
import sqlite3
from config_data.config import command


@bot.message_handler(commands=['start'])
def started(message: Message) -> None:
    conn = sqlite3.connect('database/command_history.db')
    cursor = conn.cursor()

    cursor.execute('CREATE TABLE IF NOT EXISTS command_history'
                   '(id INTEGER PRIMARY KEY AUTOINCREMENT, user_name TEXT, commands TEXT)')
    conn.commit()
    cursor.execute('SELECT * FROM command_history WHERE user_name=?', (message.from_user.username,))
    if cursor.fetchone() is None:
        cursor.execute('INSERT INTO command_history(user_name, commands) VALUES(?, ?)',
                       (message.from_user.username, ''.join(command)))
        conn.commit()
    else:
        cursor.execute('SELECT * FROM command_history WHERE user_name=?', (message.from_user.username,))

    bot.send_message(message.chat.id, "Приветствую тебя пользователь!\nВас приветствует бот который помогает "
                                      "пользователям найти нужный гаджет, смартфон для себя и близких на сайте Wildberries\n/help команда поможет тебе с командами по боту.")
    command[message.from_user.username] = [message.text]
    conn.close()
