import numpy as np
import math
import pandas as pd

print("...........NumPy : Mathematics,Staistics..............")
sal=pd.read_csv("C:/Users/Roopashree obalesh/Desktop/empsal.csv")
sal.head()

i=0

while i <= 2:
    print("Select operation.")
    print("1.Mathematical Operations ")
    print("2.Statistical Operations")
    print("3.Exit")

    choice = input("Enter choice(1/2/3):")
    if choice == '1':
            print("You have chosen Mathematical operations")
            print("1.Cos functions ")
            print("2.Sin functions")
            print("3.Rounding Functions")
            print("4.Acending functions")
            print("5.Power function")
            print("6.Maximum and minimum functions")
            print("7.Absolute function")
            choice = input("Enter choice for Mathematical Function using Numpy operation(1/2/3/4/5/6/7):")
            if choice == '1':
                 in_array = [0, math.pi / 2, np.pi / 3, np.pi]
                 print ("Input array : \n", in_array)
 
                 cos_Values = np.cos(in_array)
                 print ("\nCosine values : \n", cos_Values)
                 
            elif choice == '2':
                in_array = [0, math.pi / 2, np.pi / 3, np.pi]
                print ("Input array : \n", in_array)
 
                Sinh_Values = np.sinh(in_array)
                print ("\nSine Hyperbolic values : \n", Sinh_Values)
                
            elif choice == '3':
                p=sal['Salary'].round()
                print ("\nRounded values : \n", p)
 
            elif choice =='4':
                 a=sal.sort_values(["Age", "First Name"], axis=0, ascending=True, inplace=True)
                 print("The employee details in ascending order based on Age and First Name are :",sal)
                 
            elif choice == '5':
                arr1 = [2, 2, 2, 2, 2] 
                arr2 = [2, 3, 4, 5, 6] 
                print ("arr1         : ", arr1) 
                print ("arr1         : ", arr2) 
  
                # output_array 
                out = np.power(arr1, arr2) 
                print ("\nOutput array of power function : ", out)
               
            elif choice == '6':
                print("Maximum active years of an employee",sal['active_yrs'].max() )
                print("Minimum active years of an employee ",sal['active_yrs'].min() )
                
            elif choice == '7':
                print ("Absolute Value of Marks : \n", sal.active_yrs.abs())
 
            else:
                print("Invalid choice") 
        

    elif choice == '2':
        print("You have chosen Staistical Operations")
        print("1.Mean Salary")
        print("2.Total sum and count of salaries")
        print("3.Maximum Salary and Minimum salary")
        print("4.Standard deviation of salaries")
        print("5.Varience of salaries")
        choice = input("Enter choice for Statistical operations using Numpy (1/2/3/4/5):")
        if choice == '1':
  
             print("Array:\n",sal.head())  
  
             mean1 = sal['Salary'].mean()
             print ('Mean salary: ' + str(mean1))
  
             
        elif choice == '2':
             sum1 = sal['Salary'].sum()
             print ('Sum of salaries: ' + str(sum1))
             #groupby_sum1 = sal.groupby(['Country']).sum()
             #print ('Sum of values, grouped by the Country: ' + str(groupby_sum1))
             count1 = sal['Salary'].count()
             print ('Count of salaries: ' + str(count1))
             #groupby_count1 = sal.groupby(['Country']).count()
             #print ('Count of values, grouped by the Country: ' + str(groupby_count1))

             
        elif choice == '3' :
            max1 = sal['Salary'].max()
            min1 = sal['Salary'].min()
            print ('Max salary: ' + str(max1))
            print ('Min salary: ' + str(min1))

        elif choice == '4' :
            std1 = sal['Salary'].std()
            print ('Standard deviation of salaries: ' + str(std1))

        elif choice =='5':
            var1 = sal['Salary'].var()  
            print ('Var of salaries: ' + str(var1))
            
        else:
            print("Ivalid choice")
            
    elif choice=='3':
        print("Exiting.................")
        break
        
    else:
       print("Invalid input")
