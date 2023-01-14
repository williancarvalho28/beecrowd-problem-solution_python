#beecrowd - 1061
# Event time

day1, date1 = input().split(" ")
date1 = int(date1)
hr1, mts1, sec1 = map(int, input().split(":"))

day2, date2 = input().split(" ")
date2 = int(date2)
hr2, mts2, sec2 = map(int, input().split(":"))

sec = (sec2 - sec1)
mts = (mts2 - mts1)
hr = (hr2 - hr1)
day = (date2 - date1)

if (sec < 0):
    sec += 60
    mts -= 1

if (mts < 0):
    mts += 60
    hr -= 1
    
if (hr < 0):
    hr += 24
    day -= 1
    
print(f"{day} dia(s)")
print(f"{hr} hora(s)")
print(f"{mts} minuto(s)")
print(f"{sec} segundo(s)")