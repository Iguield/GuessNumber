import functions as f
import time

if __name__ == "__main__":
    
    print("So, you want to play a game right?")
    time.sleep(1)
    print("Okay, let's play a game")
    time.sleep(1)
    print("First, you will need to choose what game are we playing")
    choose = int(
        input(
            "1. I will choose a number and you will try to guess it \n2. You will choose a number and I will guess it \n"
        )
    )
    while choose != 3:
        if choose == 1:
            f.guess()
        elif choose == 2:
            f.computer_guess()
        time.sleep(3)
        choose = int(
            input(
                "Choose again: \n1. You try to guess \n2. I try to guess \n3. Exit \n"
            )
        )
    print("Well, I had a great time! Let's play again later, shall we?")
    print("Byeee!!")