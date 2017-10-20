
f1 = open("book1.txt")
f2 = open("book2.txt")
f3 = open("book3.txt")

word_list = []

for line1 in f1:

   longest1 = ""
   for word1 in (w for w in line1.split(" ") if len(w) % 2 == 0 and len(w) > len(longest1)):
       longest1 = word1

print(word1)
word_list.append(word1)
#print(word_list)




#for line2 in f2:

#   longest = ""
#   for word in (w for w in line.split(" ") if len(w) % 2 == 0 and len(w) > len(longest)):
#       longest = word

#print(word)


#for line in f1:

#   longest = ""
#   for word in (w for w in line.split(" ") if len(w) % 2 == 0 and len(w) > len(longest)):
#       longest = word

#print(word)
