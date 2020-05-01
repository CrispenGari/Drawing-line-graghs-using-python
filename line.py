import os
print(os.getcwd()) # this line of code will help you to get the
# working directory so that you can install the modules using
# cmd width administrator privilage by running the command
# cd [paste the output of print(os.getcwd())] after that command runn
# python -m pip install matplotlib
'''
DRAWING A LINE GRAPH OF THE FOLLOWING DATA USING PYTHON 2 OR PYTHON 3
'''
"""
    +------+----+---+---+---+---+---+---+---+---+---+--+
    |AGE   |20  |21 |22 |23 |24 |25 |26 |27 |28 |29 |30|
    +------+----+---+---+---+---+---+---+---+---+---+--+
    |WEIGHT|78  |80 |86 |90 |100|110|119|119|150|68 |58|
    +------+----+---+---+---+---+---+---+---+---+---+--+
"""

# you can use the followinng code to install modules:

#from pip._internal import main as install
#install(["install","matplotlib"])

import matplotlib.pyplot as plot

age = [20 ,21 ,22 ,23 ,24 ,25 ,26 ,27 ,28 ,29 ,30]
weight =[78 ,80 ,86 ,90 ,100,110,119,119,150,68 ,58]

plot.plot(age,weight, color='red')
plot.xlabel("THE AGE OF STUDENTS")
plot.ylabel("THE WEIGHT OF STUDENTS")
plot.title("THE RELATIONSHIP BETWEEN AGE AND WEIGHT OF UNIVERSITY STUDENTS")
plot.show()