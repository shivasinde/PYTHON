# chai_Type = {"Masala" : "spicy" , "Ginger" : "zesty"}
# print(chai_Type)
# print(chai_Type["Ginger"])

# for chai in chai_Type:
#   print(chai)

# for chai in chai_Type.items():
#   print(chai)

# for key , value in chai_Type.items():
#   print(key,value)

# if "Masala" in chai_Type:
#   print("Masala Chai")
# else : 
#   print("Not Masala Chai")

# print(len(chai_Type))

# chai_Type["Green"] = "super"
# print(chai_Type)

# chai_Type.pop("Green")
# print(chai_Type)

# print(chai_Type.popitem())


# chai_Type_copy = chai_Type.copy()
# print(chai_Type_copy)

# chai_Type["Green"] = "Fresh"

# print(chai_Type)
# print(chai_Type_copy)


# chai_shop = {
#   "chai" : {
#     "Masala" : "Fresh",
#     "Green" :  "spicy"
#   }
# }
# print(chai_shop["chai"].get("Masala"))


# squre_num = {x : x ** 2 for x in range(10)}
# print(squre_num.clear())


keys = ["Masala","Lemon"]
values = ["spicy","Fresh"]

new_Dect = dict.fromkeys(keys,values)
print(new_Dect)