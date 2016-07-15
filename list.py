from random import shuffle
# Given list1 and list2
list1_shuf = ["civil","avengers","hope"]
list2_shuf = ["dark","force","war","awkens"]
index_shuf = range(len(list1))
shuffle(index_shuf)
for i in index_shuf:
    list1_shuf.append(list1[i])
    list2_shuf.append(list2[i]) 