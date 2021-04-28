import matplotlib.pyplot as plt

names = ["SHIVANSH", "ISHA", "ANOUSHA", "PRAKASH"]
math_scores = [99, 100, 77, 89]
reading_scores=[51,100, 45, 61]

plt.plot(names, math_scores, label="MATH", color = "k")
plt.plot(names, reading_scores, label="READING", color="c")

plt.ylabel("Test scores")
plt.xlabel("People")
plt.title("TEST SOCRES")
plt.legend()

plt.show()