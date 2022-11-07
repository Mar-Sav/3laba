import re
file = open('file.html')
line= file.readline()
while line:
  line = file.readline()
  #if bool( re.search(r'(\w+@\w+\.\w+)', line)):#1,7
  #if bool(re.search(r'(([a-zA-Z0-9._+-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9._-]+))', line)):#выводит 1,3,7
  #if bool( re.search(r'([A-Z|a-z]+\w+@\w+\.\w+)', line)):#1,7
  #if bool( re.search(r'\w+[\\.\w-]*@[-a-z0-9]+\.[a-z]+', line)):#выводит 1,3,7
  if bool( re.search(r'[A-Za-z0-9]+\w+@\w+\.[a-z]', line)):
    email=line.split()
    print(*email)
file.close()