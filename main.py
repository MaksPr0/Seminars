# Смотрин Николай: пишет в файл
def write_in_txt_file():
  with open('text.txt', 'w') as writer:
    writer.write('I love Git')
    return True

#  Сидоров Станислав: читает с файла
def read_txt_file():
  file = 'file.txt'
  with open(file, 'r', encoding='utf-8') as f:
     data = f.read()
     print(data)
     return data

import os
# Муртазаев Абляким: удаляет файл
def delete_file():
  file_path = 'file.txt'
  try:
    os.remove(file_path)
    return True
  except:
    print("The system cannot find the file specified")
    return False