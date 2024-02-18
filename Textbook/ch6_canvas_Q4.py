import random

def main():
    numOfGames = int(input("please enter the number of games to be simulated: "))
    playerAdeck = list(range(1,numOfGames + 1))
    playerBdeck = list(range(1,numOfGames + 1))
    playerAwins,playerBwins,ties = dualDiceSimulator(playerAdeck,playerBdeck)
    print(f"The number of games that were simulated are: {numOfGames}")
    print(f"The number of games that were tied are: {ties}")
    print(f"The number of games that Player A won are: {playerAwins}")
    print(f"The number of games that Player B won are: {playerBwins}")



def dualDiceSimulator(playerAdeck,playerBdeck):
    scoreA = 0
    scoreB = 0
    ties = 0
    while playerAdeck != []:
        playerAcard = random.choice(playerAdeck)
        playerBcard = random.choice(playerBdeck)
        if playerAcard == playerBcard:
            playerAdeck.remove(playerAcard)
            playerBdeck.remove(playerBcard)
            ties +=1
        else: 
            if playerAcard > playerBcard:
                scoreA +=1
                playerAdeck.remove(playerAcard)
                playerBdeck.remove(playerBcard)
            else: 
                scoreB +=1
                playerAdeck.remove(playerAcard)
                playerBdeck.remove(playerBcard)
    return scoreA,scoreB,ties

if __name__ == "__main__":
    main()
   