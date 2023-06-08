import random
import time

def guess():
    max = int(input("Choose the range you will try to guess (from one to): "))
    randNumber = random.randint(1, max)
    x = 0
    cont = 0
    while x != randNumber:
        x = int(input("Give it a try: "))
        cont += 1
        res = abs(x - randNumber)
        if x == randNumber:
            print(
                "Congratulations, you got it! \nThe secret number was: ",
                randNumber,
                "\nYou tried ",
                cont,
                "times",
            )
        elif res <= 2:
            print("ALMOST!")
        elif res <= 5:
            print("Getting there...")
        elif res > 5:
            print("Come on bro, you are better than this!")


def computer_guess():
    numberLow = 1
    numberRange = int(input("First of all, I will need a range so that I know how to work, right?\nSo come on, I will try to guess between 1 and: "))
    x = int(input("Okay, so now choose a number and I will try to guess it.\nDon't worry, I am going to close my eyes for just a second so I won't see what you will choose.\nAre you ready?\nChoose now!: "))
    limit = numberRange
    time.sleep(2)
    print("Did you type it in already? Can I look? Okay, this is going to be fun!")
    time.sleep(1)
    guess = 0
    cont = 0
    choosen = []
    while guess != x:
        guess = random.choice([i for i in range(numberLow, numberRange+1) if i not in choosen])
        cont += 1
        choosen.append(guess)
        dif = guess - x
        res = abs(dif)
        if dif < 0:
            numberLow = guess + 1
        else:
            numberRange = guess - 1
        if numberLow > numberRange:
            numberRange = numberLow
        if numberLow < 0:
            numberLow = 1
        if numberRange > limit:
            numberRange = limit
        print("Is it", guess, "?")
        time.sleep(1)
        if guess == x:
            print("YAAY!! I GOT IT! UHUUULLL!\nAnd guess what?? It only took me", cont, "tries!")
        elif res <= 2:
            print("Hmmm, I know I am getting close, right? Let me think and try again...")
            time.sleep(2)
        elif res <= 5:
            print("Well, I know that I am neither close nor too far... Let me think a little bit.")
            time.sleep(2)
        elif res > 5:
            print("Yeah, that was not a great shot, was it? Okay, I will have to think better...")
            time.sleep(2)
            print("JUST GIVE ME A SECOND!")
            time.sleep(1)