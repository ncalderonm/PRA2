# Imports
import pandas as pd
import csv





# Reading dataset

"""with open('Data Titanic\gender_submission.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)"""

gender_submission = pd.read_csv('Data Titanic\gender_submission.csv', header=0)
print(gender_submission.sample(5))