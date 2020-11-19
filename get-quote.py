import random

f = open("quotes.txt")
print()
quotes = f.readlines()
f.close()

last = 13
rnd = random.randint(0, last)

print(quotes[rnd])



