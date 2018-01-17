import os
import psutil
import sys
import shutil

print ('Привет, программист')
name = input ('Введите Ваше имя: ')
print (name, ', добро пожаловать в мир Python!')

answer = ''
while answer != 'q':
    answer = input('Давайте поработаем: Y/N/q? ')
    if answer == 'Y':
        print ('Отлично, хозяин!')
        print ('Я умею: ')
        print ('[1] - выведу список файлов')
        print ('[2] - выведу информацию о системе')
        print ('[3] - выведу список процессов')
        print ('[4] - продублирую файлы в текущей директории')
        print ('[5] - продублирую выбранный файл')
        print ('[6] - удалю файл в выбранной директории')


        
        do = int(input('Укажите номер действия: '))
        if do == 1:
            print (os.listdir())
        elif do == 2:
            print ('Вот что я знаю о системе: ')
            print ('Количество процессоров: ', os.cpu_count())
            print ('Платформа: ', sys.platform)
            print ('Кодировка файловой системы: ', sys.getfilesystemencoding())
            print ('Текущая директория: ', os.getcwd())
            print ('Текущий пользователь: ', os.getlogin())
            
        elif do == 3:
            print (psutil.pids())
        elif do == 4:
            print ('Дублирование файлов в текущей директории -')
            file_list = os.listdir()
            i = 0
            while i < len(file_list):
                newfile = file_list[i] + '.dupl'
                shutil.copy (file_list[i], newfile)
                i += 1
                
        else:
            pass
    elif answer == 'N':
        print ('До свидания!')
    else:
        print ('Неизвестный ответ')
        
   
             
             
    

