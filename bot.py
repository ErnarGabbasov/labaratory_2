from aiogram import Bot, Dispatcher, executor, types
import database_student

API_TOKEN = 'TOKEN'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start']) # Начало работы бота
async def cmd_start(message: types.Message):
    await message.answer(f"Здравствуйте, Я - Students Bot. Я сообщу информацию о посещаемости и баллах студента по дисциплине.\n\n"
                         f"Чтобы узнать как пользоваться ботом, введите команду /help.\n"
                         f"Узнать весь список дисциплин можно при помощи команды /list.")

@dp.message_handler(commands=['help']) # Как пользоваться ботом
async def cmd_help(message: types.Message):
    await message.answer(f"Чтобы узнать информацию о студенте, введите сообщение в виде: "
                         f"Фамилия Имя Дисциплина.\n\n"
                         f"Чтобы узнать всю информацию о студенте, введите сообщение в виде: "
                         f"Фамилия Имя Все дисциплины.")

@dp.message_handler(commands=['list']) # Список дисциплин
async def cmd_list(message: types.Message):
    await message.answer(f'1. Основы проффесиональной деятельности\n'
                         f'2. Математика\n'
                         f'3. Программирование\n'
                         f'4. Физическая культура\n'
                         f'5. История\n')

@dp.message_handler()
async def student_info(message: types.Message):
    text = message.text.split()
    if len(text) >= 3:
        student_name = f'{text[0]} {text[1]}' # Вводим фамилию и имя студента
        disciplin = ' '.join(text[2:]) # Вводим дисциплину
        student_info = database_student.find_databaseStudents(student_name, disciplin)
        if student_info != []:
            activity = ''
            for i in student_info:
                activity += f'Дисциплина: \"{i[3]}\"\nПосещаемость: {i[4]}\nБаллы: {i[5]}\n\n'
            await message.answer(f'Информация о студенте \"{student_name}\":\n\n{activity}')
        else:
            await message.answer(f'Не удалось найти данного студента. Проверьте правильность данных.')
    else:
        await message.answer('Прошу прощения, мне не знакома данная команда.\nВоспользуйтесь командой /help.')

def start():
    executor.start_polling(dp, skip_updates=True)

