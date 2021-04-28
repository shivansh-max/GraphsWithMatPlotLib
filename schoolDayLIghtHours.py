import matplotlib.pyplot as plt

names = ["January", "February", "March", "April", "May", "June", "July", "August", "September","October", "November", "December"]
dheli = [10.22,10.51,11.35,12.28,13.16,13.51,13.56,13.29,12.43,11.53,11.3,10.28]
sydney = [14.22,13.44,12.49,11.43,10.45,10.3,9.56,10.28,11.23,12.25,13.28,14.14]

plt.plot(names, dheli, label="New Dheli, India", color = "k")
plt.plot(names, sydney, label="Sydney,Australia", color="c")

plt.ylabel("Day Light Hours (hour.minutes)")
plt.xlabel("Months")
plt.title("Day Light Hours")
plt.legend()

plt.show()