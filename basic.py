import os
import re
from dotenv import load_dotenv

load_dotenv()

questions = str(os.getenv('Question'))
options=str(os.getenv('All_Option'))
option_regex=str(os.getenv('Option'))


f = open("test.txt", "r")
data=f.read()

questions = re.findall(questions,data)
options = re.findall(options,data)

questions_len=len(questions)

for i in range(questions_len):
    print(questions[i])
    option=re.findall(option_regex,options[i])
    for j in option:
        print(j)