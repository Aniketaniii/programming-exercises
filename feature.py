# #import library files 
# import pandas as pd
# import numpy as np

# #create a database containing missing values

# data={
#     'Age':[25,30,np.nan,35,40,42],
#     'Salary':[50000,np.nan,55000,65000,np.nan,70000],
#     'Department':['HR','Finance','IT',np.nan,'IT','HR']
# }

# #create a table using data and display

# df=pd.Dataframe(data)
# print("ORiginal data")
# print(df)

# #detect and display missing values
# print("\n MIssing values ")
# print(df.isnull())

# print("\n  Count of missing values")
# print(df.isnull().sum())

# # mean of age 
# dfmean=df.copy()
# meanage=df['Age'].mean()
# dfmean['Age'] = dfmean['Age'].fillna(meanage)
# print("Mean Imputed Data")
# print(dfmean)

# # median of salary 

# dfmedian=dfmean.copy()
# median=df['Salary'].median()
# dfmedian['Salary']=dfmedian['Salary'].fillna(median)
# print("\n MedianImputed data")
# print(dfmedian)

# #mode of department

# dfmode=dfmedian.copy()
# mode=df['Department'].mode()[0]  # 0 or 1  for hr or it
# dfmode['Department']=dfmode['Department'].fillna(mode)
# print("\n Mode imputed data")
# print(dfmode)

# # #forward fill

# # dfforward=df.copy()
# # dfforward=dfforward.ffill()
# # print("\n forward fill")
# # print(dfforward)

# # #backward fill

# # dfbackward=df.copy()
# # dfbacward=dfbackward.bfill()
# # print("\n backward fill")
# # print(dfbacward)


# # dfknn=df.copy()
# # numeric_columns=['Age','Salary']
# # imputer=KNNImputer(n_neighbors=2)
# # dfknn[numeric_columns]=imputer.fit_transforms(dfknn[numeric_columns])

# # print("\n KNN imputation")
# # print(dfknn)


units = int(input("Enter total units consumed: "))

fixed_charge = 150

if units > 100:
    variable_charge = (units - 100) * 6
else:
    variable_charge = 0

total_amount = fixed_charge + variable_charge


print("\n----- Electricity Bill -----")
print("Units Consumed      :", units)
print("Fixed Charge (₹)   :", fixed_charge)
print("Variable Charge (₹):", variable_charge)
print("Total Payable (₹)  :", total_amount)
