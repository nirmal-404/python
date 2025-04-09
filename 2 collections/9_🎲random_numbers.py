import random

print(help(random))

number = random.randint(1, 6)
print(number)

number_float=random.random() # genarates a number between 0 and 1 
print(number_float)

options = ("rock", "paper", "scissors")
option = random.choice(options)
print(option)

cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A",]
random.shuffle(cards)
print(cards)