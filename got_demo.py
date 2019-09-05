from pprint import pprint
from characters import characters

#a character count
a_characters = []

for character in characters:
    if character['name'][0] == 'A':
        a_characters.append(character['name'])
num_of_a_characters = len(a_characters)
print("There are %s characters that start with A." %num_of_a_characters)

#z character count
z_characters = []
for character in characters:
    if character['name'][0] == 'Z':
        z_characters.append(character['name'])

num_of_z_characters = len(z_characters)
print("There are %s characters that start with Z." %num_of_z_characters)

#how many are dead

dead_characters = 0
living_characters = 0
for character in characters:
    if character["died"] == "":
        living_characters += 1
    else:
        dead_characters += 1

print("%s characters are still living. %s characters are dead." % (living_characters, dead_characters))


#who has the most titles
#num_of_titles = len(characters[285]["titles"])

i = 0
n = 1
most_titles = []
for character in characters:
    if len(characters[i]["titles"]) > n:
        n = len(characters[i]["titles"])
        most_titles.append(characters[i]["name"])
        mostest = ''.join(most_titles)
    i += 1
print("%s has %s titles" % (mostest, n))

#how many are valyrian

valyrians = 0
n = 0
for character in characters:
    if characters[n]["culture"] == "Valyrian":
        valyrians += 1
    n += 1
print("%s characters are Valyrian." % (valyrians))

#who plays hot pie
i = 0
for char in characters:
    if characters[i]["name"] == "Hot Pie":
        hot_pie_actor = (characters[i]["playedBy"])
    i += 1
print("Hot Pie is played by a character names %s." % (hot_pie_actor))

#how many in the tv series
num_on_tv = 0
num_not_on_tv = 0
i = 0
for character in characters:
    if len(characters[i]["tvSeries"]) > 1:
        num_on_tv += 1
    else:
        num_not_on_tv += 1
    i += 1

num_of_characters = len(characters)
print("Total characters: %s" % num_of_characters)
print("Characters on TV: %s" % num_on_tv) 
print("Characters NOT on TV: %s" % num_not_on_tv)

#who has last name targaryen
i = 0
targaryens = []
for character in characters:
    if "Targaryen" in characters[i]["name"]:
        targaryens.append(characters[i]["name"])
    i += 1
print("A list of Targaryens: " + str(targaryens))

#house histogram
from houses import houses


print(houses["region"])



#print(house_list)

# # print out the key names individually
# for k in jon_snow:
#    print(k)

# # print out just the values
# for key in jon_snow:
#    print(jon_snow[key])

# # print both the key and the value
# for k in characters.jon_snow:
#    print("%s: %s" % (k, jon_snow[k]))