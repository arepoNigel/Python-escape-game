
import cmd
import textwrap
import sys
import os
import time
import random






class player:
    def __init__(self):
        self.name = ''
        self.job= ''
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        self.location = 'b2'
        self.game_over = False
myPlayer = player()

def puzzle1():
    print("")
    print("")
    print("")

    speech5 = "The flame disperses into five turqoise wisps. The wisps illuminates on a stone podium. The stone podium contains a metal tablet. "
    speech6 = "'The answer lies in the numbers,' said a voice. Two wisps flew at the back of you and shines on a floor.\n The floor contains the same carvings as on the metal tablet.\n"
    
    
    for character in speech5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    
    for character in speech6:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    img_puzzle1()
    img_refpuzzle1()
    puzzle1_ans()

def puzzle2():
    
    speech7 = "You have successfully solved the first puzzle. You hear a crackling sound of a stone door opening. A wisp flies through the door and through the hallway. It wants you to follow it. "
    speech8 = "You start to follow the wisp. While following, the wisp's light shines through the hallway uncovering a number of painting murals honouring the fallen brothers of Humility. "
    speech9 = "The wisp stops and hovers above and enters a lamp. Bright light soon emerges from the lamp. There you see a giant diamond containing 26 plates with alphabets on it. "
    speech10 = "\nIt looks like you can remove the plates and place them in a hole between the diamond.\n\n\n"
    speech11 = "It cannot be seen, cannot be felt,\n"
    speech12 = "Cannot be heard, cannot be smelt,\n"
    speech13 = "It lies behind stars and under hills,\n"
    speech14 = "And empty holes it fills,\n"
    speech15 = "It comes first and follows after,\n"
    speech16 = "Ends life, kills laughter.\n"
    speech17 = "You hear the voices again. You try to figure out what were those about.\n"

    for character in speech7:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in speech8:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in speech9:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in speech10:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in speech11:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.09)
    for character in speech12:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.09)
    for character in speech13:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.09)
    for character in speech14:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.09)
    for character in speech15:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.09)
    for character in speech16:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.09)#10
    for character in speech17:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    
    img_puzzle2()
    puzzle2_ans()




### GAME FUNCTIONALITY
def setup_game():
    os.system('cls')

    


    #name collecting
    print("Demons are real. They lurk around the shadow lands and feed on the saddened and lost people. Demons are dangerous. They are never to be friended.")
    print("To combat the monsters, you volunteered yourself to the the Brotherhood of Humility under the companionship of Our Lady of Grieving Souls.")
    print("-- Joerburn 19:20 --")

    print("                                                       ")
    question1 = "Dear Pilgrim, what is thy name?\n"
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05) #delay
    player_name = input("> ")

          

    ###Introduction
    question3 = "Welcome, " + player_name + ".\n"
    for character in question3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05) #delay
    myPlayer.name = player_name

    speech1 = "Your journey begins in a dark cubeoid room.\n"
    speech2 = "There are no lights illuminating the room. You can hear, speak, feel, taste, smell but not see. \n"
    speech3 = "Suddenly, an orange flame appears infront of you. 'Approach the flame O pilgrim,' a voice storms in the room. \n"
    speech4 = "'QUICKLY!'You approach the flame.\n"
    
    for character in speech1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in speech2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in speech3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in speech4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)


    puzzle1()
    
    
    

def img_puzzle1():
    print("                                      Metal Tablet    ")
    print("                                   ===================")
    print("                                   |  1 1 1 1 1 1 1  |")
    print("                                   |  1 2 1 2 1 2 1  |")
    print("                                   |  1 2 1 1 1 2 1  |")
    print("                                   |  1 2 1 2 1 2 1  |")
    print("                                   |  1 1 1 1 1 2 1  |")
    print("                                   ===================")
    
def img_refpuzzle1():
    print("                                       Stone Floor    ")
    print("                                   ===================")
    print("                                   |  1 1 1 2 2 2 2  |")
    print("                                   |  1 1 1 2 2 2 2  |")
    print("                                   |  1 1 1 2 2 2 2  |")
    print("                                   |  1 1 1 2 2 2 2  |")
    print("                                   |  1 1 1 2 2 2 2  |")
    print("                                   ===================")

    print("                                   ===================")
    print("                                   |  2 2 2 1 1 2 2  |")
    print("                                   |  2 2 2 1 1 2 2  |")
    print("                                   |  2 2 2 1 1 2 2  |")
    print("                                   |  2 2 2 1 1 2 2  |")
    print("                                   |  2 2 2 1 1 2 2  |")
    print("                                   ===================")

    print("                                   ===================")
    print("                                   |  2 2 2 2 2 1 1  |")
    print("                                   |  2 2 2 2 2 1 1  |")
    print("                                   |  2 2 2 2 2 1 1  |")
    print("                                   |  2 2 2 2 2 1 1  |")
    print("                                   |  2 2 2 2 2 1 1  |")
    print("                                   ===================")

def img_puzzle2():
    print("                                      _________                ")
    print("                                     {A---Z---Y}                ")
    print("                                   {B=====1=====X}             ")
    print("                                 {C=======1=======W}      ")
    print("                                {D========1=========V}    ")
    print("                              {E==========1==========U}           ")
    print("                             {F===========1===========T}          ")
    print("                             {G====| ||  ||  ||  |====S}     ")
    print("                             {H====**=====1=====**====R}         ")
    print("                             {I===*==*====1====*==*===Q}  ")
    print("                              {J==*==*====1====*==*==P}        ")
    print("                               {K==**=====1=====**==O}             ")
    print("                                |L++++++++M++++++++N|   ")






def puzzle1_ans():
    quesPuzzle1 = "\nSolve this puzzle and you may leave this room...\n"
    for character in quesPuzzle1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)

    realAns1 = ["zero three seven", "037"]
    while True:
        try:
            ans1 = str(input("==> "))
            if ans1 in realAns1:
                print("You have successfully passed the stone and metal puzzle.")
                os.system('cls')
                puzzle2()
                break
            else:
                raise Exception
        except Exception:
            print("The answer is wrong, try again or forfeit this game!")
    

def puzzle2_ans():
    quesPuzzle2 = "\nSolve the riddle and you may leave this room...\n"
    for character in quesPuzzle2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)

    ans2 = str(input("==> "))
    if ans2.lower() == ("dark"):
        print("You have successfully passed the riddle puzzle.")
        print("To be continued...") 
    while ans2.lower() not in ["dark"]:
        print("The answer is wrong, try again or forfeit this game! ")
        ans2 =str(input("==> "))    
        if ans2.lower() == ("dark"):
            print("You have successfully passed the riddle puzzle.")
            print("To be continued...")    
    
    
def help_menu():
    print("                      ========================================================                                             ")
    print("                                      LUSTRATION (GAMEPLAY)                                                                    ")
    print("                      ========================================================                                             ") 
    print('              -Each puzzle you face has numbered questions,-\n sometimes they would be riddles.             ')
    print('              - Type your answers to unlock a new room.    -                                                ')
    print('               -If you cannot think of the answer, come back again - \n while you have an idea.-                ')
    print("               - Some riddles have answers that have 2 digits but it's best to answer the riddle as-\n in '86' not '086'. ")
    print('                           -Good Luck and Have Fun-                                                                 ')
    
    title_screen()

    
def title_screen():
    print("================================================================================================================================================================================")
    print("  [][]        [][]         [][]   [][][][][][][][]   [][][][][][][][]   [][][][][][][]         [][][][][][]     [][][][][][][][]   [][]   [][][][][][][][]   [][][][       ][]  ")
    print("  [][]        [][]         [][]   [][][][][][][][]   [][][][][][][][]   [][][][][][][][]     [][][][][][][][]   [][][][][][][][]   [][]   [][][][][][][][]   [][][][][     ][]  ")
    print("  [][]        [][]         [][]   ][][][                   [][]         [][]        [][][]   [][]        [][]         [][]         [][]   [][]        [][]   [][]   [][]   ][]  ")
    print("  [][]        [][]         [][]   [][][][][][][][]         [][]         [][]        [][][]   [][]        [][]         [][]         [][]   [][]        [][]   [][]    [][]  ][]  ")
    print("  [][]         [][]       [][]              [][][]         [][]         [][][][][][][][]     [][][][][][][][]         [][]         [][]   [][]        [][]   [][]     [][] ][]  ")
    print("  [][][][][]     [][][][][][]     [][][][][][][][]         [][]         [][]   [][]          [][]        [][]         [][]         [][]   [][][][][][][][]   [][]      [][]][]  ")
    print("  [][][][][]       [][][][]       [][][][][][][][]         [][]         [][]     [][]        [][]        [][]         [][]         [][]   [][][][][][][][]   [][]       [][][]  ")
    print("================================================================================================================================================================================")
    print('                                                                                              >Play                               ')
    print('                                                                                              >Load                               ')
    print('                                                                                              >Help                               ')
    print('                                                                                              >Quit                               ')
    print('                                                                                       Copyright 2019 Arepo                       ')
    option = input("==> ")
    if option.lower() ==  ("play"):
        setup_game()
    elif option.lower() == ("load"):
        pass
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in ["play", "help", "load", "quit"]:
        print("Enter a valid command please type again.")
        option =input("==> ")
        if option.lower() ==  ("play"):
            setup_game()
        elif option.lower() == ("load"):
            pass
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("quit"):
            sys.exit()


title_screen()




