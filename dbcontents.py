import os, sys
import colorama
from sysnsrc import SqLiteContents, title, printparam, printerror
#dbcontents.py contents.db *.nsr  командная строка

if __name__ == '__main__':

    colorama.init()
    title(os.path.split(sys.argv[0])[1], 'Скрипт создает оглавление из НСР файлов')
    if len(sys.argv) < 2:
        printerror('Ошибка', 'Неверный формат вызова')
        printparam(os.path.split(sys.argv[0])[1],
                   r'"путь\к новой\базе.db" "путь_1\к файлам\*.nsr" ... "путь_n\к файлам\*.nsr"')
        exit(1)
    contents = SqLiteContents(dbpath=sys.argv[1])
    # contents.init_db(new_db=True)
    for i in range(2, len(sys.argv)):
        print(sys.argv[i])
        contents.add_files(sys.argv[i])
    contents.create_contents()
