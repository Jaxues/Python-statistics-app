# Python-statistics-app
## Introduction
This is a simple CLI-based program written in python 
Its main functionality is to calculate descriptive statistics, linear regression, and create confidence intervals.
This program assumes it is run in a virtual environment with all packages from 'requirements.txt' installed.
It also assumes that data are in the form of .csv files
The initial setup of the program won't include folders for data or output. But once it is run initially it will create these folders.

## Methodology
Since this is a CLI app, I have decided not to include any graphs or visualizations for data. 
This tool is mainly for performing calculations in a relatively fast and easy way, on csv data.         
The reason for this is that statistics can be helpful if they are understood in terms of the data. E.g. a statistic by itself isn't useful in just the mean. But what the context behind what the data is from it explains the mean is the average from the data set"

## Functions of the program
### Data Exploration 
This is the function used to analyze the statistics for one variable. This variable can be either quantitative or categorical and the program will determine what to calculate based on that.

The format of data is assumed to be each row corresponds to one value this is the case for both quantitative and categorical data.

Descriptive statistics for variables
One quanaitative variable
- Sample size
- Mean
- Median
- Standard Deviation
- Lower Quartile
- Upper Quartile
- Maximum
- Minimum

One Categorical variable
- Sample size
- Proportion

### Linear Regression function
Takes two columns for each quantitative variable.
Where one row corresponds to one entry.

The output that is produced will be a summary of whether the relationship is positive or negative between the two variables.
And whether the strength is weak, medium, or strong. 
As well it will give the line of best fit for the data.

Strength is calculated based on the following
- 1 is a perfect correlation between the two variables
- 0.99 to 0.7 is a strong correlation between the two variables
- 0.69 to 0.40 is a moderate correlation between the two variables
- 0.39 to 0 is a weak correlation between two variables 
- 0 is no correlation and no strength

Direction is calculated based on the correlation coefficient is negative, positive, or 0.

### Confidence interval
Takes one column of a single quantitative variable.
Where one row represents one entry of data
Calculates the sample mean and standard deviation and then uses a Scipy confidence interval function to estimate values for a given proportion alpha. 

Values of alpha are given as numbers between 0 and 1, this determines the size of the interval.
The program produces error messages if alpha is 0,1, less than 0, or not a numerical value.

### Save output
This takes statistical output and creates a text file saving all data produced from using a function.
If the user doesn't enter a name for the file, the program will automatically fill it with a timestamp instead
All saved output will be in the output folder. If this folder doesn't already exist the program will create it.


## Future features
As project currently is I think it is functional enough to be a good program.
Currently my plan for this was only to have this as a summer project, so I wasn't able to implement all features that I previously wanted to. Including hypothesis testing , as well as cutting some features for producing confidence intervals for median, standard deviation, and difference in means.
Because those were either out of my current skill level of what I can program or I ran out of time.
Further features I didn't plan but could add would be adding a flask frontend for a more user friendly and approach use of program I have made.
Also if more graphical implementation was made it'd make more sense to produce graphs of output for data.
But this would also add the complexity of databases, user management and then potentially hosting if required.
