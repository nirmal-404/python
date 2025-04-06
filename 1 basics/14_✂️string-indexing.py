# indexing - accesing els of a sequence using [] (indexing operator)
#            [start : end : step] 

credit_number="1234-5678-9012-3456"

print(credit_number[0]) # 1
print(credit_number[:4]) # 1234
print(credit_number[5:9]) # 5678
print(credit_number[5:]) # 5678-9012-3456
print(credit_number[-1]) # 6
print(credit_number[::2]) # 13-6891-46 (every second character)
print(credit_number[::3]) # 146-136 (every third character)

last_4_digits=credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_4_digits}")

reversed_credit_number = credit_number[::-1]
print(reversed_credit_number) # 6543-2109-8765-4321