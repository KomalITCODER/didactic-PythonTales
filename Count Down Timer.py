## COunt Down Timer

import time 

my_time = int(input("What timer u would like to set:"))


print(f"Times is over")

print("x"*100)

for x in range(my_time , 0 , -1):
    sec = x% 60
    min = int((x/60) % 60)
    hrs = int(x/3600)
    time.sleep(1)
    print(f"{hrs:02}:{min:02}:{sec:02}")
