# Смотрин Николай: пишет в файл
def write_in_txt_file():
  with open('text.txt', 'w') as writer:
    writer.write('I love Git')
    return True

  if __name__ == "__main__":
     if write_in_txt_file():
        print("[OK] write")
        
     print(read_txt_file())
    
    if delete_file():
      print("[OK] delete")
