
name = "Nirmal Prera"
phone = "075-890-8057"

length = len(name)
print(f"Name length: {length}")

first_occurance=name.find("r")
print(f"first occurance: {first_occurance}")

last_occurance=name.rfind("r")
print(f"last occurance: {last_occurance}")

capitalized = name.capitalize()
print(f"capitalized: {capitalized}")

upper_case = name.upper()
print(f"All caps: {upper_case}")

lower_case = name.lower()
print(f"All caps: {lower_case}")

is_digits = name.isdigit()
print(f"Is digits: {is_digits}")

is_alpha = name.isalpha()
print(f"Is alpha: {is_alpha}")

no_of_dashes = phone.count("-")
print(f"Number of dashes: {no_of_dashes}")

replced_phone_no = phone.replace("-", " ")
print(f"Replaced phone number: {replced_phone_no}")

#prints the descriptions of available string methods
print(help(str))
