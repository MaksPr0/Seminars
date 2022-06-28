# Смотрин Николай: пишет в файл
def write_in_txt_file():
  with open('text.txt', 'w') as writer:
    writer.write('I love Git')
    return True 
