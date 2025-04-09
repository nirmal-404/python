#  *args    = allows you to pass multiple non key arguments
#  **kwargs = allows you to pass multiple keyword arguments
#             * unpacking order
#             1. postional, 2. default, 3. keyword, 4. ARBITARY

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(f"1 + 2 = {add(1, 2)}")
print(f"1 + 2 + 3 = {add(1, 2, 3)}")

print()


def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")
    print()

print_address(street="123 Main St", city="Anytown", state="CA", zip_code="12345")
print_address(street="321 Main St", city="Newtown", state="AC", zip_code="54321", apt="001")


def shipping_info(*args, **kwargs):
    print("---------Shipping Info:---------")
    print("Name : ", end=" ")
    for arg in args:
        print(arg, end=" ")
    print()

    for key, value in kwargs.items():
        if key == "state":
            print(f"{key} : {kwargs.get(key)} (Priority State)")
        else:
            print(f"{key} : {value}")
    print("--------------------------------")

shipping_info("Mr.", "Manusha", "Nirmal", street="123, test st.", apt="002", zip="00112", state="GM")

