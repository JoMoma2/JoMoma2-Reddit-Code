"""
Quinten Peters, 10-08-22, Project 3

Presume that you are working for a shipping company.

Design a program that calculates the total shipping charge required to ship a package based on weight and distance traveled.   

For the project use the chart below:

Weight / Zone Chart
Weight	Zone 1	Zone 2	Zone 3
< 5 pounds	6.00	7.00	8.00
>= 5 pounds and <= 10 Pounds	8.00	10.00	12.00
> 10 pounds	10.00	15.00	20.00"""

# Definitions
def weight():
    weight = int(input("What is the weight? "))
    return weight

def zone():
    zone = int(input("Which zone are you trying to ship to? "))
    return zone

"""This is running the weight() function twice if weight() > 5 because that is what I am telling it to do.
I'm not sure how to not make it recall the function and just get it to use the input already provided.

def processing():
    if weight() < 5:
        if zone() == 1:
            cost = 6
        elif zone() == 2:
            cost = 7
        else :
            cost = 8
    elif weight() <= 10:
        if zone() == 1:
            cost = 8
        elif zone() == 2:
            cost = 10
        else :
            cost = 12
    else: 
        if zone() == 1:
            cost = 10
        elif zone() == 2:
            cost = 15
        else :
            cost = 20
    
    return(cost)
    
    
    Made the functions equal to a variable and that worked. Example used down below is as follows:
    
    weightarg = weight()
    zonearg = zone()
    
    if weightarg < 5:
        if zonearg == 1:
            cost = 6
        elif zonearg == 2:
            cost = 7
        else :
            cost = 8
    elif weightarg <= 10:
        if zonearg == 1:
            cost = 8
        elif zonearg == 2:
            cost = 10
        else :
            cost = 12
    else: 
        if zonearg == 1:
            cost = 10
        elif zonearg == 2:
            cost = 15
        else :
            cost = 20
    
    weightarg becomes a variable that is the same as what the function "weight" returns and the same goes for the function "zone".
    This calls the function once and only once, while being able to recall the inputs further down in the program.
    """

def processing():
    weightarg = weight()
    zonearg = zone()
    
    if weightarg < 5:
        if zonearg == 1:
            cost = 6
        elif zonearg == 2:
            cost = 7
        else :
            cost = 8
    elif weightarg <= 10:
        if zonearg == 1:
            cost = 8
        elif zonearg == 2:
            cost = 10
        else :
            cost = 12
    else: 
        if zonearg == 1:
            cost = 10
        elif zonearg == 2:
            cost = 15
        else :
            cost = 20
    
    return(cost)

def printing():
    print("Your package will cost " + str(processing()) + " dollars to ship")


#Puting it all together
printing()