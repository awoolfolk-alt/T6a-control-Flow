

#Formula returns 1-30 days and evrything that is divisible by 3, 5, and 15. 
for day in range(1, 31):
    if day % 15 == 0:
        print(f"Day {day}: FULL AUDIT")
    elif day % 5 == 0:
        print(f"Day {day}: Scanner audit")
    elif day % 3 == 0:
        print(f"Day {day}: Cycle count")
    else:
        print(f"Day {day}: Normal operations")