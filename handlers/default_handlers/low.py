from telebot.types import Message
from config_data.config import command, sorted_low
from loader import bot


@bot.message_handler(commands=['low'])
def low_output(message: Message) -> None:
    bot.send_message(message.chat.id, 'Нашел смартфоны по возрастанию цены.')
    for elem in sorted_low:
        bot.send_message(message.chat.id,
                         f'Бренд: {elem.get("brand", None)}\nМодель телефона: {elem.get("name", None)}\nЦена: {elem.get("priceU", None)}₽\nЦена после скидки: {elem.get("salePriceU", None)}₽\nПродавец: {elem.get("supplier", None)}\nРейтинг продовца: {elem.get("supplierRating", None)}⭐️\nСсылка на товар: https://www.wildberries.ru/catalog/{elem.get("id", None)}/detail.aspx')

    command[message.from_user.username].append(message.text)
