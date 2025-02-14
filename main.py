import telebot
from telebot import types
import random

TOKEN = "7947093127:AAFNgyYA3Y0VOAq1NjqG-vlShbnxl-jEXdQ"
bot = telebot.TeleBot(TOKEN)

recipes_db = {
    "супы": [
        {
            "name": "Куриный суп",
            "ingredients": "курица, лук, морковь, лапша, вода, соль",
            "instructions": "1. Варим курицу 30 минут\n2. Добавляем нарезанные овощи\n3. Кладем лапшу\n4. Солим и варим 15 минут"
        },
        {
            "name": "Томатный суп с базиликом",
            "ingredients": "помидоры, чеснок, базилик, сливки, лук, оливковое масло",
            "instructions": "1. Обжарить лук и чеснок\n2. Добавить помидоры\n3. Варить 20 минут\n4. Пюрировать и добавить сливки"
        },
        {
            "name": "Грибной крем-суп",
            "ingredients": "шампиньоны, лук, сливки, картофель, сливочное масло",
            "instructions": "1. Обжарить грибы с луком\n2. Добавить картофель и воду\n3. Варить 25 минут\n4. Измельчить и добавить сливки"
        },
        {
            "name": "Борщ",
            "ingredients": "свекла, капуста, картофель, морковь, лук, говядина, томатная паста, сметана",
            "instructions": "1. Варить бульон 2 часа\n2. Обжарить овощи\n3. Добавить свеклу и капусту\n4. Варить 40 минут"
        },
        {
            "name": "Суп минестроне",
            "ingredients": "цукини, фасоль, помидоры, сельдерей, морковь, лук, пармезан, оливковое масло",
            "instructions": "1. Обжарить овощи\n2. Добавить бульон\n3. Варить 30 минут\n4. Подавать с сыром"
        }
    ],
    "десерты": [
        {
            "name": "Тирамису классический",
            "ingredients": "маскарпоне, печенье савоярди, кофе эспрессо, какао, яйца, сахар",
            "instructions": "1. Взбить маскарпоне с желтками\n2. Собрать слои с кофе\n3. Охлаждать 6 часов\n4. Посыпать какао"
        },
        {
            "name": "Шоколадный фондан",
            "ingredients": "темный шоколад, масло, яйца, сахар, мука",
            "instructions": "1. Растопить шоколад с маслом\n2. Смешать с остальными ингредиентами\n3. Выпекать 12 минут при 200°C"
        },
        {
            "name": "Чизкейк Нью-Йорк",
            "ingredients": "творожный сыр, песочное печенье, сахар, яйца, сливки, ваниль",
            "instructions": "1. Сделать основу из печенья\n2. Смешать начинку\n3. Выпекать 1 час при 160°C\n4. Охладить 6 часов"
        },
        {
            "name": "Панна котта",
            "ingredients": "сливки, желатин, ваниль, сахар, ягодный соус",
            "instructions": "1. Нагреть сливки с сахаром\n2. Добавить желатин\n3. Разлить по формам\n4. Охладить 4 часа"
        }
    ],
    "основные блюда": [
        {
            "name": "Лазанья Болоньезе",
            "ingredients": "листы лазаньи, фарш говяжий, томатный соус, сыр моцарелла, бешамель",
            "instructions": "1. Обжарить фарш\n2. Слоить листы с соусами\n3. Запекать 40 минут при 180°C"
        },
        {
            "name": "Курица терияки",
            "ingredients": "куриное филе, соус терияки, мед, чеснок, кунжут",
            "instructions": "1. Мариновать курицу 30 минут\n2. Обжарить до готовности\n3. Полить соусом и посыпать кунжутом"
        },
        {
            "name": "Паста Карбонара",
            "ingredients": "спагетти, гуанчиале, яйца, пармезан, черный перец",
            "instructions": "1. Обжарить гуанчиале\n2. Смешать яйца с сыром\n3. Соединить с пастой\n4. Добавить перец"
        },
        {
            "name": "Тако с говядиной",
            "ingredients": "лепешки, говяжий фарш, лук, перец чили, помидоры, авокадо, лайм",
            "instructions": "1. Обжарить фарш с овощами\n2. Приготовить сальсу\n3. Собрать тако\n4. Подавать с лаймом"
        }
    ],
    "закуски": [
        {
            "name": "Брускетта с томатами",
            "ingredients": "багет, помидоры, чеснок, оливковое масло, базилик",
            "instructions": "1. Обжарить хлеб\n2. Натереть чесноком\n3. Выложить помидоры с базиликом"
        },
        {
            "name": "Гуакамоле",
            "ingredients": "авокадо, лайм, помидор, кинза, лук, перец чили",
            "instructions": "1. Размять авокадо\n2. Смешать с остальными ингредиентами\n3. Подавать с чипсами"
        },
        {
            "name": "Спринг-роллы",
            "ingredients": "рисовые листы, креветки, рисовая лапша, мята, соус чили",
            "instructions": "1. Замочить листы\n2. Завернуть начинку\n3. Обжарить до хрустящей корочки\n4. Подавать с соусом"
        },
        {
            "name": "Тарталетки с лососем",
            "ingredients": "тарталетки, слабосоленый лосось, сливочный сыр, укроп, лимон",
            "instructions": "1. Намазать сыр в тарталетки\n2. Выложить лосось\n3. Украсить укропом\n4. Сбрызнуть лимоном"
        }
    ],
    "выпечка": [
        {
            "name": "Банановый хлеб",
            "ingredients": "бананы, мука, яйца, сахар, разрыхлитель, масло",
            "instructions": "1. Размять бананы\n2. Смешать все ингредиенты\n3. Выпекать 50 минут при 180°C"
        },
        {
            "name": "Пирог с яблоками",
            "ingredients": "яблоки, мука, сахар, яйца, корица, сливочное масло",
            "instructions": "1. Приготовить тесто\n2. Выложить яблоки\n3. Выпекать 45 минут при 190°C"
        },
        {
            "name": "Круассаны",
            "ingredients": "мука, масло сливочное, дрожжи, молоко, сахар, соль",
            "instructions": "1. Приготовить слоеное тесто\n2. Сформировать круассаны\n3. Выпекать 20 минут при 200°C"
        },
        {
            "name": "Пирог Киш Лорен",
            "ingredients": "тесто, бекон, сыр, яйца, сливки, лук",
            "instructions": "1. Выложить тесто в форму\n2. Обжарить бекон с луком\n3. Залить яичной смесью\n4. Выпекать 40 минут"
        }
    ],
    "напитки": [
        {
            "name": "Мохито",
            "ingredients": "белый ром, лайм, мята, сахар, содовая, лед",
            "instructions": "1. Растереть мяту с лаймом\n2. Добавить лед и ром\n3. Долить содовой"
        },
        {
            "name": "Латте с карамелью",
            "ingredients": "эспрессо, молоко, карамельный сироп, взбитые сливки",
            "instructions": "1. Смешать кофе с сиропом\n2. Взбить молоко\n3. Собрать слоями"
        },
        {
            "name": "Апероль Шприц",
            "ingredients": "апероль, просекко, содовая, апельсин, лед",
            "instructions": "1. Наполнить бокал льдом\n2. Смешать ингредиенты\n3. Украсить долькой апельсина"
        },
        {
            "name": "Матча латте",
            "ingredients": "матча, молоко, мед, ваниль, вода",
            "instructions": "1. Взбить матча с водой\n2. Подогреть молоко\n3. Соединить ингредиенты\n4. Добавить мед"
        }
    ]
}

favorites_db = {}

def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    buttons = [
        "🍴 Случайный рецепт",
        "📂 Поиск по категориям",
        "🔍 Поиск по ингредиентам",
        "📜 Доступные ингредиенты",
        "❤️ Избранное"
    ]
    markup.add(*[types.KeyboardButton(btn) for btn in buttons])
    return markup

def get_unique_ingredients():
    ingredients = set()
    for category in recipes_db.values():
        for recipe in category:
            for ingredient in recipe['ingredients'].split(','):
                cleaned = ingredient.strip().lower()
                if cleaned: ingredients.add(cleaned)
    return sorted(ingredients)

def add_fav_button(recipe):
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton("❤️ Добавить в избранное", callback_data=f"add_fav_{recipe['name']}")
    markup.add(btn)
    return markup

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 
                    "🍳 Добро пожаловать в Кулинарного Помощника!\nВыберите действие:",
                    reply_markup=main_menu())

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "🍴 Случайный рецепт":
        send_random_recipe(message)
    elif message.text == "📂 Поиск по категориям":
        show_categories(message)
    elif message.text == "🔍 Поиск по ингредиентам":
        bot.send_message(message.chat.id, "Введите ингредиенты через запятую:")
    elif message.text == "📜 Доступные ингредиенты":
        show_available_ingredients(message)
    elif message.text == "❤️ Избранное":
        show_favorites(message)
    else:
        search_by_ingredients(message)

def show_available_ingredients(message):
    ingredients = get_unique_ingredients()
    text = "🍴 Доступные ингредиенты:\n\n• " + "\n• ".join(ingredients) if ingredients else "Ингредиенты пока не добавлены 😞"
    bot.send_message(message.chat.id, text)

def show_categories(message):
    markup = types.InlineKeyboardMarkup()
    for category in recipes_db.keys():
        markup.add(types.InlineKeyboardButton(category, callback_data=category))
    bot.send_message(message.chat.id, "Выберите категорию:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data.startswith('add_fav_'):
        recipe_name = call.data[8:]
        add_to_favorites(call)
    elif call.data.startswith('del_fav_'):
        recipe_name = call.data[8:]
        remove_from_favorites(call)
    elif call.data in recipes_db:
        send_category_recipes(call.message, call.data)

def send_category_recipes(message, category):
    for recipe in recipes_db[category]:
        text = f"🍲 {recipe['name']}\n\nИнгредиенты:\n{recipe['ingredients']}\n\nИнструкция:\n{recipe['instructions']}"
        bot.send_message(message.chat.id, text, reply_markup=add_fav_button(recipe))

def send_random_recipe(message):
    all_recipes = [recipe for category in recipes_db.values() for recipe in category]
    if all_recipes:
        recipe = random.choice(all_recipes)
        text = f"🎲 Случайный рецепт: {recipe['name']}\n\nИнгредиенты:\n{recipe['ingredients']}\n\nИнструкция:\n{recipe['instructions']}"
        bot.send_message(message.chat.id, text, reply_markup=add_fav_button(recipe))
    else:
        bot.send_message(message.chat.id, "Рецептов пока нет 😞")

def search_by_ingredients(message):
    ingredients = [i.strip().lower() for i in message.text.split(',')]
    found_recipes = []
    
    for category in recipes_db.values():
        for recipe in category:
            recipe_ingredients = recipe['ingredients'].lower()
            if all(ingredient in recipe_ingredients for ingredient in ingredients):
                found_recipes.append(recipe)
    
    if found_recipes:
        for recipe in found_recipes:
            text = f"🔍 Найден рецепт: {recipe['name']}\n\nИнгредиенты:\n{recipe['ingredients']}\n\nИнструкция:\n{recipe['instructions']}"
            bot.send_message(message.chat.id, text, reply_markup=add_fav_button(recipe))
    else:
        bot.send_message(message.chat.id, "По вашему запросу ничего не найдено 😞")

def show_favorites(message):
    user_id = message.chat.id
    if user_id not in favorites_db or not favorites_db[user_id]:
        bot.send_message(user_id, "В избранном пока ничего нет 😞")
        return
    
    bot.send_message(user_id, "❤️ Ваше избранное:")
    for recipe in favorites_db[user_id]:
        text = f"🍲 {recipe['name']}\n\nИнгредиенты:\n{recipe['ingredients']}\n\nИнструкция:\n{recipe['instructions']}"
        markup = types.InlineKeyboardMarkup()
        btn = types.InlineKeyboardButton("🗑 Удалить", callback_data=f"del_fav_{recipe['name']}")
        markup.add(btn)
        bot.send_message(user_id, text, reply_markup=markup)

def add_to_favorites(call):
    user_id = call.message.chat.id
    recipe_name = call.data[8:]
    recipe = find_recipe_by_name(recipe_name)
    
    if not recipe:
        bot.answer_callback_query(call.id, "Рецепт не найден 😞")
        return
    
    if user_id not in favorites_db:
        favorites_db[user_id] = []
    
    if recipe not in favorites_db[user_id]:
        favorites_db[user_id].append(recipe)
        bot.answer_callback_query(call.id, "✅ Добавлено в избранное!")
    else:
        bot.answer_callback_query(call.id, "⚠️ Уже в избранном!")

def remove_from_favorites(call):
    user_id = call.message.chat.id
    recipe_name = call.data[8:]
    
    if user_id in favorites_db:
        favorites_db[user_id] = [r for r in favorites_db[user_id] if r['name'] != recipe_name]
        bot.answer_callback_query(call.id, "❌ Удалено из избранного")

def find_recipe_by_name(name):
    for category in recipes_db.values():
        for recipe in category:
            if recipe['name'] == name:
                return recipe
    return None

if __name__ == '__main__':
    bot.polling(none_stop=True)
   
