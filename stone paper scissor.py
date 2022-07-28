
import random #the computer selects random outcomes
def gameWin(comp,you): #function computer and you
    
    if comp==you: #if the outcomes of computer and u match it will be a tie
        return None # match tie
    elif comp =='s': #if computer chooses stone
        if you == 'x': #if we choose scissor
            return False #computer wins so the function is false coz it is GameWin
        elif you=='p': #if we are paper        
            return True #and comp= stone we win so it is true 
    
    elif comp =='p': #if comp=paper
        if you == 's': #and we are stone
            return False #so we loose so false
        elif you=='x': #if we are scissor
            return True #we win so this is true
    
    elif comp =='x': #if comp= scissor
        if you == 'p': #we are paper
            return False #we will loose
        elif you=='s': #and if we are stone
            return True # we will beat scissor sio true

print("Computer Turn: Stone(s) Paper(p) or Scissor(x)?") #the options that are available are stone as(s),paper as(p),and scissor as (x)
randNo=random.randint(1,3) # we set the comp to take 1 no out of 3 at random
if randNo == 1: #if at random computer chooses 1
    comp='s' # this is equivalent to stone 

elif randNo == 2: #if at random computer chooses 2
    comp= 'p'  # this is equivalent to paper

elif randNo == 3:   #if at random computer chooses 3
    comp='x'   # this is equivalent to scissor

you =input("Your Turn: Stone(s) Paper(p) or Scissor(x)?")
a = gameWin(comp, you)

print(f"Computer chose {comp}")
print(f"You chose {you}")

if a==None:
    print("Game tie")

elif a:
    print("You Win")

else:
    print("You loose")

