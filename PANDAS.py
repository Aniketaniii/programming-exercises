import pandas as pd

data=[100,200,300,400,500]

series=pd.Series(data,index=["day 1","day 2","day 3 ","day 4","day 5"])

series.loc["day 1"]=10
print(series)
print(series[series>100])

mydict={"day 1":30,"day 2":50,"day 3":20}
s1=pd.Series(mydict)

print(s1)
print(s1["day 2"])
print(s1.iloc[0])


dic={"name": "aniket","age": 18,"gender":"male","mail":"aniiiiketgupta@gmail.com"}
s2=pd.Series(dic)

print(s2)