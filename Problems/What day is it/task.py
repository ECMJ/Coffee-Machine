time = int(input(""))
utc = 10.5
result = utc + time
if -24 <= result < 0:
    print("Monday")
elif 0 <= result <= 24:
    print("Tuesday")
elif 24 < result <= 26:
    print("Wednesday")

