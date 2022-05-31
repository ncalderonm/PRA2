# Imports
import pandas as pd
import csv





# Reading dataset

gender_submission = pd.read_csv('Data Titanic\gender_submission.csv', header=0)
print(gender_submission.sample(5))

test_df = pd.read_csv('Data Titanic\test.csv', header=0)
print(test_df.sample(5))

train_df = pd.read_csv('Data Titanic\train.csv', header=0)
print(train_df.sample(5))