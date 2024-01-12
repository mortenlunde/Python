print("Welcome to my little game!\n\n")

playing = input("Do you want to play a little game?\n")

if playing.lower() != "yes":
    print("Too bad, byeeeeee!")
    quit()

print("Lets go!\n")
print("What does theese abriviations stand for?\n")
score = 0

answer = input("CPU?\n")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Sorry, incorrect!")

answer = input("GPU?\n")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Sorry, incorrect!")
    
answer = input("RAM?\n")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Sorry, incorrect!")
    
answer = input("PSU?\n")
if answer.lower() == "power supply unit":
    print("Correct!")
    score += 1
else:
    print("Sorry, incorrect!")
    
answer = input("SSD?\n")
if answer.lower() == "solid state drive":
    print("Correct!")
    score += 1
else:
    print("Sorry, incorrect!")
    
print("Your total score is " + str(score) + " out of 5.")
print("That means you got " + str((score / 5) * 100) + "%.")
