names = ['thomas', 'gabe', 'aaron', 'abdallah', 'david']
print(names[0])
print(names[3])
print(names[2]) 
print(names[4])
print(names[-1])
print(names[1])

message5 = "My first friend was " + names[-1].title() + "."
message4 = "My most recent freind is " + names[3].title() + "."
message1 = "My best friend in Austin is " + names[-1].title() + "."
message2 = names[2].title() + " was my best friend in college"
message3 = names[4].title() + " is actually my brother!"

print(message2)


cars = ['toyoata', 'ford', 'chevy', 'nissan']
message10 = "I want my next car to be a " + cars[2] + "."

print(message10)

cars[1] = 'cadillac'
print(cars)

del cars[-1]
print(cars)

popped_cars = cars.pop()
print(cars)

print(popped_cars)
