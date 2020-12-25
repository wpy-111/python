"""
   6行4列
   ****
   ####
   ****
   ####
   ****
   ####
"""
for r in range(6):
    for c in range(4):
        if r % 2 == 0:
            print("*", end=" ")
        else:
            print("#", end=" ")
    print()
