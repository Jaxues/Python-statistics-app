"""This is where all analysis methods wil be kept in a module structure"""
import os
import pandas as pd
def escape(usr_input):
    if str(usr_input.lower())=='q':
        return False
    else:
        return True

def selection():
    print("""Please select one of the operations you would like to do, type number for each
          \n 1 Data exploration
          \n 2 Confidence Interval
          \n 3 Hypothesis testing
          \n If you would like help type 'help'
          \n If you would like to leave type 'q' to exit""")
    while True:
        usr_input=input("Command: ")
        if escape(usr_input):
            if usr_input=='1':
                data_exploration()
            elif usr_input=='2':
                ConfidenceInterval()
            elif usr_input=='3':
                HypothesisTesting()
            else:
                print("Please enter a valid input")
        else:
            print("Proccess exited")
            return False
            
def data_exploration():
    print("""Welcome this is the data exploration function""")
    items=os.listdir('data')
    if items:
        n=1
        for item in items:
            if item.endswith(".csv"):
                print(f'{n} {item}')
                n+=1
        while True:
            operateon=input("Enter the number of the file you would like to analyze: ")    
            if operateon.isnumeric():
                if int(operateon) in range(len(items)+1):
                    file=pd.read_csv(f"{os.getcwd()}/data/{items[int(operateon)-1]}")
                    print(file)
                    categories=list(file.columns)
                    print(getcolumnvars(categories))
                    return False
                else:
                    print("Not within range of files")
            elif operateon.lower()=='q':
                return False
            else:
                print("That is not a valid integer please enter another")
    else:
        print("No files in data directory")


def getcolumnvars(colvars):
        n=0
        print(colvars)
        for category in colvars:
                            print(f"{n+1} {category}")
                            n+=1
        explantory_index=input("Select column for explantory")
        return colvars[int(explantory_index)-1]



def ConfidenceInterval():
    print("This is the confidence interval function. This is currently under work")

def HypothesisTesting():
    print("This is the hypothesis testing function")


