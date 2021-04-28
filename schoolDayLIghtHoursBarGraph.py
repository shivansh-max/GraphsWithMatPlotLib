# import matplotlib.pyplot as plt
#
# names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
#          "December"]
# dheli = [10.22, 10.51, 11.35, 12.28, 13.16, 13.51, 13.56, 13.29, 12.43, 11.53, 11.3, 10.28]
# sydney = [14.22, 13.44, 12.49, 11.43, 10.45, 10.3, 9.56, 10.28, 11.23, 12.25, 13.28, 14.14]
#
# plt.plot(names, dheli, label="New Dheli, India", color="k")
# plt.plot(names, sydney, label="Sydney,Australia", color="c")
#
# position = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# position2 = [0.3, 1.3, 2.3, 3.3, 4.3, 5.3, 6.3, 7.3, 8.3, 9.3, 10.3, 11.3, 12.3]
# position3 = [0.99, 1.99, 2.99, 3.99, 4.99, 5.99, 6.99,7.99,8.99,9.99,10.99,11.99,12.99,]
#
# plt.bar(position, sydney, width=0.3, color="black", label="Sydney, Australia")
# plt.bar(position2, dheli, width=0.3, color="c", label="Delhi,India")
#
# plt.xticks(position3, names)
#
# plt.ylabel("Day Light Hours (hour.minutes)")
# plt.xlabel("Months")
# plt.title("Day Light Hours")
# plt.legend()
#
# plt.show()

import matplotlib.pyplot as plt

# figsize
fig = plt.figure(figsize=(5, 7))
names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
         "December"]
dheli = [10.22, 10.51, 11.35, 12.28, 13.16, 13.51, 13.56, 13.29, 12.43, 11.53, 11.3, 10.28]
sydney = [14.22, 13.44, 12.49, 11.43, 10.45, 10.3, 9.56, 10.28, 11.23, 12.25, 13.28, 14.14]
position = [0, 1, 2, 3]
position2 = [0.25, 1.25, 2.25, 3.25]
position3 = [0.99, 1.99, 2.99, 3.99]

plt.bar(position, dheli, width=0.25, color="black", label="MATH")
plt.bar(position2, sydney, width=0.25, color="c", label="READNG")

plt.xticks(position3, names)

plt.ylabel("Test scores")
plt.xlabel("People")
plt.title("TEST SOCRES")
plt.legend()

plt.show()
