data = {}
def xxx():
    data[name] = price
    # print(data)
repeat = True
while repeat:
    name = input("what is your name: ")
    price = int(input("what is the bid price: "))
    xxx()
    a = input("if their any other user who want to bid: ")
    # num=0
    if a == "yes":
        print('\n'*100)
        xxx()
    else:
        print('\n'*100)
        repeat = False
        num = 0
        for key in data:
            if data[key] > num:
                num = data[key]
        print(f"The winner is {key} with the bid amount of {num}.")
   







































# cities = {
#     "kakinada": "kotta kajja",
#     "vizag" : "city of love",
# }


# classes = {
#     "first class":["mythreyi","rakesh","amulya"],
#     "second class" :["vignesh","ram","abhilash","sumanth"]
# }

# nested_list = ["A","B",["C","D"]]
# print(nested_list[2][0])

# # print(classes["first class"][1])



# travel_log = {
#   "France": {
#     "cities_visited": ["Paris", "Lille", "Dijon"],
#     "total_visits": 12
#    },
#   "Germany": {
#     "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#     "total_visits": 5
#    },
# }

# print(travel_log["Germany"]["cities_visited"][2])


# print(art.logo)
