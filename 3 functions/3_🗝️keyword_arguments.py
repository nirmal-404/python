#  arguments proceeded by an identifier
#  helps with readability
#  order of arguments does not matter
#  1. positional, 2. default, 3. KEYWORD, 4. Arbitary

def greet(message, title, fname, lname):
    print(f"{message} {title}. {fname} {lname} 😊")

greet("Good Morning", title="Mr", lname="Perera", fname="Nirmal")


def get_phone(country, area, first, last):
    return f"+{country}-{area}-{first}-{last}"

phone_num=get_phone(94, 75, 890, 8057)
print(phone_num)