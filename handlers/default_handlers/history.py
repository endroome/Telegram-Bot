from loader import bot
from telebot.types import Message
from config_data.config import command
import sqlite3

@bot.message_handler(commands=['history'])
def history(message: Message) -> None:
    conn = sqlite3.connect('database/command_history.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM command_history WHERE user_name=?', (message.from_user.username,))
    if cursor.fetchone() is None:
        cursor.execute('INSERT INTO command_history(user_name, commands) VALUES(?, ?)',
                       (message.from_user.username, ''.join(command)))
        conn.commit()
    cursor.execute('UPDATE command_history SET commands=? WHERE user_name=?',
                   (", ".join(command[message.from_user.username]), message.from_user.username))
    conn.commit()
    cursor.execute('SELECT * FROM command_history')
    users_commands = cursor.fetchall()
    for index in users_commands:
        if message.from_user.username in index:
            bot.send_message(message.chat.id, f'История запросов пользователя: {"".join(index[2:])}')
    conn.close()
