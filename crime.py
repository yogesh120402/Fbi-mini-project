import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt

colors = ['#105B63', '#FFFAD5','#FFD34E','#DB9E36','#BD4932']

lo_outcomes = pd.read_csv(r'C:\MINI PROJECT\fbi\london-outcomes.csv')
lo_outcomes.head()
lo_outcomes.info()
lo_outcomes.isnull().sum()
lo_outcome_cleaned = lo_outcomes.dropna()

uniques_report = lo_outcomes['Month'].unique()
print(uniques_report)

first_report = uniques_report[0]
last_report  = uniques_report[-1]

print(first_report,last_report)

reported_by_uniques = lo_outcomes['Reported by'].unique()
reported_by_uniques

outcome_types = lo_outcomes['Outcome type'].unique()
outcome_types

plot1 = lo_outcomes.groupby('Month').size().reset_index(name='number of outcomes').set_index('Month')
plot1
plot1.plot(kind="line",figsize=(20,10), linestyle='--', marker='o',color=colors)

plot2 = lo_outcomes.groupby('Outcome type').size().reset_index(name='Number of outcomes').set_index('Outcome type')
plot2 = plot2.sort_values(by='Number of outcomes', ascending=False)

values_of_outcomes = plot2['Number of outcomes'][0]
rest_of_outcomes = sum(plot2['Number of outcomes'][1:])

print('Number of Cases completed ', values_of_outcomes)
print('Number of Cases incompleted', rest_of_outcomes)
print('Cases completed greater or equal than cases incompleted?',rest_of_outcomes >= values_of_outcomes)

plot2.plot(kind="bar",figsize=(20,10),color=colors[3])
plt.show()


