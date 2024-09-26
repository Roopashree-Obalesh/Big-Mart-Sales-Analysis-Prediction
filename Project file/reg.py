import numpy as np
import matplotlib.pyplot as plt  # To visualize
import pandas as pd  # To read data
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn import datasets, linear_model, metrics

print("...........Regression..............")
data = pd.read_csv("C:/Users/Roopashree obalesh/Desktop/diabetes.csv") 
print(data.head())

i=0

while i <= 3:
    print("Select operation.")
    print("1.Linear Regression ")
    print("2.Logistic Regression")
    print("3.Polinomial Regression")
    print("4.Exit")

    choice = input("Enter Your choice(1/2/3/4):")
    if choice == '1':
        print("Linear Regression")
        X = data.iloc[:, 0].values.reshape(-1, 1)  # values converts it into a numpy array
        Y = data.iloc[:, 3].values.reshape(-1, 1)  # -1 means that calculate the dimension of rows, but have 1 column
        linear_regressor = LinearRegression()  # create object for the class
        linear_regressor.fit(X, Y)  # perform linear regression
        Y_pred = linear_regressor.predict(X)  # make predictions

        # comparing actual response values (y_test) with predicted response values (y_pred) 
        #print("Linear Regression model accuracy(in %):",metrics.accuracy_score(Y, Y_pred)*100)

        plt.scatter(X, Y)
        plt.plot(X, Y_pred, color='red')
        plt.show()

    
    elif choice == '2':
        print("Logistic regression")

        X = data.iloc[:, 0].values.reshape(-1, 1)  # values converts it into a numpy array
        y = data.iloc[:, 2].values.reshape(-1, 1)

        
        # create logistic regression object 
        reg = linear_model.LogisticRegression() 
   
        # train the model using the training sets 
        reg.fit(X, y) 
  
        # making predictions on the testing set 
        y_pred = reg.predict(X) 
   
        # comparing actual response values (y_test) with predicted response values (y_pred) 
        print("Logistic Regression model accuracy(in %):",  
        metrics.accuracy_score(y, y_pred)*100)

        #visualization
        plt.scatter(X, y)
        plt.plot(X, y_pred, color='red')
        plt.show()



    elif choice == '3':

        print("Polynomial regression")
        
        X = data.iloc[:, 0].values.reshape(-1, 1)  # values converts it into a numpy array
        y = data.iloc[:, 2].values.reshape(-1, 1)

        poly = PolynomialFeatures(degree = 4) 
        X_poly = poly.fit_transform(X) 
  
        poly.fit(X_poly, y) 
        lin2 = LinearRegression() 
        lin2.fit(X_poly, y)

        # Visualising the Polynomial Regression results 
        plt.scatter(X, y, color = 'blue') 

        plt.plot(X, lin2.predict(poly.fit_transform(X)), color = 'red') 
        plt.title('Polynomial Regression') 
        plt.xlabel('Glucose') 
        plt.ylabel('Age') 

        plt.show() 

          
    elif choice=='4':
        print("Exiting.................")
        break
        
    else:
       print("Invalid input")
