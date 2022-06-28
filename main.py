# Смотрин Николай: пишет в файл
def write_in_txt_file():
  with open('text.txt', 'w') as writer:
    writer.write('I love Git')
    return True

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