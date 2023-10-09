succesful = False

for attempt in range(3):
    print(f"attempt {attempt+1}")
    if succesful:
        print("succesfull attempt")
        break
else:
    print(f"ateempt {attempt+1} times with fail")
