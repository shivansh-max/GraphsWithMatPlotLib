import matplotlib.pyplot as plt

names = ["SHIVANSH", "ISHA", "ANOUSHA", "PRAKASH"]
math_scores = [99, 100, 77, 89]
reading_scores=[51,100, 45, 61]

plt.scatter(names, math_scores, color="k",label="MATH",marker="*",s=40)
plt.scatter(names, reading_scores, color="c",label="READING",marker="*",s=40)

plt.ylabel("Test scores")
plt.xlabel("People")
plt.title("TEST SOCRES")
plt.legend()

plt.show()