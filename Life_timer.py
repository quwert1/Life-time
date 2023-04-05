# ТЗ:
# Добавить одну крутую мелодию, при произведении которой в фоне
# ассистент говорил фразу и она играла...



# python "C:\Users\User\Desktop\Фото\Python\РАБОЧИЙ-ТАЙМЕР\Life_timer.py"


import time, datetime, pyttsx3, random, os, threading, sys
from audioplayer import AudioPlayer
from playsound import playsound

os.chdir('/Users/vladislav/Desktop/coding/python/Life-time/Музыка-ТАЙМЕР')

programm_condition = True
s = 1

go_music = ["Ещё музычки? ", "Было славно. Го ещё? ", "РАЗЬЁЁЁЁЁЁБ ПОГНАЛИ ЕЩЁ", "Знатненько навалили. Ещё?", "Фуууух, нормально дало. Ещё разок? "]

def say_speaker(speaker_text):
    print(speaker_text)
    
    engine = pyttsx3.init()

    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-130)

    engine.say(speaker_text)
    engine.runAndWait()

def endSongsSound():
    END_folder = os.path.abspath("/Users/vladislav/Desktop/coding/python/Life-time/Музыка-ТАЙМЕР/конечные песни")
    END_files = os.listdir(END_folder)
    END_file = random.choice(END_files)
    END_oFile = (END_folder + '/' + END_file)

    AudioPlayer(END_oFile).play(block=True)

def notificationSound():
    NOTE_folder = os.path.abspath("//Users/vladislav/Desktop/coding/python/Life-time/Музыка-ТАЙМЕР/звуковые уведомления")
    NOTE_files = os.listdir(NOTE_folder)
    NOTE_file = random.choice(NOTE_files)
    NOTE_oFile = (NOTE_folder + '/' + NOTE_file)

    AudioPlayer(NOTE_oFile).play(block=True)

def end_programm():
    s = 0
    programm_condition = False

    notificationSound()
    say_speaker(random.choice(workEndAnswer))
    print('')
    endSongsSound()

    #say_speaker(' Программа еще не дописана до конца,\nпоэтому извиняюсь, если во время воспроизведения музыки меня кто-то перебил.\nСейчас команда разработчиков усердно трудится, чтобы исправить эту проблему.\nЕсли программа не завершится автоматически, прошу Вас завершить ее вручную. Спасибо за понимание.\nЕсли хотите еще послушать музыку, используйте инструкцию ниже. Обещаю, теперь меня никто не перебьёт, хах.')
    say_speaker(' Рабочий день окончен, но мы можем послушать музыку! \nХотите навалить ещё жесткого музла? Y или n ')
    
    while True:
        print('')
        repeat = input('Программа завершится при введенном значении n: ')

        if repeat.lower() == 'y' or repeat.lower() == 'н':
            endSongsSound()
            say_speaker(random.choice(go_music))
        elif repeat.lower() == 'n' or repeat.lower() == 'т':
            break
        else:
            print('')
            say_speaker('Неверный формат. Допускаются только значения y или n независимо от регистра.')

print(" Добрый день, вас приветствует программа - умный таймер, \nкоторая позволит вам сосредоточиться на учебе при помощи \nкомбинации работа - отдых. \nРекомендуемые циклы: 25 работа, 5 отдых.")
print('')

try:
    work = int(input('Введите желаемое время работы в минутах: '))
    print('')
except:
    print('ВВЕДИТЕ ЦЕЛОЕ ЦИСЛО!')
    print('')
    time.sleep(1)
    work = int(input('Введите желаемое время работы в минутах: '))
    print('')

try:
    chill = int(input('Введите желаемое время отдыха в минутах: '))
    print('')
except:
    print('ВВЕДИТЕ ЦЕЛОЕ ЦИСЛО!')
    print('')
    time.sleep(1)
    chill = int(input('Введите желаемое время отдыха в минутах: '))
    print('')
    
def validateTime(fullWork):    
    if len(fullWork) != 5:
        return 'Неверный формат, попробуйте снова.'
    else:
        if int(fullWork[0: 2]) > 23:
            return 'Неверный формат, попробуйте снова.'
        elif int(fullWork[3: 5]) > 59:
            return 'Неверный формат, попробуйте снова.'
        else:
            return 'ok'

while True:
    now_del = datetime.datetime.now()

    curent_hour_del = now_del.hour
    curent_min_del = now_del.minute

    curent_hour_del = str(curent_hour_del)
    curent_min_del = str(curent_min_del)

    if len(curent_hour_del) == 1:
        curent_hour_del = str(0) + str(curent_hour_del)

    else:
        pass

    if len(curent_min_del) == 1:
        curent_min_del = str(0) + str(curent_min_del)

    fullWork = input('Введите время, в которое планируете закончить, например (' + str(curent_hour_del) + '-' + str(curent_min_del) + '): ')
    print('')

    validate = validateTime(fullWork)

    if validate != 'ok':
        print(validate)

    else:
        print('Все готово. Удачи!')
        print('')
        break

workAnswer = ["Эй, за работу, отдых кончился. Если захочешь еще немного отдохнуть, вспомни про зарплату в 40 тысяч. Ладно, сегодня без негатива. Иди работай.", "Я рада сообщить тебе о том, что отдых. КОНЧИЛСЯ!!!", "АЙ ДОНТ ВОННА ДАЙ КОС МАЙ ЛИТЛ СИСТЕР АР ЛИТТЛ БИЧ. Короче отдых у тебя закончился, иди работай.", "ЭТО ПОШЛАЯ МОЛЛИ И СЕЙЧАС МЫ БУДЕМ ИЗУЧАТЬ. ВАКУОЛИ. ну поняли да, типо молли вакуоли. Ладно, отдых у тебя кончился.", "МОЙ МУЖ ДОЛБИТ МЕНЯ ЧАСАМИ ПОСЛЕ ТОГО, КАК ВЫПИЛ ЭТО ЧУДО-СРЕДСТВО. И. И отдых у тебя кончился ха-ха.", "С новыми силами садять за работу. Не забудь. . . ОТСОСАТЬ БЕГЕМОТУ ХАХАХХАХАХАХХАХА. Отдых закончен хах.", "Отдыхать забавно, но не переотдыхивайся. О, отдых как-раз закончился.", "Да! Отдых закончен! Но ты не расстраивайся, он когда-нибудь начнется! Хах.", "КВЭ бро. Работай иди, иначе не заработаешь 1245213525 тысяч миллионов", "Чувак, тебе сорок пять лет. Пойди и найди работу. Хахахах отдых закончился.", "Строчку за Валю и строчку за Гришку. Вот. На пизде получается шишка. Хахах отдых закончен.", "Отдых закончен, прошу приступить к работе. ... ... А еще я пиво. Нихуя себе.", "СКОЛЬКО ДЕЛО НЕ ГОНИ, ВСЕ РАВНО ТЫ РАЗ ДВА ТРИ. Ебать это я к чему... А, точно, отдых закончен.", "Союз нерушимый республик свободных сплатила на веки великая Русь... Отдых закончен."]
chillAnswer = ["Ты заслужил отдых, джедай. ТОЛЬКО НЕ ГЛОТАЙ НЕ ГЛОТАЙ!!!", "Ура, перемена. Да, действительно маловато эмоций.", "Отдыхай, братишка, я люблю когда волосатые мужики обмазываются маслом.", "Включаю песню моргенштерна пососи. Да ладно, шутка, отдых у тебя.", "Улыбайся улыбайся в невесомости пари и останься. Короче отдыхай пока.", "Пора отдыхать. Афигеть блин.", "Все, поработали и хватит... ну... только на " + str(chill) + " минут.", "Спроси у своей мамы кто её кумир... Отдых начался.", "Я люблю пингвини. Они такие. Такие семейний. Кстати, у тебя начался отдых.", "ААААААА БЛЯТЬ ОГРОМНЫЙ СТРАПОН!!!! А. Показалось. Это кружка. У тебя отдых.", "ОТДЫХ ОТДЫХ ОТДЫХ ПЕЧАЛЬНАЯ ПОРА СРЕДИ КРАСИВЫХ ГОЛУБЕЙ ПРОШУ, УБЕЙ. УБЕЙ. Да, если ты не понял, у тебя отдых", "Я уже говорила, что люблю пингвини? Чтож, я повторюсь. Люблю пингвини. Отдыхай иди.", "БЕГИИИИИ сквозь кошмары и проблемы прямиком в летний двор. Отдыхай.", "Работай усерднее. Только после отдыха. ААААААХАХАХХАХАХАХ Я ПИЗДА Я ПИЗДА Я ПИЗДА. ОТДЫХ БЛЯЯЯТЬ.", "Я поздравляю тебя с очередным отдыхом. Не за что.", "Пора отдыхать!", "ДАДАДАДАДАДАДА ВРЕМЯ ОТДЫХА ГЛУБОКИЙ ОТСОС", "Рада сообщить, что наступило врямя отдыха. Очко."]
workEndAnswer = ["ЕПТВОЮМАТЬ какой же сложный день был. Ладно, слава богу он окончен.", "Рабочий день подошел к концу. Но если хочешь, можем еще потрудиться, улыбающийся смайлик. Да, я пока не научилась использовать смайлики. грустный смайлик.", "У-у-у-у-у да я богатый ушлепок у у меня денег так много. Ладно давай сваливай, день окончен.", "Слушай, ты меня заебал, я тут сижу пизжу как клоун ебаный попугай блять. Все иди нахуй отсюда, рабочий день окончен.", "Рабочий день полностью окончен! Ура! ААААЙ ХЭД НОУН БАЙ МАЙ САЙДС СТИЛ ФАКИН ХАД НО ВАН. Да ладно-ладно, врубаю музыку.", "День окончен. Гаааснет свет. И многоточий. Боольше нет. ... ... ... ХХАХАХАХАХХ НАЕБАЛА ВОТ ОНИ ТОЛЬКО ЧТО БЫЛИ. ХАХАХ. Ах.... Ладно, до встречи", "ДИДЖЕЙ ПЛЮЮЮЮС ок погнали, день окончен!!!!"]

work = work * 60
chill = chill * 60

fullWorkHour = int(fullWork[0: 2])
fullWorkMin = int(fullWork[3: 5])

now2 = datetime.datetime.now()

curent_hour2 = now2.hour
curent_min2 = now2.minute

if int(fullWorkHour) < int(curent_hour2):
    fullWorkHour += 24
    timer_hour = int(fullWorkHour) - int(curent_hour2)

elif int(fullWorkHour) > int(curent_hour2):
    timer_hour = int(fullWorkHour) - int(curent_hour2)

elif int(fullWorkHour) == int(curent_hour2):
    if int(curent_min2) > int(fullWorkMin):
        timer_hour = 24
    elif int(curent_min2) <= int(fullWorkMin):
        timer_hour = 0 

if int(fullWorkMin) > int(curent_min2):
    timer_min = int(fullWorkMin) - int(curent_min2)

elif int(fullWorkMin) < int(curent_min2):
    difference_min = 60 - int(curent_min2)
    timer_min = int(difference_min) + int(fullWorkMin)
    timer_hour -= 1
elif int(fullWorkMin) == int(curent_min2):
    timer_min = 0

print('До срабатывания таймера осталось: ' + str(timer_hour) + ' часов ' + str(timer_min) + ' минут. ')
print('')

notificationSound()
say_speaker('Работа началась.')
print('')

general_hour = int(timer_hour) * 3600
general_min = int(timer_min) * 60

general_work_time = int(general_hour) + int(general_min)

timer = threading.Timer(general_work_time, end_programm)
timer.start()

while general_work_time != 0:
    now = datetime.datetime.now()

    curent_hour = now.hour
    curent_min = now.minute

    for i in range(0, work):
        if general_work_time == 0:
            break

        time.sleep(1)
        general_work_time -= 1

    if general_work_time == 0:
        break

    notificationSound()
    say_speaker(random.choice(chillAnswer))
    print('')

    for i in range(0, chill):
        if general_work_time == 0:
            break

        time.sleep(1)
        general_work_time -= 1

    if general_work_time == 0:
        break

    notificationSound()
    say_speaker(random.choice(workAnswer))
    print('')





# #______________________________________________________________


# import time, datetime, pyttsx3, random, os, threading, sys, keyboard
# from audioplayer import AudioPlayer
# from playsound import playsound

# # def endSongsSound():
# #     END_folder = "C:\\Users\\User\\Desktop\\Фото\\Python\\РАБОЧИЙ-ТАЙМЕР\\конечные песни"
# #     END_files = os.listdir(END_folder)
# #     END_file = random.choice(END_files)
# #     END_oFile = ("C:\\Users\\User\\Desktop\\Фото\\Python\\РАБОЧИЙ-ТАЙМЕР\\конечные песни\\" + END_file)
   
# #     print(END_folder)
# #     print(END_files)
# #     print(END_file)
# #     print(END_oFile)
# #    # AudioPlayer(END_oFile).play(block=True)

# # def notificationSound():
# #     NOTE_folder = "C:\\Users\\User\\Desktop\\Фото\\Python\\РАБОЧИЙ-ТАЙМЕР\\звуковые уведомления"
# #     NOTE_files = os.listdir(NOTE_folder)
# #     NOTE_file = random.choice(NOTE_files)

# #     NOTE_oFile = ("C:\\Users\\User\\Desktop\\Фото\\Python\\РАБОЧИЙ-ТАЙМЕР\\звуковые уведомления\\" + NOTE_file)

# #     print(NOTE_folder)
# #     print(NOTE_files)
# #     print(NOTE_file)
# #     print(NOTE_oFile)
# #    # AudioPlayer(NOTE_oFile).play(block=True)



# def endSongsSound():
#     END_folder = os.path.abspath("Музыка-ТАЙМЕР\\конечные песни")
#     END_files = os.listdir(END_folder)
#     END_file = random.choice(END_files)
#     END_oFile = (END_folder + '\\' + END_file)

#     AudioPlayer(END_oFile).play(block=True)

# def notificationSound():
#     NOTE_folder = os.path.abspath("Музыка-ТАЙМЕР\\звуковые уведомления")
#     NOTE_files = os.listdir(NOTE_folder)
#     NOTE_file = random.choice(NOTE_files)
#     NOTE_oFile = (NOTE_folder + '\\' + NOTE_file)

#     AudioPlayer(NOTE_oFile).play(block=True)

# endSongsSound()
# notificationSound()
