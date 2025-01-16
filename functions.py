"""This is where all analysis methods wil be kept in a module structure"""
import os
import pyenvvariables
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
            elif usr_input.lower()=='help':
                help()

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
                    path_to_data=f"{pyenvvariables.data_directory}/{items[int(operateon)-1]}"
                    file=pd.read_csv(path_to_data)
                    categories=list(file.columns)
                    col_var=getcolumnvars(categories)
                    select_data=file[col_var]
                    select_data=select_data.dropna()
                    print(f"Descriptive statistics for {col_var}\n {'='*23}")
                    if pd.api.types.is_numeric_dtype(select_data):
                        description=select_data.describe().to_list()
                        print(f"Sample size: {select_data.size}")
                        print(f"Mean: {round(select_data.mean(),2)}")
                        print(f"Median: {select_data.median()}")
                        print(f"Standard Deviation: {round(select_data.std(),2)}")
                        print(f"Lower quartile:{description[4]}")
                        print(f"Upper Quartile:{description[6]}")
                        print(f"Maximum:{select_data.max()}")
                        print(f"Minimum:{select_data.min()}")
                        return False
                    else:
                        print("Categorical data summary")
                        print(select_data.describe())
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
        for category in colvars:
                            print(f"{n+1} {category}")
                            n+=1
        explantory_index=input("Select column for explantory")
        return colvars[int(explantory_index)-1]



def ConfidenceInterval():
    print("This is the confidence interval function. This is currently under work")

def HypothesisTesting():
    print("This is the hypothesis testing function")

def help():
    print("This is the helper function\n")
    first_call=True
    while True:

        if first_call is True:
            selection=input("What is the area you would like help with. \n 1 Data exploration \n 2 confidenceence interval \n 3 hypothesis testing \n 4 general faq and questions about program\n Please type the number corresponding to your problem else type q or quit to exit: ")
        else:
            selection=input("Please enter the name of the command you would like.\nIf you have forgotten what the commands are you can type 'commands' to get them again: ")
        print(selection)
        if selection=='1':
            first_call=False
            print("This is area of explaining some functionality of data exploration function")
            print("\n Firstly the data exploration function can currently perform analysis on one quantative variable. ")
            print("\n For categorical variables it will assume that is the form column name,column 2")
            print("\n E.g. if there are 1000 rows in csv then if 600 of those rows are for categorical 1, categorical 1 will be variable with most occurences.")
            print("If your data is in a different format to this the current version of this program doesn't currently support that method")

            print("Here is a brief description of the meaning of common descriptive statistics")
            common_measurements=["="*23, 'Mean: Average for data calculated by taking sum divided of data divided by sample size. Mean is affected by outliers and can be less reliable in smaller datasets', 'Standard deviation: Measurement of average spread of data. Standard deviation can be used along with mean to approximate data using a normal distrubtion or other theoritical distrubtions', 'Sample size: Total number of enteries for a dataset', 'Lower Quartile','Upper Quartile','Maximum', 'Minimum','Range' ,'Interquartile range', 'r value']
            for measurement in common_measurements:
                print(f"{measurement} \n")
        elif selection=='2':
            first_call=False
            print("This is area for questions about hypothesis testing function")
        elif selection=='3':
            first_call=False
            print("This is the area explaining functionality and ideas of confidence interval functionality")
        elif selection.lower()=='4':
            print("This is a simple cli based program written in python \n It's main functionality is to calculate descriptive statistics, confidence intervals, as well as perform hypothesis testing.")
            print("This program assume that it is run in a virtual enviorment with all packages from 'requirements.txt' installed.\n It also assumes that data are in the form of .csv files")
            print('\n Since this is a cli app, I have decided to not include any graphs or visualizations for data at this point. This tool is mainly for performing calculations in a relatively fast and easy way, on csv data.')
            print("\n The reason for this is that statistics can be helpful if they are understood in terms of the data. E.g. a statistic by itself isn't useful in just the mean. But what the context behind what the data is from it explains the mean is the average from the data set")
            first_call=False
        elif selection.lower()=='commands':
            first_call=True
        elif selection.lower()=='q' or selection.lower()=='quit':
            print("Help function exited")
            return False
        else:
            print("Please enter a valid command")

