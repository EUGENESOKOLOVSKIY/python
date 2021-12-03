import numpy as np
import matplotlib.pyplot as plt

test = "quatre jutges dun jutjat mengen fetge dun penjat"
def create_dictionary2(txt):
    dictionary = {}
    i=0
    for x in set(txt):
        dictionary[x] = txt.count(x)/len(txt)
    return dictionary
   

test_dict = create_dictionary2(test)
plt.bar(test_dict.keys(), test_dict.values(), width=0.5, color='g')
plt.xlabel('Символ')
plt.ylabel('частота')
plt.title('Частота символів')
plt.savefig('Histogram_Lab#7_task2.png', bbox_inches ='tight' )
plt.show()