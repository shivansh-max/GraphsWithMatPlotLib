import matplotlib.pyplot as plt

# figsize
fig = plt.figure(figsize = (5,7))
names = ["SHIVANSH", "ISHA", "ANOUSHA", "PRAKASH"]
math_scores = [99, 89, 77, 100]
reading_scores=[51,100, 45, 61]
position = [0,1,2,3]
position2 = [0.3,1.3,2.3,3.3]
position3 = [0.15,1.15, 2.15, 3.15]


plt.bar(position, math_scores, width = 0.3, color = "black", label= "MATH")
plt.bar(position2, reading_scores, width = 0.3, color = "c", label= "READNG")

plt.xticks(position3, names)

plt.ylabel("Test scores")
plt.xlabel("People")
plt.title("TEST SOCRES")
plt.legend()

plt.show()