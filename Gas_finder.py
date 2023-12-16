import sys


def welcomeMessage():                                                   #This function will be used to display to the user the  purpose of this program. In here
                                                                        # you will find a statement that briefly introduces the gyst of the program.
    return("""                                                          
    Welcome to your trip estimated and automation.
    This automation will allow you to gauge and price your trip.
    Below you will be given questions to determine the price it will cost to travel from Georgia to Florida.""")

def gasMatrix():                                                    #This function is used to gather information from the user.
                                                                    #Assisting them in deciding whether to operate based of our
                                                                    #given gas prices or gas pricesthat they choose to enter
    print('*******************MAIN MENU*****************')
    print()
    choice= input ("""
    A: Use Given Gas Prices
    B: Use Gas Price in Your Area
    C: Quit/Log Out
    
    Please Enter Your Choice:""")
    if choice == "A" or choice == "a":
        displayGas()
    if choice == "B" or choice == "b":
        userGasPrices()
    if choice == 'C' or choice == 'c':
        print('system is logging off...')



def displayGas():                                                       #This function displays average gas prices throughout Georgia and Florida
    print("""
    Regular:      $2.15
    Mid-Grade:    $2.52
    Premium:      $2.81
    Diesel:       $2.71
    """, end=" ")

def userGasPrices():                                                    #This function is used if the user decides to input their own set gas prices.
                                                                        #It will convert different gas prices based off of what the user chooses to input.
                                                                        #After converting the gas prices, it will display the prices in a list, used for selection.
    userInputGas= float(input('What is The Price of Local "Regular" Gas in Your Area:'))
    midgrade = round(userInputGas + .36 ,2)
    premium = round(midgrade + .36, 2)
    diesel = round(premium -.10, 2)
    
    print('Regular:', userInputGas)
    print('Mid-Grade:', midgrade)
    print('Premium:', premium)
    print('Diesel:', diesel)
    print()

def userInputMatrix(answer):                                          #This function prompts the user to enter a select grade of gas. Based on the user's selection
                                                                      #a message will displayed, reinterating the users selection.
    regularPrice= (2.15)
    midGradePrice = 2.52
    premiumPrice = 2.82
    dieselPrice = 2.71
    if answer == 'regular' or answer == 'Regular':
        return regularPrice
    elif answer == 'Mid-Grade' or answer == 'mid-grade':
        return midGradePrice
    elif answer == 'premium' or answer == 'Premium':
        return premiumPrice
    elif answer == 'diesel' or answer == "Diesel":
        return dieselPrice

    print()



def continueMessage():                                   # This function is used simply as a message to be displayed to the user,
                                                         # on the course of action that will take place as they continue using the program
    return("""
   **** Lets Determine The Time and Fuel it Will Take to Reach The Destination ****""")

def drivetimeMileage(miles):                          #This function is used to calculate how long it will tale the user to arrive at their location
                                                      
   timeToLoca= miles / 60
   final = (round(timeToLoca,2))
   return final


def GasTankMPG(mpg,tankSize):                            #This function is used to calculate how far the user will able to travel based on
                                                         # the size of their tank and how many miles their car can travel per gallon.
    totalMileage= mpg * tankSize
    return totalMileage

def totalGasPrice(matrix,tanksize):
    gas = matrix * tanksize
    return gas

def finalCost(finalMileage,GasTank,tanksize,gas):
	initial = finalMileage/GasTank
	tankcost = gas* tanksize
	total = initial * tanksize
	final = tankcost * total
	return final
	
def main():                                                             # The main function recalls all previous functions into a summation.
    print(welcomeMessage())
    print('\n')
    print(gasMatrix())
    answer = input('Select your type of gas from the given list:')
    print(userInputMatrix(answer))
    print()
    print(continueMessage())
    print()
    tankSize= int(input('Enter Tank Size of Your vehicle:'))
    mpg= int(input("Enter MPG of Your Vehicle:"))
    print()
    distance=(GasTankMPG(mpg, tankSize))
    print("The Distance Before Refill will be", distance,"miles")
    print()
    miles= int(input('Enter Total Distance(in miles) to Florida Location:'))
    finalMileage= (drivetimeMileage(miles))
    print()
    print('It will take', finalMileage, "hours to reach your destination.")
    matrix= userInputMatrix(answer)
    totalGas=(totalGasPrice(tankSize,matrix))
    mortal_kombat=(finalCost(miles,distance,matrix,tankSize))
    finsh_him = round(mortal_kombat,2)
    print()
    print("Your final cost for a one way trip will be", finsh_him)
    









main()
