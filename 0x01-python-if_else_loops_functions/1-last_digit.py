#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastigit = abs(number) % 10
if lastdigit < 0:
    lastdigit = -(lastdigit)
thestring = "lastdit of {} is {}".format(number,lastdigit)
if lastdigit > 5:
    print(f"{thestring} is greater than 5")
elif lastdigit == 0:
    print(f"{the string} is 0")
elif lastdigit < 6:
    print(f"{thestring} and is less than 6 and not 0")
