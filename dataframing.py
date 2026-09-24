import pandas as pd
data={
    "name":["aniket","adesh"],
    "age":[18,18]
}

df=pd.DataFrame(data,index=["student 1 ","student 2"])
df["marks"]=[45,46]
# print(df)

newrow=[{"name":"ayush","age":18,"marks":42},
        {"name":"aditya","age":18,"marks":41}
        ]
newrow=pd.DataFrame(newrow,index=["student 3","student 4"])


df=pd.concat([df,newrow])
df[" gender"]=["male","male","male","male"]
print(df)


