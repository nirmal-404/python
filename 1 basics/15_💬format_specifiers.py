# format specifiers = {value:flags} format a value based on waht flags are inserted

# .(number)f  -   round to that many decimal places (fixed point)
# :(number)  -  allocate that many spacees
# :03  -  allocate zero pad that many spaces
# :<  -  left justify
# :>  -  right justify
# :^  -  center align
# :+  -  use a plus sign to indicate potive values
# :=  -  place sign to leftmost position
# :   -  insert a space before positive numbers
# :,  -  comma separator

price = 3.14159

                             # 0123456789
print(f"LKR {price:.8f}")    # 3.14159000           8 decimal points
print(f"LKR {price:10f}")    # ··3.141590           spaces 10
print(f"LKR {price:010f}")   # 003.141590           0 padded
print(f"LKR {price:>10}")    # ···3.14159           to right
print(f"LKR {price:<10}")    # 3.14159···           to left
print(f"LKR {price:^10}")    # ·3.14159··           centered
print(f"LKR {price:+}")      # +3.14159             + for poitive ums and - for negative numbers
print(f"LKR {price: }")      # ·3.14159             - for negatives ' ' for positives
print(f"LKR {price:,}")      # ·3.14159             , separated 1234.56 -> 1,234.56

example_val = 12345.4225
print(f"LKR {example_val:+15,.2f}")   # LKR ·····+12,345.42