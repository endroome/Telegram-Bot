from telebot.types import Message
from loader import bot
from config_data.config import command
from config_data.config import sorted_high

@bot.message_handler(commands=['high'])
def high_output(message: Message) -> None:
    bot.send_message(message.chat.id, 'Нашел смартфоны по убыванию цены.')
    for elem in sorted_high:
        bot.send_message(message.chat.id,
                         f'Бренд: {elem.get("brand", None)}\nМодель телефона: {elem.get("name", None)}\nЦена: {elem.get("priceU", None)}₽\nЦена после скидки: {elem.get("salePriceU", None)}₽\nПродавец: {elem.get("supplier", None)}\nРейтинг продовца: {elem.get("supplierRating", None)}⭐️\nСсылка на товар: https://www.wildberries.ru/catalog/{elem.get("id", None)}/detail.aspx')

    command[message.from_user.username].append(message.text)
