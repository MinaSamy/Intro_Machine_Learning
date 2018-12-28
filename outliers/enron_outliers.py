#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
import operator
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
#remove the TOTAL outlier point
data_dict.pop("TOTAL",0)

features = ["salary", "bonus"]
data = featureFormat(data_dict, features)

my_data=[]
my_salary_data=[]

### your code below
for point in data:
    salary = point[0]
    bonus = point[1]
    my_data.append(bonus)
    my_salary_data.append(salary)
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

my_data.sort(reverse=True)
my_salary_data.sort(reverse=True)
#should have used index because index 0 contains the TOTAL of values
biggest_bonus=my_data[0]
biggest_salary=my_salary_data[0]
biggest_key=''
#print("Biggest salary for the key ",my_data[0])
#print("Smallest salary for the key ",my_data[len(my_data)-1])
'''
for key in data_dict:
    entry=data_dict[key]
    if entry["salary"]==biggest_salary:
        biggest_key=key
        break
print(biggest_key)
'''

#filter entries with Salary values (non NaN)
sorted_dict={k:v for (k,v) in data_dict.items() if v["salary"]!='NaN'}
sorted_dict=sorted_dict.items()
#Sort descendingly
sorted_dict.sort(key=lambda x:x[1]["salary"],reverse=True)
print(sorted_dict[1])


