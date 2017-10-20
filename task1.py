f1 = open("book1.txt")
word_list = []
accu = 0

for line in f1:
word_list.append(line.strip())

for i in range(len(word_list)):
      print(i)

