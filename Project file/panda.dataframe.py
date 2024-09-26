print("----Pandas frame----")
import pandas as pd
import numpy as np
i = 0
dat = pd.read_csv("C:/Users/Roopashree obalesh/Desktop/names.csv")
df=pd.DataFrame(dat)
print(df)
Course=pd.Series([])

while i <= 3:
    print("Select operation.")
    print("1.Create a data frame")
    print("2.Create a data frame from dict of nd arrays/list")
    print("3.Adding new column with static values")
    print("4.Pass different value for each row")

    choice = input("Enter choice(1/2/3):")
    if choice == '1':
        value = input("Enter comma separated values :")
        list = value.split(",")
        df=pd.DataFrame(list)
        print("The dataframe is: ")
        print(df)
        print("-------------------------------------------")      
            
    elif choice == '2':
        data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
        df = pd.DataFrame(data, index=['Emp01','Emp02','Emp03','Emp04'])
        print("The dataframe is : ")
        print(df)
        print("The data frame is created using dictionary")
        print("-------------------------------------------")
       
                                    
    elif choice == '3':
        print("The file is : ")
        print(dat)
        dat.insert(2,"Course","Any")
        print("File after adding the row Course : ")
        print(dat)
        print("-------------------------------------------")
       

    elif choice == '4':
        popped_col = dat.pop("Course")
        for i in range(len(dat)): 
            if dat["Age"][i] == 20: 
                Course[i]="MSc"
  
            elif dat["Age"][i] == 21: 
                Course[i]="MBA"
  
            elif dat["Age"][i] == 22: 
                Course[i]="MCA"
  
            else:
                Type_new[i]= dat["Age"][i]
        print("The file after adding row values to the new column : ")
        dat.insert(2, "Course", Course) 
        print(dat)
        print("-------------------------------------------")
                            
    else:
       print("Invalid input")
       break
