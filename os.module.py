import os
import time

directory = '.'
for root,dirs,files in os.walk(directory):
    for file in files:
        filepatch = os.path.join(root,file)
        filetime = os.path.getmtime(filepatch)
        time_nev = time.strftime('%d.%m.%Y.%H:%M',time.localtime(filetime))
        filesize = os.path.getsize(filepatch)
        parent_dir = os.path.dirname(filepatch)

print(f'Обнаружен файл:{file},Путь:{filepatch},Размер:{filesize} байт,Время изменения:{time_nev},'
      f'Родительская директория:{parent_dir}')

