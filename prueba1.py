import random

#The game
game = []
while True:    
    print ("Welcome to my casino!")
    player = random.randint (2, 26)
    dealer = random.randint (2, 26)

    #Game
    while True:
        print ("The player got: ", player, "The dealer got: ", dealer)
        do_you_want_more_cards = input ("Do you want more cards? S/N ")
        if do_you_want_more_cards == "S":
            player = player + random.randint (1, 13)
        else:
            if player == 21 or (player > dealer and player < 21) or (player < 21 and dealer > 21):
                print ("The player won")
                game.append ("Player")
                break
            elif player == dealer:
                print ("The dealer won")
                game.append ("Dealer")
                break
            else:
                print ("The dealer won")
                game.append ("Dealer")
                break
    ask_to_end_the_game = input ("Do you want to finish the game? S/N ")
    if ask_to_end_the_game == "S":
        break
    else:
        print ("\n"*20)
print (game)