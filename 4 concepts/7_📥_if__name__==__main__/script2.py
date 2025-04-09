
from script1 import *

def favourite_drink(drink):
    print(f"Your favourite drink is {drink}")

def main():
    print("This is script 2")
    favourite_food("sushi")
    favourite_drink("coffee")
    print("Good - Bye")

if __name__ == '__main__':
    main()