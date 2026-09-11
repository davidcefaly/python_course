def main ():
    difficulty = input("Difficult or Casual? ")
    if not (difficulty == "Difficult" or difficulty == "Casual"):
        print ("Enter a valid difficulty")
        return

    players = input("Multiplayer or Single-player? ")
    if not (players == "Multiplayer" or players == "Single-player"):
        print ("Enter a valid number of players")
        return

    if difficulty == "Difficult" and players == "Multiplayer":
            recomend ("Poker")
    elif difficulty == "Difficult" and players == "Single-player":
        recomend ("Klondike")
    elif difficulty == "Casual" and players == "Multiplayer":
         recomend ("Hearts")
    else:
         recomend ("Clock")

        
def recomend (game):
    print ("you might like", game)


main()

