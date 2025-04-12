
# 0 -> ZeroDivisionError
# asd -> ValueError

try:
    number = int(input("Enter a number: "))
    print(1 /number)
except ZeroDivisionError:
    print("You cant divide by 0 IDIOT !")

except ValueError:
    print("Enter only numbers please")

finally:
    print("Do some cleanup here")