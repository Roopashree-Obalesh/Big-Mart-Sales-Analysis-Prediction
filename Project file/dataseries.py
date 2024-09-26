print("----Pandas series----")
import pandas as pd
import numpy as np
i = 0
df = pd.read_csv("C:/Users/Roopashree obalesh/Desktop/names.csv")
ser = pd.Series(df['Names'])

while i <= 3:
    print("Select operation.")
    print("1.Creating and Accessing the elements of series")
    print("2.Addition of data series")
    print("3.Read from a file and convert into series")
    print("4.Accessing the elements using iloc function")

    choice = input("Enter choice(1/2/3):")
    if choice == '1':
        value = input("Enter comma separated values :")
        list = value.split(",")
        ser=pd.Series(list)
        print("The dataseries is: ", "\n" ,ser)
        print("Accessing the elements ser[:4] : ",ser[:5])
        
            
    elif choice == '2':
        data = pd.Series([5, 2, 3,7], index=['a', 'b', 'c', 'd'])
        data1 = pd.Series([1, 6, 4, 9], index=['a', 'b', 'c', 'd'])
        print(data, "\n\n", data1)
        a=data.add(data1, fill_value=0)
        print("The added data series is : ",a)
       
                                    
    elif choice == '3':
        dat = ser.head(10)
        print(dat)
       

    elif choice == '4':
        dat = ser.head(10)
        print("The elements are : ",dat.iloc[3:6])
        break       
                            
    else:
       print("Invalid input")
       break
