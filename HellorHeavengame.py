print('''
88                                                                    
88                                                                    
88                                                                    
88,dPPYba,   ,adPPYba, ,adPPYYba, 8b       d8  ,adPPYba, 8b,dPPYba,   
88P'    "8a a8P_____88 ""     `Y8 `8b     d8' a8P_____88 88P'   `"8a  
88       88 8PP""""""" ,adPPPPP88  `8b   d8'  8PP""""""" 88       88  
88       88 "8b,   ,aa 88,    ,88   `8b,d8'   "8b,   ,aa 88       88  heaven
88       88  `"Ybbd8"' `"8bbdP"Y8     "8"      `"Ybbd8"' 88       88  
''')
print("Welcome to your choose of Heaven or Hell.")
print("Your mission is to find Jesus and go to heaven.")
choice1 = input('You\'re at a crossroad, where do you want to go? '
                'Type "heaven" or "hell".\n').lower()

if choice1 == "heaven":
    choice2 = input('You\'ve come to a crossroads and must choose to pick up your cross and follow Jesus. '
                    'There is forgiveness and love. '
                    'Type "wait" to tell Jesus I am not ready, there is still things I want to do on earth. '
                    'Type "Yes" I\'m ready to die to self .\n').lower()
    if choice2 == "wait":
        choice3 = input("You arrive back to your normal life unharmed. "
                        "However, you have a choice. sin and turn away from Christ, "
                        "turn away and accept Jesus as your lord and savior or commit to being a good person. "
                        "Which do you choose?\n").lower()
        if choice3 == "sin":
            print("Satan takes you and you go to Hell. Game Over")
        elif choice3 == "accept":
            print("You will enter the kingdom of heaven. You Win!")
        elif choice3 == "good person":
            print("Failed to accept Christ is the only key to heaven. Game Over.")
        else:
            print("You chose anything else. Game Over.")
    else:
        print("You have put your faith in Jesus Christ and can enter heaven. You win!.")

else:
    print("You live a satisfying life on earth but when you die you are thrown into the lake of fire. Game Over!")
