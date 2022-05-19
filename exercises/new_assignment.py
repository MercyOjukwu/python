from functools import reduce

users = [
    {"name": "Mercy Chiaki", "age": 19, "tweets": ["I'm happy", "God is good", "I love food", "Hey...I like you"], "Verify": "True"},
    {"name": "Ibrahim Musa", "age": 21, "tweets": ["Today will be great", "Yeses..I did it"], "Verify": "False"},
    {"name": "Isaac John", "age": 45, "tweets": ["I'm in a good mood!", "Help...", "Let's party!"], "Verify": "True"},
    {"name": "flowTomi Jola", "age": 30, "tweets": ["I finished my schooling late", "I studied online", "I love you", "Just meh!"], "Verify": True},
    {"name": "Sarah James", "age": 29, "tweets": ["I'm just happy ", "I am rich!"], "Verify": "False"}

]

print("> User names: ", [user["name"] for user in users])
print()

print("> Verified user younger than 25: ", [user["name"] for user in users if user["age"] < 25 and user["Verify"] == "True"])
print()

max_age = reduce(lambda x, y: x if x["age"] > y["age"] else y, users)
print("> User with maximum age: ", max_age)
print()

min_age = reduce(lambda x, y: x if x["age"] < y["age"] else y, users)
print("> User with minimum age", min_age)
print()

average = sum(user["age"] for user in users) // len(users)
print("> Average user age is: ", average)


# average_age = reduce(lambda x, y: x if x["age"] + y["age"] / len(["age"])else y, users)
# print(">User with average age: ", average_age)
print()

user_with_most_tweets = reduce(lambda x, y: x if x["tweets"] > y["tweets"] else y, users)
print("> User with most tweets: ", user_with_most_tweets)


# verified_users = list(map(lambda x: x for "True" in "Verify" , users))
# print(verified_users)


# just_map = map(lambda y: y["Verify"], filter(lambda x: x["True"], users))
# print(just_map)
#
# average = sum(user["age"] for user in users) / len(users)
# print(">Average user age is: ", average)


# average_age = reduce(lambda x, y: x if x["age"] + y["age"] / len(["age"])else y, users)
# print(">User with average age: ", average_age)
