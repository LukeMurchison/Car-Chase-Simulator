from dataclasses import dataclass
import random


@dataclass
class player:
    health: int
    speed: int
    crime: str
    onfoot: bool


class cop:
    health: int
    speed: int
    number: int
    type: str


def game(player, cop) -> bool:
    if player.health <= 0 or cop.health <= 0:
        return False
    else:
        return True


def info(player, cop, action_num) -> None:
    print(f"Your Speed: {player.speed}")
    print(f"Your Health: {player.health}")
    print(f"Number of actions {action_num}")
    print(f"<---#--->")
    print(f"Cop Health: {cop.health}")
    print(f"Cop Speed: {cop.speed}")


def straight(action, action_num):
    if action == "STRAIGHT":
        rng = random.randint(1, 4)
        if rng <= 3:
            print("you hit a car and wrecked yours.")
            dmg = random.randint(15, 50)
            print(f"You took {dmg} damage. ")
            player.health -= dmg
            if action_num >= 3:
                print("You still have time to run. What do you do? ")
                action_num -= 1
        elif rng == 4:
            print("you hit a car and wrecked yours. You would not survive this crash")
            player.health = 0


def main():
    player.health = 100
    cop.health = 100
    crimes = ["Kidnapping", "Speeding", "Murder", "Suspended License", "Warrant"]
    player.crime = random.choice(crimes)
    cop_type = [
        "City Police",
        "State Troopers",
        "Unknown Federal Agency",
        "Sheriff's Department",
    ]
    cop.type = random.choice(cop_type)
    events = [
        "4-way",
        "stop light",
        "stop sign" "Sharp left",
        "Sharp right",
        "Spike Strip",
        "pothole",
        "road block",
        "road work",
    ]
    player.speed = 35
    cop.speed = 35
    wrecked = False
    can_turn = True
    cop.number = 1
    reverse = False
    reverse_num = 0
    action_num = 0
    action = ""

    while game(player, cop):
        game(player, cop)

        action = input("[Go] - [Speed Up] - [Slow Down] - [Info] - [Quit] ").upper()

        if action == "QUIT":
            break

        randevents = random.choice(events)

        # speed control
        if player.speed < 0:
            reverse = True
        elif player.speed >= 75:
            can_turn = False
        elif player.speed >= 100:
            print("Your car begins to shake and rattle.")
        elif player.speed >= 120:
            wrecked = True

        # Turning
        if can_turn == False:
            if action == "LEFT" or action == "RIGHT":
                print("You've rolled your car goiong to fast on a turn. ")
                player.health = 0

        # actions
        if action == "GO":
            print("You keep driving. ")
            action_num += 1
        if action == "SPEED UP":
            player.speed += 10
            print(f"Curent speed: {player.speed}")
            action_num += 1
        if action == "SLOW DOWN":
            player.speed -= 10
            print(f"Curent speed: {player.speed}")
            action_num += 1
        if action == "INFO":
            info(player, cop, action_num)
            action_num += 1
        if action == "STOP":
            break

        # reverse
        if reverse == True:
            print(
                "You're going in reverse now! if you don't fowrd soon you'll be caught. "
            )
            action_num -= 1
            reverse_num += 1

        # reverse turns
        if reverse == True:
            if reverse_num >= 3:
                print("You've backed in to a police car! You can still get away.")
                dmg = random.randint(10, 25)
                print(f"You took {dmg} damage")
                player.health -= dmg

        # wrecked
        if wrecked == True:
            print("You've wrecked your car! ")
            player.health = 0

        # action_num
        if action_num <= 0:
            print("You've been caught!")
            player.health = 0

        # event 4-way
        if randevents == "4-way":
            action = input(
                """There's a 4-way ahead. Which way do you want to go?
[Straight] - [Left] - [Right] - [quit]"""
            ).upper()
            if action == "STRAIGHT":
                straight(action, action_num)
            if action == "LEFT" or action == "RIGHT":
                if can_turn == True:
                    print("You made it! ")
                else:
                    print("You crashed!")
                    player.health = 0

        # event stop light
        if randevents == "stop light" or randevents == "stop sign":
            print(
                """There's a stop light down the road, you can't tell the color yet. What do you do? """
            )
            action = input("[Straight] - [Left] - [Right] - [Stop]").upper()
            if action == "STRAIGHT":
                straight(action, action_num)
            if action == "LEFT" or action == "RIGHT":
                if can_turn == True:
                    print("You made it! ")
                else:
                    print("You crashed!")
                    player.health = 0

        # event sharp left
        if randevents == "Sharp left":
            print("The road takes a sharp left. Can you make it?")
            if can_turn == True:
                print("You made it! ")

        # event sharp right
        if randevents == "Sharp right":
            print("The road takes a sharp left. Can you make it?")
            if can_turn == True:
                print("You made it! ")
        # event Spike Strip
        if randevents == "Spike Strip":
            print("There's a spike strip set up ahead. What do you do? ")
            action = input("[Straight] - [Try to Go Around] - [Stop]").upper()
            straight(action, action_num)
        if action == "TRY TO GO AROUND":
            rng = random.randint(1, 4)
            if rng == 1:
                print("You made it past with all your tires intact! ")
            if rng != 1:
                rng = random.randint(1, 4)
                print(f"You lost {rng} tires.")
                if action_num <= 3:
                    player.onfoot = True
                else:
                    player.health = 0
        if action == "STOP":
            player.health = 0
        # event pothole
        if randevents == "pothole":
            print("You hit a pothole! ")
            rng = random.randint(1, 4)
            if rng == 1:
                dmg = random.randint(15, 35)
                print(f"It did a number on your car. You took {dmg} damage. ")
                player.health -= dmg
            else:
                print("You got lucky this time! ")
        if action == "STOP":
            player.health = 0
        # event road block
        if randevents == "road block":
            print("There's a road block ahead! ")
            action = input("[Keep going] - [Stop]").upper()
            if action == "KEEP GOING":
                rng = random.randint(3, 4)
                if rng <= 3:
                    print("You hit several cars ")
                    dmg = random.randint(50, 100)
                    player.health -= dmg
                else:
                    print("You got lucky! ")
        if action == "STOP":
            player.health = 0
        # evnt road work
        if randevents == "road work":
            print("there's road work ahead! ")
            action = input("[Keep going] - [Stop]").upper()
            if action == "KEEP GOING":
                rng = random.randint(3, 4)
                if rng <= 3:
                    print("You hit several holes and large equipment ")
                    dmg = random.randint(50, 100)
                    player.health -= dmg
                else:
                    print("You got lucky! ")
        if action == "STOP":
            player.health = 0

    else:
        print("You Lost! ")


if __name__ == "__main__":
    main()
