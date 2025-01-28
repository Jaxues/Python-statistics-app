"""This is where all analysis methods wil be kept in a module structure"""

import os
import pandas as pd
import datetime
from scipy import stats
from pyenvvariables import output_directory, data_directory


def escape(usr_input):
    if str(usr_input.lower()) == "q":
        return False
    else:
        return True


def print_statouput(stat_output):
    """Prints all statistics in given statoutput"""
    for stat in stat_output:
        print(stat)


def get_filesnames():
    items = os.listdir("data")
    Continue = True
    if items:
        n = 1
        print(items)
        for item in items:
            if item.endswith(".csv"):
                print(f"{n} {item}")
                n += 1
        while Continue is True:
            operateon = input(
                "Enter the number of the file you would like to analyze: "
            )
            if operateon.isnumeric():
                if int(operateon) in range(len(items) + 1):
                    path_to_data = f"{data_directory}/{items[int(operateon)-1]}"
                    file = pd.read_csv(path_to_data)
                    return True, file, list(file.columns)
                else:
                    print("File selected is not in range")
            elif operateon.lower() == "q":
                break
            else:
                print("That is not a valid integer please enter another")

    else:
        print(
            "No files in data directory, please add files before trying to perform functions"
        )


def getcolumnvars(colvars, keyword):
    n = 0
    for category in colvars:
        print(f"{n+1} {category}")
        n += 1
    explantory_index = input(f"Select column for {keyword} ")
    return colvars[int(explantory_index) - 1]


def is_float(number):
    try:
        float(number)
        return True
    except:
        return False


def getalphavalue():
    while True:
        alpha = input("Enter a value for signifance level")
        if alpha.isnumeric() or is_float(alpha):
            if float(alpha) == float(0):
                print("Can't have alpha of Zero. This would reject all findings.")
            elif float(alpha) >= float(1):
                print("Can't have alpha of 1 or more this would accept all values.")
            elif float(alpha) < 0:
                print("Can't have an alpha value of less than zero.")
            else:
                return alpha
        else:
            print("Alpha value has to be numeric")


def save_file(output_list):
    while True:
        save_file = input("Would you like to save file")
        if save_file.lower() in ["y", "yes"]:
            filename = input("Enter a filename else it will autofill with timestamp")
            saved_file = os.path.join(
                output_directory,
            )
            print(saved_file)
            if filename.strip is None:
                file = open(
                    saved_file
                    + f"Data {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}.txt",
                    "x",
                )
            if filename.strip():
                file = open(saved_file + filename, "x")

            file = open(filename, "w")
            for output in output_list:
                file.write(output)

        elif save_file.lower() in ["n", "no"] or not save_file.strip():
            return False


def selection():
    print(
        """Please select one of the operations you would like to do, type number for each
          \n 1 Data exploration
          \n 2 Linear Regression
          \n 3 Confidence Interval
          \n 4 Hypothesis testing
          \n If you would like help type 'help'
          \n If you would like to leave type 'q' to exit"""
    )
    while True:
        usr_input = input("Command: ")
        if escape(usr_input):
            if usr_input == "1":
                data_exploration()
            if usr_input == "2":
                linearregression()
            elif usr_input == "3":
                ConfidenceInterval()
            elif usr_input == "4":
                HypothesisTesting()
            elif usr_input.lower() == "help":
                help()

            else:
                print("Please enter a valid input")
        else:
            print("Proccess exited")
            return False


def data_exploration():
    print("""Welcome this is the data exploration function""")
    items, file, categories = get_filesnames()
    if items:
        col_var = getcolumnvars(categories, "analysis")
        select_data = file[col_var]
        select_data = select_data.dropna()
        stat_output = []
        if select_data.empty:
            print(f"No Data in {col_var}")
        elif pd.api.types.is_numeric_dtype(select_data):
            description = select_data.describe().to_list()
            stat_output = [
                f"Descriptive statistics for {col_var}\n {'='*23}",
                f"Sample size: {select_data.size}",
                f"Mean: {round(select_data.mean(),2)}",
                f"Median: {select_data.median()}",
                f"Standard Deviation: {round(select_data.std(),2)}",
                f"Lower quartile:{description[4]}",
                f"Upper Quartile:{description[6]}",
                f"Maximum:{select_data.max()}",
                f"Minimum:{select_data.min()}",
            ]
        else:
            categorical_description = select_data.value_counts().tolist()
            colum_names = select_data.unique().tolist()
            stat_output = ["Categorical data summary", f"Categories in {col_var}"]
            for column, frequency in zip(colum_names, categorical_description):
                total = f"{column}:{frequency} occurences"
                proportion = f"{column}:{round(frequency/select_data.size,2)} proportion of total"
                stat_output += total, proportion

        print_statouput(stat_output)


def linearregression():
    print("This is the function for linear regression")
    items, file, categories = get_filesnames()
    if items:
        stat_output = []
        explantory_var = getcolumnvars(categories, "explantory")
        response_var = getcolumnvars(categories, "response")
        explantory_val = file[explantory_var]
        response_val = file[response_var]
        if explantory_val.empty or response_val.empty:
            print("One column is empty please select a different column")
        elif (
            pd.api.types.is_numeric_dtype(explantory_val) is False
            or pd.api.types.is_numeric_dtype(response_val) is False
        ):
            print(
                "One column has values that aren't numeric. Can't perform linear regression this data"
            )
        else:
            correlation = explantory_val.corr(response_val)
            print(correlation)
            if correlation == 0:
                stat_output += f"There is no relationship betwen {explantory_var} and {response_var}"
            else:

                if correlation < 0:
                    relationship = "negative"
                elif correlation > 0:
                    relationship = "positive"
                if abs(correlation) == 1:
                    strength = "perfect"
                elif abs(correlation) > 0.69:
                    strength = "strong"
                elif abs(correlation) > 0.39:
                    strength = "moderate"
                else:
                    strength = "weak"
                stat_output += (
                    f"There is a {strength} {relationship} between {explantory_var} and {response_var}",
                    f"Correlation coefficient is {round(correlation,2)}",
                )
                scipy_linregress = stats.linregress(explantory_val, response_val)
                stat_output += (
                    f"The line of best fit for the relationship between {explantory_var} and {response_var} is given by: y={round(scipy_linregress[0],2)}*x+{round(scipy_linregress[1],2)}",
                    f"With standard error of gradient being {round(scipy_linregress[4],2)}",
                )

            print_statouput(stat_output)

def ConfidenceInterval():
    print("This is the confidence interval function. This is currently under work")
    alpha=getalphavalue()
    items, file, categories = get_filesnames()
    print(alpha)
    print(categories)
    print(file)


    


def HypothesisTesting():

    predefined_stats = input(
        "This is the hypothesis testing function \n Press (1) if you have predefined mean and standard deviation for hypothesis testing \n Press (2) if you want to calculate mean and standard deviation"
    )
    alpha = getalphavalue()

    variable = getcolumnvars()

    print(alpha)


def help():
    print("This is the helper function\n")
    first_call = True
    while True:

        if first_call is True:
            selection = input(
                "What is the area you would like help with. \n 1 Data exploration \n 2 confidenceence interval \n 3 hypothesis testing \n 4 general faq and questions about program\n Please type the number corresponding to your problem else type q or quit to exit: "
            )
        else:
            selection = input(
                "Please enter the name of the command you would like.\nIf you have forgotten what the commands are you can type 'commands' to get them again: "
            )
        print(selection)
        if selection == "1":
            first_call = False
            print(
                "This is area of explaining some functionality of data exploration function"
            )
            print(
                "\n Firstly the data exploration function can currently perform analysis on one quantative variable. "
            )
            print(
                "\n For categorical variables it will assume that is the form column name,column 2"
            )
            print(
                "\n E.g. if there are 1000 rows in csv then if 600 of those rows are for categorical 1, categorical 1 will be variable with most occurences."
            )
            print(
                "If your data is in a different format to this the current version of this program doesn't currently support that method"
            )

            print(
                "Here is a brief description of the meaning of common descriptive statistics"
            )
            common_measurements = [
                "=" * 23,
                "Mean: Average for data calculated by taking sum divided of data divided by sample size. Mean is affected by outliers and can be less reliable in smaller datasets",
                "Standard deviation: Measurement of average spread of data. Standard deviation can be used along with mean to approximate data using a normal distrubtion or other theoritical distrubtions",
                "Sample size: Total number of enteries for a dataset",
                "Lower Quartile",
                "Upper Quartile",
                "Maximum",
                "Minimum",
                "Range",
                "Interquartile range",
                "r value",
            ]
            for measurement in common_measurements:
                print(f"{measurement} \n")
        elif selection == "2":
            first_call = False
            print("This is area for questions about hypothesis testing function")
        elif selection == "3":
            first_call = False
            print(
                "This is the area explaining functionality and ideas of confidence interval functionality"
            )
        elif selection.lower() == "4":
            print(
                "This is a simple cli based program written in python \n It's main functionality is to calculate descriptive statistics, confidence intervals, as well as perform hypothesis testing."
            )
            print(
                "This program assume that it is run in a virtual enviorment with all packages from 'requirements.txt' installed.\n It also assumes that data are in the form of .csv files"
            )
            print(
                "\n Since this is a cli app, I have decided to not include any graphs or visualizations for data at this point. This tool is mainly for performing calculations in a relatively fast and easy way, on csv data."
            )
            print(
                "\n The reason for this is that statistics can be helpful if they are understood in terms of the data. E.g. a statistic by itself isn't useful in just the mean. But what the context behind what the data is from it explains the mean is the average from the data set"
            )
            first_call = False
        elif selection.lower() == "commands":
            first_call = True
        elif selection.lower() == "q" or selection.lower() == "quit":
            print("Help function exited")
            return False
        else:
            print("Please enter a valid command")
