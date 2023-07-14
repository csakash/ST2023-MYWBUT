# let's consider a string "HUNTER"

value1 = "UMBRELLA"
# value2 = 'Hunter'

# we want to access the letter 'H'
"""
H   U   N   T   E   R
0   1   2   3   4   5

"""

print(value1)
print(value1[0])    # 0th index of the variable value1
print(value1[4])


print(value1.index("A")) # 

print(len(value1))


# Print the 4th index of the word "Umbrella"
print("4th index of the word: ", value1[4])
print("4th character of the word: ", value1[3])


################################################################

# Slicing of a string

hero = "Ironman"

# I want to extract "ron" from "Ironman"
print(hero[1:4])

# I want to extract all the characters after "n"
print(hero[3:len(hero)])
print(hero[3:])

# I want to extract all the character upto "n"
print(hero[:4])