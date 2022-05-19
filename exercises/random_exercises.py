universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]


def enrollment_stats(x):
    for names in x:
        return x[0:]


import random
# print(enrollment_stats(universities))

Nouns = ["fossil", "horse", "aardvark", "judge", "chef", "mango",
         "extrovert", "gorilla"]
Verbs = ["kicks",
         "jingles",
         "bounces",
         "slurps",
         "meows",
         "explodes", "curdles"]
Adjectives = ["furry",
              "balding",
              "incredulous",
              "fragrant",
              "exuberant", "glistening"]
Prepositions = ["against",
                "after",
                "into",
                "beneath",
                "upon",
                "for", "in", "like", "over", "within"]
Adverbs = ["curiously",
           "extravagantly",
           "tantalizingly",
           "furiously", "sensuously"]
random_element = random.choice(["a", Adjectives, Nouns])

# {A/An}{ Adjectives1} {noun1}
# {A/An} {adj1} {noun1} {verb1} {prep1} the {adj2} {noun2}
# {adverb1}, the {noun1} {verb2}
# the {noun2} {verb3} {prep2} a {adj3} {noun3}

# print(random.choice([ Adjectives and Nouns]))

key_value_pairs = ( ("California", "Sacramento"), ("New York", "Albany"))

print(dict(key_value_pairs))







