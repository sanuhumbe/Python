
while(True):
        print ('Rock = 1, paper = 2, scissor = 3')
        player_1 = raw_input("Player 1: ")
        player_2 = raw_input("Player 2: ")
        Rock = "1"; paper = "2"; scissor = "3"
        val = ["1", "2", "3"]
        if player_1 in val and player_2 in val:
            if player_1 == player_2:
                print "sorry! it is a tie!"

            elif player_1 == "1" and player_2 == "2":
                print "Player 2 wins3!"

            elif player_1 == "2" and player_2 == "1":
                print "Player 1 wins!"

            elif player_1 == "1" and player_2 == "3":
                print "Player 1 wins!"

            elif player_1 == "3" and player_2 == "1":
                print "Player 2 wins"

            elif player_1 == "2" and player_2 == "3":
                print "Player 2 wins!"

            elif player_1 == "3" and player_2 == "2":
                print "Player 1 wins!"

            stop = raw_input("Do you want to stop?(Y/N): ")
            if(stop=="y"or stop=="Y"):
                break
        else:
            print("An error has occured.")        
        