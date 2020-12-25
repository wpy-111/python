"""
   外层4行   内层
    *      1
    **     2
    ***    3
    ****   4
"""
for r in range(4):
    for c in range(r+1):
        print("*",end="")
    print()