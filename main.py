def town_storyline():
    print("As you enter town, a young man runs up to you screaming for help. You ask him what's wrong and he "
          "tells you that his family is trapped in a mine and that no one else will help him. What do you do?")
    question2a = input("a. Help the man\nb. Continue to sell your illegal goods\n")

    if question2a == 'a':
        mine_searching()

    if question2a == 'b':
        print("You decline helping the man and continue towards a shady alleyway to sell your illegal goods. Two men"
              "are in the alleyway, each offering to buy your goods. One has a robotic eye, and the other has a mask"
              "over his face. Who do you sell to?")
        question3a = input("a. Masked man\nb. Man with a robotic eye\n")

        if question3a == 'a':
            print("The masked man doesn't have enough money, so he asks for you to follow him back to his trailer."
                  "On your way, you end up entering an alley with a group of mutants at the end. You turn around, "
                  "only to realize that there are mutants on each side of the alley. You're trapped!")
            killed_by_mutants()

        if question3a == 'b':
            killed_by_cop()


def mutant_base_storyline():
    print("You begin to head south. After an hour, you reach the mutants' base. You peer inside the darkness "
          "and are starting to think this might have been a bad plan when a group of mutants jump out of the"
          "dark and attack you. What do you do?")
    question2b = input("a. Hold back and shoot from a distance\nb. Charge!\n")

    if question2b == 'a':
        print("You shoot at the mutants, backing up as you do so. You trip over a rock, scratching your leg"
              "as you go down, leaving blood on the ground. The charging mutants stop at the blood in the "
              "ground, trying to dig for more. You have a moment of safety, leaving you to decide what to do"
              "next. What do you do?")
        question3a = input("a. Keep killing off the mutants\nb. Run back to town\n")

        if question3a == 'a':
            print("You continue shooting until your clip runs out. You still have your knife to fight with though.")
            killed_by_mutants()

        if question3a == 'b':
            town_storyline()

    if question2b == 'b':
        killed_by_mutants()


def killed_by_mutants():
    print("You run into the crowd of mutants, stabbing them as you get close. Quickly, the mutants are able to "
          "overpower you and they surround you. They begin tearing at your flesh, eating you. As you die, you "
          "wonder what fate you would have met if you had made different choices...\nGAME OVER")


def killed_by_cop():
    print("It's a cop! Before you can plead your case, he pulls out a pistol and shoots you straight between the eyes."
          "\nGAME OVER")


def killed_by_mine():
    print("You peer into the black hole trying to see if there is anyone inside. As you lean over, your foot slips on"
          "a rock and you tumble into the mine. You fall hundreds of feet before hitting the ground and dying.\n"
          "GAME OVER")


def doctor_storyline():
    print("As you enter town, a young man runs up to you screaming for help. You ask him what's wrong and he "
          "tells you that his family is trapped in a mine and that no one else will help him. What do you do?")
    question2a = input("a. Help the man\nb. Continue to the doctor\n")

    if question2a == 'a':
        mine_searching()

    if question2a == 'b':
        print("You decline helping the man and continue towards the doctor's office in town, which is actually"
              "a rusted out trailer. He has to knock you out, and tells you that he can either do it with a "
              "sedative that will cost you all of your money or he can just hit you over the head. What do "
              "you choose?")
        question3a = input("a. Pay for the sedative\nb. Get hit over the head\n")

        if question3a == 'a':
            print("You give the doctor all of your money and he knocks you out. Unbeknownst to you, the doctor has "
                  "gambling debt and is paying it off by selling organs in the black market. He puts you under and"
                  "harvests your organs. You never wake up.\nGAME OVER")

        if question3a == 'b':
            print("The doctor hits you over the head with a crowbar and you black out."
                  "Unbeknownst to you, the doctor has gambling debt and is paying it off by selling organs in the "
                  "black market. He puts you under and harvests your organs. Then he steals all of your money. "
                  "You never wake up.\nGAME OVER")


def mine_searching():
    print("You decide to help the man. He hands you a flashlight and tells you to head northeast. You ask"
          "for further directions, but he is too flustered to remember more than that. You walk northeast"
          "for several hours without finding the mine and it begins to become dark. What do you do?")
    question3a = input("a. Spend the night\nb. Leave now\n")

    if question3a == 'a':
        print("You fall asleep outside in a field. When you wake up, you are surrounded by a crowd of mutants. The "
              "only way out is to fight.")
        killed_by_mutants()

    if question3a == 'b':
        print("You continue walking until you stumble across a hole that looks like the mine the man described.")
        killed_by_mine()


print("The year is 2137, a century since the nuclear-virus wiped out civilization as we know it, Leaving behind "
      "zombie-like creatures called 'mutants'. Make your choices carefully, or you could end up dead,"
      " or worse, a mutant!")
print("You are scavenging the ruins of a gas station when a mutant jumps out at you. You are holding a laser-knife "
      "and a machine-shotgun. What do you do?")
question1 = input("a. Stab the mutant\nb. Run away from the mutant\n")

if question1 == 'a':
    print("You lunge forward and stab the mutant in the chest, but the mutant continues to charge you. Before you "
          "can react, it bites you in the shoulder. You are able to then kill the mutant, but now you have the "
          "virus and will become a mutant in a matter of hours. What do you do?")
    question1a = input("a. Seek treatment in town\nb. Get revenge on the mutants\n")

    if question1a == 'a':
        doctor_storyline()

    if question1a == 'b':
        mutant_base_storyline()

if question1 == 'b':
    print("You scream and begin to run towards town. You're halfway back when you realize that you left a good "
          "portion of your supplies back at the gas station. What do you do?")
    question1b = input("a. Track down the mutant\nb. Go back to town anyway\n")

    if question1b == 'a':
        mutant_base_storyline()

    if question1b == 'b':
        town_storyline()




