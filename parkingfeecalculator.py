vehicle = input("vehicle:")
hours = float(input("hours:"))
parking_fee = float(input("parking fee:"))
if hours<=0:
  print("Invalid parking duration")
elif vehicle == "Car" or vehicle == "Bike" or vehicle == "SUV":
    if hours<1:
        hours=1
    if vehicle=="Car":
        first_rate=50
        additional_rate=20
    elif vehicle=="Bike":
        first_rate=30
        additional_rate=10
    else:
        first_rate=70
        additional_rate=30
    if hours <=2:
        fee = first_rate
    else:
        extra_hours = hours-2
        fee = first_rate + (extra_hours*additional_rate)
    print("Vehicle:",vehicle)
    print("Hours:",hours)
    print("parking Fee:",fee)
else:
    print("Invalid vehicle type")


