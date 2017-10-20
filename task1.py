f1 = open("book1.txt")
#word_list = []
#accu = 0

#for line in f1:
#    word_list.append(line.strip())

#for i in range(len(word_list)):
#       print(i)

for line in f1:

   longest = ""
   for word in (w for w in line.split(" ") if len(w) % 2 == 0 and len(w) > len(longest)):
       longest = word






