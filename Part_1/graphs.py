import csv
import os.path
import matplotlib.pyplot as plt


# patient data structure to store the dates and scores since this is wall we need for mapping scores
class Patient:
    def __init__(self):
        self.dates = []
        self.scores = []

    def addDate(self, date):
        self.dates.append(date)

    def addScore(self, score):
        self.scores.append(score)

    def getDate(self):
        return self.dates

    def getScore(self):
        return self.scores


# stores tha patient id as a key, leaving the value as a new Patient object when a new patient is found from the file
patients = {}

if os.path.isfile("phq_all_final.csv"):
    # reads and takes all the needed patient data
    with open("phq_all_final.csv") as csvfile:
        read = csv.reader(csvfile)
        data = list(read)
        for i in range(1, len(data)):
            if data[i][1] not in patients:
                patients[data[i][1]] = Patient()
            patients[data[i][1]].addScore(int(data[i][4]))
            patients[data[i][1]].addDate(data[i][0].split("T")[0])

    # runs through all the patients from the csv file and plots their scores over time
    # close the window to see the next patient
    for id_num in patients:
        plt.figure("GAD-7 Results")
        plt.suptitle("GAD-7 Results Over Time Of " + id_num)
        plt.plot(patients[id_num].getDate(), patients[id_num].getScore())
        plt.xlabel("Date")
        plt.xticks(rotation=45)
        plt.ylabel("Score")
        mng = plt.get_current_fig_manager()
        mng.window.state('zoomed')
        plt.show()
