superheroes = ["Ironman", "Captian America", "Thor", "Hulk"]

print(type(superheroes))

print(superheroes)
print(superheroes[0])
print(superheroes[1])
print(superheroes[2])
print(superheroes[1:3])

print(superheroes.index("Hulk"))

# for(i=0; i<len(superheroes); i++){
#     print(superheroes[i])
# }
# cap = ["Captain America", 9]
# print(cap[1])
# for elem in superheroes:    # elem is a temporary variable, each value inside upserheros is accessed one by one
#     print(elem)

rating = ["Ironmman", 10, "Captain America", 9, "Thor", 8, "Hulk", 7]
ratingList = [
    ["Ironman", 10], 
    ["Captain America", 9], 
    ["Thor", 8], ["Hulk", 7]
    ]

print(ratingList[0][0])
print(ratingList[0][1])
print(ratingList[1][0])
print(ratingList[1][1])
print(ratingList[2][0])
print(ratingList[2][1])
print(ratingList[3][0])
print(ratingList[3][1])

"""
  [ ["Ironnman"          10]
    ["Captain America"   9]
    ["Thor"              8]
    ["Hulk"              7] ]
"""

print(superheroes)
print(rating)
print(ratingList)
print("Captain america list: ", ratingList[1][1])

"""a =
    1   2 
    3   4
    4   6
    7   9
"""

################################################################

superheroes = ("Ironman", "Thor", "Spiderman")

dc_heros = ["batman", "Wonder Woman", "Superman", "Flash"]

print(superheroes[0])
print(superheroes[1])
print(superheroes[2])

print(dc_heros[2])
dc_heros[2] = "Ironman"

print(dc_heros)

superheroes[1] = "Flash"
print(superheroes)





