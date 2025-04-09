# dice_art = {
#     1: (
#         "┌─────────┐",
#         "│         │",
#         "│    ●    │",
#         "│         │",
#         "└─────────┘"
#     ),
#     2: (
#         "┌─────────┐",
#         "│  ●      │",
#         "│         │",
#         "│      ●  │",
#         "└─────────┘"
#     ),
#     3: (
#         "┌─────────┐",
#         "│  ●      │",
#         "│    ●    │",
#         "│      ●  │",
#         "└─────────┘"
#     ),
#     4: (
#         "┌─────────┐",
#         "│  ●   ●  │",
#         "│         │",
#         "│  ●   ●  │",
#         "└─────────┘"
#     ),
#     5: (
#         "┌─────────┐",
#         "│  ●   ●  │",
#         "│    ●    │",
#         "│  ●   ●  │",
#         "└─────────┘"
#     ),
#     6: (
#         "┌─────────┐",
#         "│  ●   ●  │",
#         "│  ●   ●  │",
#         "│  ●   ●  │",
#         "└─────────┘"
#     ),
# }


# # print(dice_art.get(1))
# noofdice = 3

# for row in range(noofdice):
#     # print(row)
#     for i in dice_art.get(row+1):
#         print(i, end=" ")
#         break;



nums = {
    1: ("ab", "b", "c"),
    2: ("d", "e", "f"),
    3: ("g", "h", "i")
}

noofdice = 2

for row in range(noofdice):  # The length of the tuple in any key (1) will give the row count
    for col in range(1, noofdice + 1):  # Iterating through the columns (keys 1, 2)
        print(nums[col][row], end=" ")  # Print the element at the row-th position in the col-th tuple
    print()
    