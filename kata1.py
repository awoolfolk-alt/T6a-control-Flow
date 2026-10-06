# want to print out the check times for the first 10 checks in a shift, which occur every 15 minutes starting from 15 minutes after the shift starts.
check_times = range(15, 151, 15)
for check in range(1, 11):
    print(f"Check {check}: {check_times[check - 1]} Minutes After Shift Start")





