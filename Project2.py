"""
Program: Eason115P2.py
Author: Jeannette Eason
Date Written: 8/29/2020
Date Modified: 9/19/2020
Date Last Modified: 9/19/2020

This program calculates a person's BMI.

It requires the user to enter the correct password to allow access.
The user has 3 attempts to enter the correct password.
3 failed attempts prohibit the user the use the program and will
cause the program to terminate.

The program allows the user to calculate multiple BMI indexes
Once the user is done calculating BMI indexes, the program calculates
and print the total BMI, the average BMI, and the total count of
BMI indexes calculated.
The program also counts the number of people who are within normal range.
Lastly, the program creates a stats report; it counts and calculates
the number of BMI index entry within specific BMI range

"""



def main():

   
   Pass = enterThePassword()
   

def enterThePassword():
   count = 0
   attempts = 3
   
   Password = str(input("Enter a password: "))# ask the user to enter a password
   count = count + 1 # counts the number of password entry
   password = 'BMI2020'

   while Password != password and count != attempts: # condition for incorrect password
      print("Please enter the correct password")
      Password = str(input("Enter a password: "))
      count = count + 1  # counts the number of password entry
   if count == attempts: # this condition will run when user entry incorrect password 3 times
      print("You've reached the maximum limit of incorrect password entry")
      print("Please try again later")
   else: # will allow user to proceed and use the program
      print("\nWelcome! You may now use the program.\n")
      Stats = createTheStatsReport()
   


def createTheStatsReport():
   count = 0
   bmi = 0 
   normalRange = 0 
   Stats1 = 0
   Stats2 = 0
   Stats3 = 0
   Stats4 = 0
   averageStats1 = 0
   averageStats2 = 0
   averageStats3 = 0
   averageStats4 = 0
   bmi1 = 0
   bmi2 = 0
   bmi3 = 0
   bmi4 = 0


   HeightInFeet = int(input("Please enter your height in feet: "))
   HeightInInches = int(input("Please enter your height in inches: "))
   Feet = HeightInFeet * 12
   Height = (Feet + HeightInInches)
   Weight = float(input("Please enter your weight in pounds: "))
   BMI = 703*(Weight/Height**2)
   count = count + 1 #counts the number of BMI entry
   bmi = bmi + BMI #calculates the total BMI
   averageBMI = bmi/count #calculates the average BMI
   
   print("Your BMI is: " + str(BMI))

   
   if BMI >= 18.5 and BMI <= 24.9:
      normalRange = normalRange + 1 # calculates the entry within normal range
      
   if BMI >= 0.0 and BMI <= 16.3:
      Stats1 = Stats1 + 1 #sums up the number of people within BMI range 0.0-16.3
      bmi1 = bmi1 + BMI # adds the total BMI
      averageStats1 = bmi1/Stats1 # calculates the average BMI for this category
      
   if BMI >= 16.4 and BMI <= 20.2:
      Stats2 = Stats2 + 1 #sums up the number of people within BMI range 16.4-20.2
      bmi2 = bmi2 + BMI # adds the total BMI
      averageStats2 = bmi2/Stats2 # calculates the average BMI for this category
      
      
   if BMI >= 20.3 and BMI <= 28.8:
      Stats3 = Stats3 + 1 #sums up the number of people within BMI range 20.3-28.8
      bmi3 = bmi3 + BMI # adds the total BMI
      averageStats3 = bmi3/Stats3 # calculates the average BMI for this category
      
   if BMI >= 28.8:
      Stats4 = Stats4 + 1 #sums up the number of people within BMI greater than 28.8
      bmi4 = bmi4 + BMI # adds the total BMI
      averageStats4 = bmi4/Stats4 # calculates the average BMI for this category
      
   print("\nDo you want to compute another BMI index?")
   NewIndex = str(input("Press any key to continue or press enter to quit: "))


   
   

   while NewIndex != "":
      HeightInFeet = int(input("\nPlease enter your height in feet: "))
      HeightInInches = int(input("Please enter your height in inches: "))
      Feet = HeightInFeet * 12
      Height = (Feet + HeightInInches)
      Weight = float(input("Please enter your weight in pounds: "))
      BMI = 703*(Weight/Height**2)
      count = count + 1 #counts the number of BMI entry
      bmi = bmi + BMI  #calculates the total BMI
      averageBMI = bmi/count #calculates the average BMI
      
      
      
      print("Your BMI is: " + str(BMI))

      
      if BMI >= 18.5 and BMI <= 24.9:
         normalRange = normalRange + 1 # calculates the entry within normal range
         
      if BMI >= 0.0 and BMI <= 16.3:
         Stats1 = Stats1 + 1 #sums up the number of people within BMI range 0.0-16.3
         bmi1 = bmi1 + BMI # adds the total BMI
         averageStats1 = bmi1/Stats1 # calculates the average BMI for this category
         
      if BMI >= 16.4 and BMI <= 20.2:
         Stats2 = Stats2 + 1 #sums up the number of people within BMI range 16.4-20.2
         bmi2 = bmi2 + BMI # adds the total BMI
         averageStats2 = bmi2/Stats2 # calculates the average BMI for this category
         
      if BMI >= 20.3 and BMI <= 28.8:
         Stats3 = Stats3 + 1 #sums up the number of people within BMI range 20.3-28.8
         bmi3 = bmi3 + BMI # adds the total BMI
         averageStats3 = bmi3/Stats3 # calculates the average BMI for this category
         
      if BMI >= 28.8: 
         Stats4 = Stats4 + 1 #sums up the number of people within BMI greater than 28.8
         bmi4 = bmi4 + BMI # adds the total BMI
         averageStats4 = bmi4/Stats4 # calculates the average BMI for this category

      
         
      print("\nDo you want to compute another BMI index?")
      NewIndex = str(input("Press any key for yes or press enter to quit: "))
   
      
      

    
   print("\nThank you for using the program!")
   print("\nThe total BMI is: ", bmi)
   print("The average BMI is: ", averageBMI)
   print("The total count for BMI indexes calculated is: ", count)
   print("The normal range is: ", normalRange)
   print("\nThe number of BMI entry in range 0.0-16.3 is: ", Stats1)
   print("The number of BMI entry in range 16.4-20.2 is: ", Stats2)
   print("The number of BMI entry in range 20.3-28.8 is: ", Stats3)
   print("The number of BMI entry 28.8 and over is: ", Stats4)
   print("\nThe average for BMI range 0.0-16.3 is: ", averageStats1)
   print("The average for BMI range 16.4-20.2 is: ", averageStats2)
   print("The average for BMI range 20.3-28.8: ", averageStats3)
   print("The average for BMI greater than 28.8 is: ", averageStats4)
   

main()



