import matplotlib.pyplot as plt

potato_price = [0.74, 0.09,  1.25,  67.92]
cabbage_price = [0.38, 0.27,  1.75,  42.60]
onion_price = [0.63, 0.27,  1.25,  37.96]
tomato_price = [0.69, 0.36,  3.54,  25.48]
ogirok_price = [0.88, 0.27,  3.32, 25.48]
apple_price = [1.00, 0.33,  4.44, 64.23]
year = ["2007","2008","2011", "2017"] 

plt.plot(year,potato_price,label = "Картопля")
plt.plot(year,cabbage_price,label = "капуста")
plt.plot(year,onion_price,label = "Цибуля")
plt.plot(year,tomato_price,label = "Помідори")
plt.plot(year,ogirok_price,label = "Огірки")
plt.plot(year,apple_price,label = "Яблука")
plt.xlabel("Дата")
plt.ylabel("Ціна")
plt.legend()
plt.grid(True)

def showplot():
    plt.show()