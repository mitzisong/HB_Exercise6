from sys import argv

"""Write a program, wordcount.py, that opens a file named on the command 
line and counts how many times each space-separated word occurs in that file. 
Your program should then print those"""

#get a file name from the command line
#TODO make this more fault tolerant

script, filename = argv
#print script
#print filename

#open the file
f = open(filename, "r")
#print f
#print type(f)

#read the file to a variable
myfile = f.read()
#print myfile

#close the file
f.close()

#separate file in to words
split_words = myfile.split()
#print split_words

#count the words
#USE A DICTIONARY
#make an empty dictionary 
d = {}

#iterate through split words
for word in split_words:
    #separate words in dict from words not in dict
    if not d.get(word):
        #add it to the dictionary if it's not already there
        #print "This word isn't in the dictionary", word
        d[word] = 1
    else: 
        #increment the word count if it's already in the dict
        d[word] += 1
        #print "This word is in the dictionary", word

# you can also write the for loop this way
# for word in split_words:
#   d[word] = d.get(word, 0) + 1

#print d

#print out the word counts
for key, value in d.iteritems():
    print key, value


































