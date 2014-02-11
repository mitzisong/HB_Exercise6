text = """
As I was going to St. Ives
I met a man with seven wives
Every wife had seven sacks
Every sack had seven cats
Every cat had seven kits
Kits, cats, sacks, wives.
How many were going to St. Ives?
"""


#opens the file in test.txt
f = open('twain.txt', 'r')

#make all the letters lowercase
text = f.read()
text = text.lower()
tokens = text.split()
text_dict = {}

#count how many times a word occurs

for token in tokens:
    if text_dict.get(token):
        text_dict[token] += 1
    else:
        text_dict[token] = 1

print text_dict

for key, value in text_dict.iteritems():
    print key, value

    

#print word

