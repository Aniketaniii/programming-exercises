
import time

a=int(input("Enter a value in secs : "))
for i in range(a,0,-1):
    secs=int(i%60)
    mins=int(i%60)%60
    hrs=int(i/3600)
    time.sleep(1)

    print(f"{hrs:02}:{mins:02}:{secs:02}")
print("Times up! ")