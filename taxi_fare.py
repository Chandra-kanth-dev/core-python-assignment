def calculate_fare(distance):
    return 50 + (distance * 10)

trips = list(map(int, input("Enter distances of trips (comma-separated): ").split(',')))

total = 0
for i, dist in enumerate(trips, 1):
    fare = calculate_fare(dist)
    print(f"Trip {i}: ${fare}")
    total += fare

print(f"Total Fare: ${total}")
