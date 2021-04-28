import matplotlib.pyplot as plt

names = ["SHIVANSH", "ISHA", "ANOUSHA", "PRAKASH"]
math_scores = [99, 100, 77, 89]
reading_scores=[51,100, 45, 61]

plt.stackplot(names,math_scores,reading_scores,colors=['k','c'],labels=['MATH','READING'])

plt.ylabel("Test scores")
plt.xlabel("People")
plt.title("TEST SOCRES")
plt.legend()

plt.show()