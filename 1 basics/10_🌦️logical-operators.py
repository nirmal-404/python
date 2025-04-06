#  and 
age = 20
has_ticket = True

if age >= 18 and has_ticket:
    print("You can enter the event.")
else:
    print("You cannot enter the event.")


# or
time_of_day = "evening"
is_weekend = True

if time_of_day == "morning" or is_weekend:
    print("Go for a run.")
else:
    print("Stay inside and relax.")


# not
is_sunny = True

if not is_sunny:
    print("Bring an umbrella!")
else:
    print("Wear sunglasses!")


# combined
is_summer = True
is_holiday = True
is_hot = False

if (is_summer or is_holiday) and not is_hot:
    print("It's a great day for a picnic!")
else:
    print("Maybe stay inside and relax.")
