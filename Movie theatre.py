n = int(input("Enter number of shows: "))
shows = []
total_booked = 0
total_available = 0
high_demand_count = 0

for i in range(n):
    data = input("Enter show name, total seats and booked seats: ").split()

    if len(data) != 3:
        print("Invalid input. Enter all three values.")
        continue
    show_name = data[0].strip()
    total_seats = int(data[1].strip())
    booked_seats = int(data[2].strip())
    if total_seats <= 0 or booked_seats < 0 or booked_seats > total_seats:
        print("Invalid seat details")
        continue
    available_seats = total_seats - booked_seats
    occupancy = (booked_seats / total_seats) * 100
    if occupancy >= 80:
        category = "House Full"
    elif occupancy >= 60:
        category = "High Demand"
    elif occupancy >= 40:
        category = "Moderate"
    else:
        category = "Low Demand"
    print(f"{show_name} - Available: {available_seats} - Occupancy: {occupancy:.2f}% - {category}")
    shows.append([show_name, occupancy])
    total_booked += booked_seats
    total_available += available_seats
    if category == "High Demand" or category == "House Full":
        high_demand_count += 1
if len(shows) > 0:
    highest_show = shows[0]
    for show in shows:
        if show[1] > highest_show[1]:
            highest_show = show
print("Highest Occupancy:", highest_show[0])
print("Total Booked Seats:", total_booked)
print("Total Available Seats:", total_available)
print("High Demand/House Full Shows:", high_demand_count)
