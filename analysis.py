"""This is where all analysis methods wil be kept in a module structure"""

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

def ConfidenceInterval():
    print("This is the confidence interval function. This is currently under work")

def HypothesisTesting():
    print("This is the hypothesis testing function")


