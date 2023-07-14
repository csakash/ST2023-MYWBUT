# for loop
# while loop

"""
    arr = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

    for(i=0; i<arr.length; i++){
        printf("%d", arr[i])
    }
"""

arr = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

for i in range(0, len(arr)):
    print(arr[i])


for x in arr:
    # 1st iteration: x=4
    # 2nd iteration: x=5
    # 3rd iteration: x=6
    print(x)

teams = {
    "Team Ironman": [
        {"Spiderman": 8},
        {"Black Widow": 7.5},
        {"War Machine": 7}
    ],
    "Team Captain America": [
        {"Hawkeye": 6},
        {"Groot": 6.5},
        {"Antman": 7}
    ]
}

keys = teams.keys()
print(keys, type(keys))

keys_list = list(keys)
print(keys_list, type(keys_list))

# x = {"test": 1}
# print(x["test"])


# for key in keys_list:
#     print(key, teams[key])


"""
while (condition){
    write your logic here
    increment
}
"""

i = 0

print(len(keys_list))
while i < len(keys_list):
    print(i)
    print(keys_list[i])
    print(teams[keys_list[i]])
    print(teams[keys_list[i]][1])
    i = i+1

