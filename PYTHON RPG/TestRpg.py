import os
def title_screen():
    os.system("cls")
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
    elif option.lower == ("load"):
        pass
    elif option.lower == ("help"):
        help_menu()
    elif option.lower == ("quit"):
        sys.exit()
    while option.lower() not in ["play", "help", "load", "quit"]:
        print("Enter a valid command please type again.")
        option =input("==> ")
        if option.lower() ==  ("play"):
            setup_game()
        elif option.lower == ("load"):
            pass
        elif option.lower == ("help"):
            help_menu()
        elif option.lower == ("quit"):
            sys.exit()






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

title_screen()