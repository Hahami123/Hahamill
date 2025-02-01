import telebot
from telebot import types
import logging

API_TOKEN = '7147793439:AAFhI7r1XPbtI1CBuymAatnwCy_Vb-dpYhE'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    btn_str = types.InlineKeyboardButton('Выбрать продукт', callback_data='select_product')
    markup.add(btn_str)
    bot.send_message(message.chat.id, f'Привет {message.from_user.first_name}! это кулинарный бот помошник .', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'select_product')
def select_product(call):
    markup1 = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Яйцо', callback_data='Egg') 
    btn2 = types.InlineKeyboardButton('Молоко', callback_data='Moloko')
    btn3 = types.InlineKeyboardButton('Мясо', callback_data='Maso')
    btn4 = types.InlineKeyboardButton('Макароны', callback_data='Pasta')
    btn5 = types.InlineKeyboardButton('Сыр', callback_data='Cheese')
    btn6 = types.InlineKeyboardButton('Гречка', callback_data='Grechka')
    btn7 = types.InlineKeyboardButton('Рыба', callback_data='Fish')
    btn8 = types.InlineKeyboardButton('Картошка', callback_data='Kartoshka')
    markup1.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)

    bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='Выберите продукт:',reply_markup=markup1)

@bot.callback_query_handler(func=lambda call: call.data in ['Egg', 'Moloko', 'Maso', 'Pasta', 'Cheese', 'Grechka', 'Fish', 'Kartoshka'])
def choose_product(call):
    product = call.data.lower()
    markup2 = types.InlineKeyboardMarkup()
    btn9 = types.InlineKeyboardButton('Яичница', callback_data='Egg_gotovo')
    btn10 = types.InlineKeyboardButton('Омлет', callback_data='Omelet')
    markup2.add(btn9, btn10)

    bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text=f'Вы выбрали {product}. Что дальше?',
        reply_markup=markup2
    )

@bot.callback_query_handler(func=lambda call: call.data == 'Egg_gotovo')
def egg_gotovo(call):
    # Создаем кнопку "Назад"
    markup3 = types.InlineKeyboardMarkup()
    btn_nazad = types.InlineKeyboardButton('Назад', callback_data='back')
    markup3.add(btn_nazad)
    
    # Открываем картинку
    with open('яичница.jpg', 'rb') as photo:
        bot.send_photo(call.message.chat.id, photo)
        
    bot.send_message(call.message.chat.id, 'Натрите сыр и огурцы на крупной тёрке. Количество этих ингредиентов должно быть примерно одинаковым.Отделите яичные желтки от белков. Добавьте к белкам соль, перец и майонез и взбейте вилкой.Растопите масло на сковороде на слабом огне. Выложите огурцы и сыр и слегка обжарьте. Когда сыр начнёт плавиться, влейте белковую массу.', reply_markup=markup3)
# Обработчик для кнопки "Назад"
@bot.callback_query_handler(func=lambda call: call.data == 'back')
def back_to_products(call):
    # Возвращаемся к выбору продуктов
    markup = types.InlineKeyboardMarkup()
    products = [
        ('Яйца', 'Egg'),
        ('Молоко', 'Moloko'),
        ('Мясо', 'Maso'),
        ('Паста', 'Pasta'),
        ('Сыр', 'Cheese'),
        ('Гречка', 'Grechka'),
        ('Рыба', 'Fish'),
        ('Картофель', 'Kartoshka')
    ]
    for product_name, product_callback in products:
        button = types.InlineKeyboardButton(product_name, callback_data=product_callback)
        markup.add(button)

    bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text="Выберите продукт:",
        reply_markup=markup
    )

if __name__ == "__main__":


    bot.polling(none_stop=True)
