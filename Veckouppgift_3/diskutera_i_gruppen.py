x =0
y = 1
while y < 10:
        if y % 2 == 0:
            x -= y
        else:
            x += y * y
        y += 1
print(x)

message = "its_time_to_get_coding"
print(message[4:8])

answer = 0
for i in range(101):
    answer +=i
print("Summan av talen från 1 till 10 är: " + str(answer))

answer = 0
for i in range(11):
    answer +=i
print("Summan av talen från 1 till 10 är: " + str(answer))

limit = 11
index = 0
while index <=limit:
    print (index)
    index = index + 1


numbers = [1, -2, 3, -2, 4, -3]
total = 0

for number in numbers:
    total += number
    print(total)


movies =  ["SAW", "John Carter", "Edge of tomorrow", "Merry Poppins"]
print("Movies in the list:")
for movie in movies:
           print(movie)

