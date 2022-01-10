import content as content
import keyboard as keyboard
import telebot
import psycopg2
import datetime

conn = psycopg2.connect(database="telebot",
                        user="postgres",
                        password="1234",
                        host="localhost",
                        port="5432")
cursor = conn.cursor()

token = "5018976092:AAFkFvUXFYDLkv5gIonvG70KgPURa73o22w"

bot = telebot.TeleBot(token)


def weeker():
    today = datetime.datetime.today().strftime("%W")
    if int(today) % 2 == 0:
        return "нижняя неделя"
    else:
        return "верхняя неделя"

@bot.message_handler(commands=["start"])
def start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup()
    keyboard.row('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница')
    # keyboard.row()
    keyboard.row('Расписание на текущую неделю')
    keyboard.row('Расписание на следующую неделю')
    bot.send_message(message.chat.id, 'Чтобы увидеть расписание группы, нажмите кнопки ниже', reply_markup=keyboard)

@bot.message_handler(commands=["week"])
def week(message):
    bot.send_message(message.chat.id, "Cейчас: " + weeker())


@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, "Здравствуйте! Данный бот показывает расписания группы БФИ2101"
                     "\nКоманды: \n /help - сведения о работе бота\n /mtuci - ссылка на сайт университета\n /week - Вы можете узнать какая сейчас неделя\n /start - запускает бот")


@bot.message_handler(commands=["mtuci"])
def mtuci(message):
    bot.send_message(message.chat.id, "https://mtuci.ru/")


@bot.message_handler(content_types=["text"])
def answer(message):
    a = message.text.lower()
    if a == 'понедельник':
        if weeker() == 'верхняя неделя':
            cursor.execute("Select id, full_name from teacher")
            teacher = list(cursor.fetchall())
            cursor.execute("Select subject, room_numb, start_time from timetable"
                           " Where day = 'Понедельник' and week_status = 'Вверхняя'")
            time = list(cursor.fetchall())
            bot.send_message(message.chat.id,
                             text='\n_____Понедельник_____\n_____Верхняя неделя_____\n'
                                  "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                                  "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                                  "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n".format(

                                 time[0][0], time[0][1], time[0][2], teacher[14][1],
                                 time[1][0], time[1][1], time[1][2], teacher[12][1],
                                 time[2][0], time[2][1], time[2][2], teacher[10][1]))
        elif weeker() == "нижняя неделя":
            cursor.execute("Select id, full_name from teacher")
            teacher = list(cursor.fetchall())
            cursor.execute("Select subject, room_numb, start_time from timetable"
                           " Where day = 'Понедельник' and week_status = 'Нижняя'")
            time = list(cursor.fetchall())
            bot.send_message(message.chat.id,
                             text='\n_____Понедельник_____\n_____Нижняя неделя_____\n'
                                  "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                                  "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                                  "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n".format(

                                 time[0][0], time[0][1], time[0][2], teacher[14][1],
                                 time[1][0], time[1][1], time[1][2], teacher[12][1],
                                 time[2][0], time[2][1], time[2][2], teacher[10][1]))
    elif a == 'вторник':
        if weeker() == "верхняя неделя":
            cursor.execute("Select id, full_name from teacher")
            teacher = list(cursor.fetchall())
            cursor.execute("Select subject, room_numb, start_time from timetable"
                           " Where day = 'Вторник' and week_status = 'Вверхняя'")
            time = list(cursor.fetchall())
            bot.send_message(message.chat.id,
                             text='\n_____Вторник_____\n_____Верхняя неделя_____\n'
                                  "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                                  "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                                  "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                                  "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                                  "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n".format(

                                 time[0][0], time[0][1], time[0][2], teacher[0][1],
                                 time[1][0], time[1][1], time[1][2], teacher[2][1],
                                 time[2][0], time[2][1], time[2][2], teacher[4][1],
                                 time[3][0], time[3][1], time[3][2], teacher[7][1],
                                 time[4][0], time[4][1], time[4][2], teacher[11][1]))

        elif weeker() == "нижняя неделя":
            cursor.execute("Select id, full_name from teacher")
            teacher = list(cursor.fetchall())
            cursor.execute("Select subject, room_numb, start_time from timetable"
                           " Where day = 'Вторник' and week_status = 'Нижняя'")
            time = list(cursor.fetchall())
            bot.send_message(message.chat.id,
                             text='\n_____Вторник_____\n_____Нижняя неделя_____\n'
                                  "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                                  "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n".format(

                                 time[0][0], time[0][1], time[0][2], teacher[0][1],
                                 time[1][0], time[1][1], time[1][2], teacher[2][1]))

    elif a == 'среда':
        if weeker() == "верхняя неделя":
            cursor.execute("Select id, full_name from teacher")
            teacher = list(cursor.fetchall())
            cursor.execute("Select subject, room_numb, start_time from timetable"
                           " Where day = 'Среда' and week_status = 'Вверхняя'")
            time = list(cursor.fetchall())
            bot.send_message(message.chat.id,
                             text='\n_____Среда_____\n_____Верхняя неделя_____\n'
                                  "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                                  "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n".format(

                                 time[0][0], time[0][1], time[0][2], teacher[15][1],
                                 time[1][0], time[1][1], time[1][2], teacher[9][1]))

        elif weeker() == "нижняя неделя":
            cursor.execute("Select id, full_name from teacher")
            teacher = list(cursor.fetchall())
            cursor.execute("Select subject, room_numb, start_time from timetable"
                           " Where day = 'Среда' and week_status = 'Нижняя'")
            time = list(cursor.fetchall())
            bot.send_message(message.chat.id,
                             text='\n_____Среда_____\n_____Нижняя неделя_____\n'
                                  "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                                  "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n".format(

                                 time[0][0], time[0][1], time[0][2], teacher[8][1],
                                 time[1][0], time[1][1], time[1][2], teacher[9][1]))

    elif a == 'четверг':
        if weeker() == "верхняя неделя":
            cursor.execute("Select id, full_name from teacher")
            teacher = list(cursor.fetchall())
            cursor.execute("Select subject, room_numb, start_time from timetable"
                           " Where day = 'Четверг' and week_status = 'Вверхняя'")
            time = list(cursor.fetchall())
            bot.send_message(message.chat.id,
                             text='\n_____Четверг_____\n_____Верхняя неделя_____\n'
                                  "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                                  "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                                  "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                                  "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n".format(

                                 time[0][0], time[0][1], time[0][2], teacher[5][1],
                                 time[1][0], time[1][1], time[1][2], teacher[1][1],
                                 time[2][0], time[2][1], time[2][2], teacher[3][1],
                                 time[3][0], time[3][1], time[3][2], teacher[13][1]))

        elif weeker() == "нижняя неделя":
            cursor.execute("Select id, full_name from teacher")
            teacher = list(cursor.fetchall())
            cursor.execute("Select subject, room_numb, start_time from timetable"
                           " Where day = 'Четверг' and week_status = 'Нижняя'")
            time = list(cursor.fetchall())
            bot.send_message(message.chat.id,
                             text='\n_____Четверг_____\n_____Нижняя неделя_____\n'
                                  "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                                  "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n".format(

                                 time[0][0], time[0][1], time[0][2], teacher[16][1],
                                 time[1][0], time[1][1], time[1][2], teacher[16][1]))

    elif a == 'пятница':
        if weeker() == "верхняя неделя":
            cursor.execute("Select id, full_name from teacher")
            teacher = list(cursor.fetchall())
            cursor.execute("Select subject, room_numb, start_time from timetable"
                           " Where day = 'Пятница' and week_status = 'Верхняя'")
            time = list(cursor.fetchall())
            bot.send_message(message.chat.id,
                             text='\n_____Пятница_____\n_____Верхняя неделя_____\n'
                                  "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                                  "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n".format(

                                 time[1][0], time[1][1], time[1][2], teacher[9][1],
                                 time[0][0], time[0][1], time[0][2], teacher[6][1]))

        elif weeker() == "нижняя неделя":
            cursor.execute("Select id, full_name from teacher")
            teacher = list(cursor.fetchall())
            cursor.execute("Select subject, room_numb, start_time from timetable"
                           " Where day = 'Пятница' and week_status = 'Нижняя'")
            time = list(cursor.fetchall())
            bot.send_message(message.chat.id,
                             text='\n_____Пятница_____\n_____Нижняя неделя_____\n'
                                  "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                                  "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n".format(

                                 time[1][0], time[1][1], time[1][2], teacher[9][1],
                                 time[0][0], time[0][1], time[0][2], teacher[6][1]))

    elif a == 'расписание на текущую неделю':
        if weeker() == 'нижняя неделя':
            cursor.execute("Select id, full_name from teacher")
            teacher = list(cursor.fetchall())
            cursor.execute("Select subject, room_numb, start_time from timetable"
                           " Where week_status = 'Нижняя'")
            Time = list(cursor.fetchall())

            bot.send_message(message.chat.id,
                             text='\n_____Понедельник_____Нижняя неделя_____\n'
                                  "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                                  "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                                  "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"

                                  "\n____Вторник_____Нижняя неделя_____\n"
                                  "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                                  "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"


                                  "\n____Среда_____Нижняяя неделя_____\n"
                                  "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                                  "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"

                                  "\n_____Четверг_____Нижняя неделя_____\n"
                                  "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                                  "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"


                                  "\n_____Пятница_____Нижняя неделя_____\n"
                                  "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                                  "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n".format(
                                 Time[0][0], Time[0][1], Time[0][2], teacher[14][1],
                                 Time[1][0], Time[1][1], Time[1][2], teacher[12][1],
                                 Time[2][0], Time[2][1], Time[2][2], teacher[10][1],

                                 Time[3][0], Time[3][1], Time[3][2], teacher[0][1],
                                 Time[4][0], Time[4][1], Time[4][2], teacher[2][1],

                                 Time[5][0], Time[5][1], Time[5][2], teacher[8][1],
                                 Time[9][0], Time[9][1], Time[9][2], teacher[9][1],

                                 Time[6][0], Time[6][1], Time[6][2], teacher[16][1],
                                 Time[7][0], Time[7][1], Time[7][2], teacher[16][1],

                                 Time[8][0], Time[8][1], Time[8][2], teacher[9][1],
                                 Time[10][0], Time[10][1], Time[10][2], teacher[6][1]))

    elif a == 'расписание на следующую неделю':
        weeker() == 'верхняя неделя'
        cursor.execute("Select id, full_name from teacher")
        teachers = list(cursor.fetchall())
        cursor.execute("Select subject, room_numb, start_time from timetable Where week_status = 'Верхняя'")
        Time = list(cursor.fetchall())

        bot.send_message(message.chat.id,
                         text='\n_____Понедельник_____Верхняя неделя_____\n'
                              "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                              "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                              "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"

                              "\n_____Вторник_____Верхняя неделя_____\n"
                              "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                              "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                              "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                              "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                              "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"

                              "\n_____Среда_____Верхняя неделя_____\n"
                              "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                              "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"

                              "\n_____Четверг_____Верхняя неделя_____\n"
                              "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                              "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                              "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                              "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"

                              "\n_____Пятница_____Верхняя неделя_____\n"
                              "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                              "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n".format(

                             Time[0][0], Time[0][1], Time[0][2], teachers[14][1],
                             Time[1][0], Time[1][1], Time[1][2], teachers[12][1],
                             Time[2][0], Time[2][1], Time[2][2], teachers[10][1],

                             Time[3][0], Time[3][1], Time[3][2], teachers[0][1],
                             Time[4][0], Time[4][1], Time[4][2], teachers[2][1],
                             Time[5][0], Time[5][1], Time[5][2], teachers[4][1],
                             Time[6][0], Time[6][1], Time[6][2], teachers[7][1],
                             Time[7][0], Time[7][1], Time[7][2], teachers[11][1],

                             Time[8][0], Time[8][1], Time[8][2], teachers[15][1],
                             Time[13][0], Time[13][1], Time[13][2], teachers[9][1],

                             Time[9][0], Time[9][1], Time[9][2], teachers[5][1],
                             Time[15][0], Time[15][1], Time[15][2], teachers[1][1],
                             Time[10][0], Time[10][1], Time[10][2], teachers[3][1],
                             Time[11][0], Time[11][1], Time[11][2], teachers[13][1],

                             Time[14][0], Time[14][1], Time[14][2], teachers[9][1],
                             Time[12][0], Time[12][1], Time[12][2], teachers[6][1]))

    else:
        bot.send_message(message.chat.id, "Извините, я Вас не понял")

bot.infinity_polling()