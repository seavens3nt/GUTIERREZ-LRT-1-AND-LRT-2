# File: lrt_simulation.py

# List of stations in sequence
stations = [
    "Roosevelt", "Balintawak", "Monumento", "5th Avenue", "R. Papa", "Abad Santos", 
    "Blumentritt", "Tayuman", "Bambang", "Doroteo Jose", "Carriedo", "Central Terminal",
    "UN Avenue", "Pedro Gil", "Quirino", "Vito Cruz", "Gil Puyat", "Libertad", 
    "EDSA", "Baclaran"
]

# Fare matrices
stored_value_fares = [
    [13, 14, 15, 16, 17, 18, 19, 20, 22, 23, 23, 24, 25, 26, 27, 28, 29, 30, 33, 35],
    [14, 13, 15, 15, 17, 18, 19, 20, 21, 22, 23, 24, 24, 25, 26, 27, 28, 29, 32, 34],
    [15, 15, 13, 14, 15, 16, 17, 18, 20, 21, 22, 22, 23, 24, 25, 26, 27, 28, 31, 33],
    [16, 15, 14, 13, 15, 16, 17, 17, 19, 20, 21, 21, 22, 23, 24, 25, 26, 27, 30, 32],
    [17, 17, 15, 15, 13, 14, 15, 16, 18, 19, 19, 20, 21, 22, 23, 24, 25, 26, 29, 31],
    [18, 18, 16, 16, 14, 13, 14, 15, 17, 18, 18, 19, 20, 21, 22, 23, 24, 25, 28, 30],
    [19, 19, 17, 17, 15, 14, 13, 14, 16, 17, 17, 18, 19, 20, 21, 22, 23, 24, 27, 29],
    [20, 20, 18, 17, 16, 15, 14, 13, 15, 16, 16, 17, 18, 19, 20, 21, 22, 23, 26, 28],
    [22, 21, 20, 19, 18, 17, 16, 15, 13, 14, 15, 16, 17, 17, 18, 19, 20, 22, 24, 27],
    [23, 22, 21, 20, 19, 18, 17, 16, 14, 13, 14, 15, 16, 16, 18, 18, 20, 21, 24, 26],
    [23, 23, 22, 21, 19, 18, 17, 16, 15, 14, 13, 14, 15, 16, 17, 18, 19, 20, 23, 25],
    [24, 24, 22, 21, 20, 19 ,18, 17, 16, 15, 14, 13, 14, 15, 16, 17, 18, 19, 22, 24],
    [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 14, 15, 16, 17, 18, 21, 23],
    [26, 25, 24, 23, 22, 21, 20, 19, 17, 16, 16, 15, 14, 13, 14, 15, 16, 18, 20, 23],
    [27, 26, 25, 24, 23, 22, 21, 20, 18, 18, 17, 16, 15, 14, 13, 14, 15, 17, 19, 22],
    [28, 27, 26, 25, 24, 23, 22, 21, 19, 18, 18, 17, 16, 15, 14, 13, 14, 16, 18, 21],
    [29, 28, 27, 26, 25, 24, 23, 22, 20, 20, 19, 18, 17, 16, 15, 14, 13, 15, 17, 20],
    [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 18, 17, 16, 15, 13, 16, 18],
    [33, 32, 31, 30, 29, 28, 27, 26, 24, 24, 23, 22, 21, 20, 19, 18, 17, 16, 13, 16],
    [35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 23, 22, 21, 20, 18, 16, 13]
]

single_journey_fares = [
    [0, 15, 15, 20, 20, 20, 20, 20, 25, 25, 25, 25, 25, 30, 30, 30, 30, 30, 35, 35],
    [15, 0, 15, 15, 20, 20, 20, 20, 25, 25, 25, 25, 25, 25, 30, 30, 30, 30, 35, 35],
    [15, 15, 0, 15, 15, 20, 20, 20, 20, 25, 25, 25, 25, 25, 25, 30, 30, 30, 35, 35],
    [20, 15, 15, 0, 15, 20, 20, 20, 20, 20, 25, 25, 25, 25, 25, 25, 30, 30, 30, 35],
    [20, 20, 15, 15, 0, 15, 15, 20, 20, 20, 20, 20, 25, 25, 25, 25, 25, 30, 30, 35],
    [20, 20, 20, 20, 15, 0, 15, 15, 20, 20, 20, 20, 20, 25, 25, 25, 25, 25, 30, 30],
    [20, 20, 20, 20, 15, 15, 0, 15, 20, 20, 20, 20, 20, 20, 25, 25, 25, 25, 30, 30],
    [20, 20, 20, 20, 20, 15, 15, 0, 15, 20, 20, 20, 20, 20, 20, 25, 25, 25, 30, 30],
    [25, 25, 20, 20, 20, 20, 20, 15, 0, 15, 15, 20, 20, 20, 20, 20, 20, 25, 25, 30],
    [25, 25, 25, 20, 20, 20, 20, 20, 15, 0, 15, 15, 20, 20, 20, 20, 20, 25, 25, 30],
    [25, 25, 25, 25, 20, 20, 20, 20, 15, 15, 0, 15, 15, 20, 20, 20, 20, 20, 25, 25],
    [25, 25, 25, 25, 20, 20, 20, 20, 20, 15, 15, 0, 15, 15, 20, 20, 20, 20, 25, 25],
    [25, 25, 25, 25, 25, 20, 20, 20, 20, 20, 15, 15, 0, 15, 15, 20, 20, 20, 25, 25],
    [30, 25, 25, 25, 25, 25, 20, 20, 20, 20, 20, 15, 15, 0, 15, 15, 20, 20, 20, 25],
    [30, 30, 25, 25, 25, 25, 25, 20, 20, 20, 20, 20, 15, 15, 0, 15, 15, 20, 20, 25],
    [30, 30, 30, 25, 25, 25, 25, 25, 20, 20, 20, 20, 20, 15, 15, 0, 15, 20, 20, 25],
    [30, 30, 30, 30, 25, 25, 25, 25, 20, 20, 20, 20, 20, 20, 15, 15, 0, 15, 20, 20],
    [30, 30, 30, 30, 30, 25, 25, 25, 25, 25, 20, 20, 20, 20, 20, 20, 15, 0, 20, 20],
    [35, 35, 35, 30, 30, 30, 30, 30, 25, 25, 25, 25, 25, 20, 20, 20, 20, 20, 0, 20],
    [35, 35, 35, 35, 35, 30, 30, 30, 30, 30, 25, 25, 25, 25, 25, 25, 20, 20, 20, 0]
]

# Discount rates
discounts = {
    "regular": 0.0,
    "student": 0.20,
    "pwd": 0.30,
    "senior": 0.30
}

def get_card_type():
    print("\n♡ Select card type: Regular, Student, PWD/Senior")
    card_type = input("\nEnter card type: ").strip().lower()
    print("\n﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌")
    while card_type not in discounts:
        card_type = input("Enter card type: \n").strip().lower()
        print("﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌\n")
    return card_type

def select_station(prompt):
    print(f"{prompt} (Enter number only):")
    print("\n﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌\n")
    for idx, station in enumerate(stations):
        print(f"{idx}: {station}")
    
    print("\n﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌")
    station_choice = input("\nEnter Station: ").strip()
    while not station_choice.isdigit() or int(station_choice) not in range(len(stations)):
        print("\n﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌")
        print("♡ Invalid choice. Try again. ♡")
        station_choice = input("\nEnter Station: ").strip()
        print("\n﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌")
    
    return int(station_choice)

def calculate_fare(start_idx, end_idx, fare_matrix, discount_rate):
    fare = fare_matrix[start_idx][end_idx]
    discounted_fare = fare * (1 - discount_rate)
    return discounted_fare

# Total distance of the line in km
total_line_distance_km = 19.7
# Number of segments
number_of_segments = len(stations) - 1
# Distance per segment
distance_per_segment = total_line_distance_km / number_of_segments

def main():
    total_distance = 0
    total_fare = 0
    card_type = get_card_type()
    discount_rate = discounts[card_type]

    print("\n♡ Card Type: Beep Card or Single Journey Ticket?")
    fare_type = input("\nEnter '1' for Beep Card or '2' for Single Journey Ticket: ").strip().upper()
    print("\n﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌\n")
    while fare_type not in ['1', '2']:
        print("\n♡ Invalid choice. Try again. ♡")
        fare_type = input("\nEnter '1' for Beep Card or '2' for Single Journey Ticket: \n").strip().upper()
        print("\n﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌")
    
    fare_matrix = stored_value_fares if fare_type == '1' else single_journey_fares

    initial_station_idx = select_station("Select initial station")
    print("\n﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌")
    print(f"\nYou are currently at {stations[initial_station_idx]} station.")

    while True:
        print("\n﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌")
        final_station_idx = select_station("\nSelect final station")
        
        while final_station_idx == initial_station_idx:
            print("\n♡ Initial and final station cannot be the same. Please choose a different final station.♡")
            print("\n﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌")
            final_station_idx = select_station("\nSelect final station")

        # Fare and distance
        fare = calculate_fare(initial_station_idx, final_station_idx, fare_matrix, discount_rate)
        distance_traveled = abs(final_station_idx - initial_station_idx) * distance_per_segment  # Calculate distance in km

        total_fare += fare
        total_distance += distance_traveled

        # trip details
        print(f"\nStations traveled: {stations[initial_station_idx]} -> {stations[final_station_idx]}")
        print(f"Fare for this ride: PHP {fare:.2f}")
        print("\n﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌")
        print(f"\nYou have arrived at {stations[final_station_idx]} station.")

        ride_again = input("\n♡ Do you want to ride again? (yes/no): ").strip().lower()
        if ride_again != 'yes':
            break

        initial_station_idx = final_station_idx
        print(f"\nYou are currently at {stations[initial_station_idx]} station.")
    
    print(f"Total distance traveled: {total_distance:.2f} km")
    print(f"Total fare: PHP {total_fare:.2f}")

if __name__ == "__main__":
    main()