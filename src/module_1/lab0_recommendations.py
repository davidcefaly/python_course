def main ():
    difficulty = input("Difficult or Casual? ")
    players = input("Multiplayer or Single-player? ")

    if difficulty == "Difficult":
        if players == "Multiplayer":
            recomend ("Poker")
        elif players == "Single-player":
           recomend ("Klondike")
        else:
            print("Enter a valid number of players")
            
    elif difficulty == "Casual":
        if players == "Multiplayer":
            recomend ("Hearts")
        elif players == "Single-player":
           recomend ("Clock")
        else:
            print("Enter a valid number of players")
        
    else:
        print ("Enter a valid difficulty")
      

def recomend (game):
    print ("You might like", game)


main()
