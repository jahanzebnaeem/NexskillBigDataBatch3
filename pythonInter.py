# thislist = ["apple", "banana", "cherry"]
# thistuple = ("kiwi", "orange")
# thislist.extend(thistuple)
# print(thislist)
# print(thislist[4])

# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.pop(1)
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# # for x in thislist:  # 0 = apple, 1 = banana, 2 = cherry
# # print(x)
# # for i in range(len(thislist)):
# # print(thislist[i])
# i = 0
# while i < len(thislist):
#     print(thislist[i])
#     i = i + 1

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# # newlist = []

# # for x in fruits:
# #     if "a" in x:
# #         newlist.append(x)

# newlist = [x for x in fruits if "a" in x]

# print(newlist)

# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort(reverse=True)
# print(thislist)

# def myfunc(n):
#     return abs(n - 50)


# thislist = [100, 50, 65, 82, 23]
# thislist.sort(key=myfunc)
# print(thislist)

# # note the double round-brackets
# thistuple = tuple(("apple", "banana", "cherry", "cherry"))
# print(thistuple)

# thisset = {"apple", "banana", "cherry"}
# print(thisset)

# thisset = {"apple", "banana", "cherry", "apple"}
# print(len(thisset))

# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# print(thisdict["year"])

thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}
# print(thisdict)
print(thisdict.get("colors"[1]))
