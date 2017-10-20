
f1 = open("book1.txt")
f2 = open("book2.txt")
f3 = open("book3.txt")

word_list = []

for line1 in f1:

   longest1 = ""
   for word1 in (w for w in line1.split(" ") if len(w) % 2 == 0 and len(w) > len(longest1)):
       longest1 = word1

#print(word1)
word_list.append(word1)
#print(word_list)




for line2 in f2:

   longest2 = ""
   for word2 in (w for w in line2.split(" ") if len(w) % 2 == 0 and len(w) > len(longest2)):
       longest2 = word2

#print(word2)
word_list.append(word2)
#print(word_list)


for line3 in f3:

   longest3 = ""
   for word3 in (w for w in line3.split(" ") if len(w) % 2 == 0 and len(w) > len(longest3)):
       longest3 = word3

#print(word3)
word_list.append(word3)
print(word_list)

#for i in word_list:
#   a =len(i)
#   print(max(a))

print(len(word_list))

#a = len(max(word_list, key=len))
