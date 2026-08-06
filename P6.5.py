import matplotlib.pyplot as plt

print("S115 BIJAL TRIPATHI")

categories = ["Data Structures", "Scala for DS",
              "Operating System", "Python for DS"]

scores = [65, 70, 74, 60]

explode = (0, 0, 0, 0.1)

plt.pie(scores,
        labels=categories,
        autopct="%1.1f%%",
        explode=explode,
        startangle=90)

plt.title("Student Scores")

plt.show()
