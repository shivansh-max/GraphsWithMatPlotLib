import matplotlib.pyplot as plt

names = ["SHIVANSH", "ISHA", "ANOUSHA", "PRAKASH"]

FINAL_SCORES = [80,95,68,85]

plt.pie(FINAL_SCORES,
        labels=names,
        colors=["c","b","pink","g"],
        explode=(0.1,0,0,0),
        autopct='%1.1f%%')

plt.title("FINAL TEST SOCRES")

plt.show()