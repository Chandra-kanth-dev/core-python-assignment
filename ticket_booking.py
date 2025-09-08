def available_seats(total, booked):
    return [i for i in range(1, total+1) if i not in booked]

def book_seat(booked, seat):
    if seat in booked:
        print("Seat already booked")
    else:
        booked.append(seat)

def cancel_seat(booked, seat):
    if seat in booked:
        booked.remove(seat)

if __name__ == "__main__":
    total = int(input("Enter total number of seats: "))
    booked = list(map(int, input("Enter booked seats (space separated): ").split()))

    book = int(input("Enter seat number to book: "))
    book_seat(booked, book)

    cancel = int(input("Enter seat number to cancel: "))
    cancel_seat(booked, cancel)

    print("Available seats:", available_seats(total, booked))
