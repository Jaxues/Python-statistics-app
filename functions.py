"""This is where all analysis methods wil be kept in a module structure"""

import os
from numpy._core import numeric
import pandas as pd
import datetime
import numpy as np
from pandas.core.computation.ops import isnumeric
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
                return float(alpha)
        else:
            print("Alpha value has to be numeric")


def save_file(output_list):
    while True:
        save_file = input("Would you like to save file: ")
        if save_file.lower() in ["y", "yes"]:
            filename = input("Enter a filename else it will autofill with timestamp: ")
            saved_file = os.path.join(
                output_directory,
            )
            if not filename or filename.isspace():
                filename = f"{saved_file}/{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}.txt"
            else:
                filename = f"{saved_file}/{filename}.txt"
            file = open(filename, "w")
            for output in output_list:
                file.write(output)
                file.write("\n")
            return

        elif save_file.lower() in ["n", "no"] or not save_file.strip():
            return
        else:
            print("Please enter either yes or no")


def selection():
    print(
        """Please select one of the operations you would like to do, type number for each
          \n 1 Data exploration
          \n 2 Linear Regression
          \n 3 Confidence Interval
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
            return
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
        save_file(stat_output)
        return


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
            save_file(stat_output)


def confidence_interval_mean(data,alpha):
    sample_mean=np.mean(data)
    standard_error=stats.sem(data)
    degrees_freedom=len(data)-1
    if len(data)<=30:
        print("Less than 30 samples will use t test distrubtion")
        return stats.t.interval(confidence=alpha,df=degrees_freedom,loc=sample_mean,scale=standard_error)
    else:
        print("More than 30 samples will use normal distrubtion")
        return stats.norm.interval(alpha,sample_mean,standard_error)

def ConfidenceInterval():
    print("This is the confidence interval function. This is will calculate a confidence interval for the mean based on input given")
    alpha = getalphavalue()
    items, file, categories = get_filesnames()
    if items:
        col_var = getcolumnvars(categories, "analysis")
        select_data = file[col_var]
        select_data = select_data.dropna()
        stat_output = []
        if pd.api.types.is_numeric_dtype(select_data):
            print("Select option to calculate interval for:")
            statistic=""
            lower_bound,upper_bound=confidence_interval_mean(select_data.to_list(),alpha)
            stat_output.append(f"{alpha*100}% confidence interval of {col_var} for {statistic} is between {lower_bound:.4f} and {upper_bound:.4f}")
            print_statouput(stat_output)
            save_file(stat_output)
        else:
            print("Data is not numerical can't create confidence interval")

