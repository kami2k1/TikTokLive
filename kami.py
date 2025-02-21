import time


input()
with open('dz.py', 'r',encoding='utf-8') as file:
    content = file.read()

with open('playtext.py', 'w',encoding='utf-8') as output_file:
    for char in content:
        output_file.write(char)
        output_file.flush()  
        time.sleep(0.04) 

input()

import subprocess
subprocess.run(['python', 'tiktok.py'])
