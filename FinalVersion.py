"""
Created on Nov 02 18:27:52 2018
Project: Plotting a best fit line through a set of points.

This is a program which aims to plot a best-fit fit line through a scatter plot. The user may input
the co-ordinate points either a .csv file or may enter them manually one at a time. An example
result has been provided as well, on the Swedish Auto Insurance Dataset.

Developers: Ashish Shenoy, Rishith Bhowmick, Anantha Krishna
"""

# Importing libraries and functions
import pandas as pd
import matplotlib.pyplot as plt

# Initialising the graph variables
X, Y = [], []
xlabel = ""
ylabel = ""
title = ""
check = True

# A function to calculate 'm' in the equation y = mx + c using the deviation formula.
def calc_m (X, Y):
    global check
    sumX = sum(X)
    sumY = sum(Y)
    sumX2 = sum(i**2 for i in X)
    XY = zip(X, Y)
    sumXY = sum([x*y for x, y in XY])
    n = len(X)
    num = (sumX * sumY) - (n * sumXY)
    den = (sumX)**2 - (n * sumX2)
    try:
        m = num/den
    except ZeroDivisionError:
        print("Please enter at least two points to plot first.")
        check = False
    else:
        return m

# A function calculate 'c' in the equation y = mx + c using the intercept formula.
def calc_c (X, Y):
    sumX = sum(X)
    sumY = sum(Y)
    sumX2 = sum(i**2 for i in X)
    XY = zip(X, Y)
    sumXY = sum([x*y for x, y in XY])
    n = len(X)
    num = (sumX * sumXY) - (sumY*sumX2)
    den = (sumX**2) - (n * sumX2)
    try:
        c = num/den
    except ZeroDivisionError:
        pass
    else:
        return c

# A function for the use to maunally input the co-ordinate values.
def enter (x, y):
    global X, Y
    X.append(x)
    Y.append(y)

# A function to plot the final graph.
def plot ():
    global X, Y, check
    m = calc_m(X, Y)
    c = calc_c(X, Y)
    if check:
        plt.scatter(X, Y)
        Y2 = [m * i + c for i in X]
        plt.plot(X, Y2, color = 'r')
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.show()
    else:
        check = True
    print("\n\n")

# The Main part of the program,
print("Hi, this program can display a scatter plot and calculate the best fit line for that scatter plot " \
      + "and can create a graph showing both of them together. What would you like to do?")
print("Would you like to check out an example graph or would you like to input your own values?")

while True:
    # Taking primary input from the user.
    input1 = input("Enter the word 'example' to see the example graph, 'input' to create your own graph, "\
                   + "or 'quit' if you want to exit the program: ")

    if input1 == 'example':
        # Reading and checking the example .csv file and storing the input and output variables in lists.
        print("\n\nThe example graph shown here was produced from the sample dataset "\
              + "'Swedish Auto Insurance' which is a popular dataset for test values.")
        print("This dataset contains 63 points,and each point details the number of "\
              + "insurance claims, and the total payment for all claims in thousands of "\
              + "Swedish Kronor. \n")
        print("Here is a few lines of the dataset: \n")
        w = pd.read_csv("Example.csv")
        print(w.head(), "\n\n")
        X2 = list(w["Number of Claims"].values)
        Y2 = list(w["Total Payment"].values)

        # Calculating the value of 'm' and 'c'.
        m = calc_m(X2, Y2)
        c = calc_c(X2, Y2)

        # Plotting and displaying the scatter plot along with the best fit line.
        print("Here is the graph of the best-fit line through the scatter plot. ")
        plt.scatter(X2, Y2)
        Y3 = [m * i + c for i in X2]
        plt.plot(X2, Y3, color = 'r')
        plt.xlabel("Number of claims")
        plt.ylabel("Total Payment")
        plt.title("Best-fit line and scatter plot")
        plt.show()
        print("\n")
        continue

    elif input1 == 'input':
        # Taking secondary input from the user.
        print("\nWould you like to input the points manually, one at a time, or would you like "\
              + "to input them through a .csv file? ")
        input2 = input("Enter the word 'manual' to enter the points one at a time or 'csv' to "\
                       + "enter them through a .csv file: ")

        if input2 == 'manual':
            # Instructing the user how to enter his/her own values manually.
            print("\nEnter the X and corresponding Y values using the 'enter(X, Y)' function.")
            print("To enter axis labels and titles, assign strings to xlabel, ylabel and title.")
            print("Enter 'plot()' to display the graph after entering at least two points.")
            break
        
        elif input2 == 'csv':
            # Recieving information from the user about the csv file.
            csv_name = input("Enter the name of the csv file. Make sure it is in the same folder "\
                             + "as the program: ")
            x_col_name = input("Enter the name of the column containing the x values: ")
            y_col_name = input("Enter the name of the column containing the y values: ")
            
            # Reading and displaying a few lines of the csv file for the user to cross-check.
            # Also handling all possible exceptions.
            try:
                w = pd.read_csv(csv_name)
                print("Here is a preview of the csv file: \n")
                print("\n", w.head(), "\n")
                X = list(w[x_col_name].values)
                Y = list(w[y_col_name].values)
            except FileNotFoundError:
                print("Error: " + csv_name + " is not found. \n")
                continue
            except KeyError:
                print("Error: The X-column or Y-column name is incorrect. \n")
                continue
            except:
                print("Unexpected Error. \n")
                continue
            
            print("\nTo input more co-ordinate points, use the 'enter(X, Y)' function.")
            print("To enter axis labels and titles, assign strings to xlabel, ylabel and title.")
            print("Enter 'plot()' to display the graph.")
            break
        
        else:
            print("Unknown Command.")
            continue
        
    elif input1 == 'quit':
        print("\nThank You for using our program! ")
        break
    
    else:
        print("\nUnknown Command. \n")
        continue