from prettytable import PrettyTable

from data import dt

x = PrettyTable()
x.field_names = ["Ринок","Товар","Од.в.","2007"," 2008 рік/грн","у % до 2007","2011 рік/грн","у % до 2008","2017 рік/грн","у % до 2011"]

for i in range(0, len(dt)):
    x.add_rows(
        [
            dt[i]
        ]
    )

def openTabble():
    print('\nАНАЛИЗ ЗМІНИ ЦІН')
    print(x)