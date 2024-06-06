BIN = {
 "F": "0",
 "B": "1",
 "L": "0",
 "R": "1"
}

input_file = open('5.input.txt', 'r')

input = input_file.readlines()
seat_ids = map(lambda x: int(''.join(map(lambda c: BIN[c], x.strip())), 2), input)

print(min(seat_ids))
print(max(seat_ids))
print(int(''.join(map(lambda c: BIN[c], "BFFFBBFRRR")), 2))

seat_ids.sort()

last_seat = seat_ids[0] - 1
for seat in seat_ids:
    if last_seat + 1 != seat:
        print("FOUND: " + str(last_seat + 1))
    last_seat = seat
