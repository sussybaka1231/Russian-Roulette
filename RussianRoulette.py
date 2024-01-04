import random
import time

input("RUSSIAN ROULETTE\n\n\\\\\\ PRESS THE ENTER KEY TO CONTINUE \\\\\\")

def main():
    bullet_load = input("Load 1 bullet in round 1, 2, 3, 4, 5 or 6?: ")
    print("Loading...")
    time.sleep(1)
    cylinder = ["1", "2", "3", "4", "5", "6"]
    print("Rolling cylinder...")
    time.sleep(0.5)
    shuffled_cylinder = random.choice(cylinder)
    if shuffled_cylinder[0] == bullet_load:
        print("You died.")
    else:
        print("You are alive!")
    play_again = input("Play again? ((y)es/(n)o): ")
    if play_again.lower().startswith("y"):
        main()
    else:
        if __name__ == "__main__":
            exit()
        else:
            pass

main() 