import random
def game():
    print("you are playing a game:")
    score=random.randint(1,99)
    #fetch the hiscore
    with open("game.txt") as f:
        hiscore=f.read()
        if(hiscore!=""):
            hiscore=int(hiscore)
        else:
            hiscore=0
    print(f"your score is {score}")
    if(score>hiscore):
        with open("game.txt","w") as f:
            f.write(str(score))
    return score
game()
