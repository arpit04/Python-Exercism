import random
from string import ascii_uppercase

a = random.sample(set(ascii_uppercase),2)
b = ""
name = b.join(a)

c = random.sample(set('0123456789'),3)
d = ""
digit = d.join(c)

robot_name = name+digit
print(robot_name)