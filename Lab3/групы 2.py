import csv
import sys

print("Группа 4")
filename = "4.txt"
text_file = open("4.txt", "r")
reader = csv.reader(text_file, delimiter = "\t")
for str in reader:
    print(str)
text_file.close()

print("Группа 5")
filename = "5.txt"
text_file = open("5.txt", "r")
reader = csv.reader(text_file, delimiter = "\t")
for str in reader:
    print(str)
text_file.close()

print("Группа 6")
filename = "6.txt"
text_file = open("6.txt", "r")
reader = csv.reader(text_file, delimiter = "\t")
for str in reader:
    print(str)
text_file.close()



