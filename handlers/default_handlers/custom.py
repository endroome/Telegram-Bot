from telebot.types import Message
from loader import bot
from config_data.config import command, sorted_low


@bot.message_handler(commands=['custom'])
def custom_output(message: Message) -> None:
    bot.send_message(message.chat.id, 'Введи диапазон сортировки по цене(Введите числа через пробел)')

    command[message.from_user.username].append(message.text)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def output_text(message: Message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Приветствую тебя, {message.from_user.first_name}!')
    else:
        try:
            number = message.text.split()
            first_number = int(number[0])
            second_number = int(number[1])
            for elem in sorted_low:
                if first_number <= elem.get('salePriceU') <= second_number:
                    bot.send_message(message.chat.id,
                                     f'Бренд: {elem.get("brand", None)}\nМодель телефона: {elem.get("name", None)}\nЦена: {elem.get("priceU", None)}₽\nЦена после скидки: {elem.get("salePriceU", None)}₽\nПродавец: {elem.get("supplier", None)}\nРейтинг продовца: {elem.get("supplierRating", None)}⭐️\nСсылка на товар: https://www.wildberries.ru/catalog/{elem.get("id", None)}/detail.aspx')
        except ValueError:
            bot.reply_to(message, 'Это не число, введите число')
