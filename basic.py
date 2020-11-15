import re
from .regex import Question_And_Options

f = open("test.txt", "r")
data=f.read()


r = regex.findall(data,Question_And_Options)

for i in r:
    print(i)