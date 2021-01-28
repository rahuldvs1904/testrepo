"""
import random
def roll(sides):
    sides=6
    num_roll=random.randint(1,sides)
    return num_roll
def main():
    sides=6
    rolling=True
    while rolling:
        roll_now=input("Press Enter to roll or q to quit: ")
        if roll_now.lower()!="q":
            num_roll=roll(sides)
            print("You rolled a ",num_roll)
        else:
            rolling = False
    print("Done")
main()





import random
def validate(s):
    if s.isdigit() and 1<=int(s)<=100:
        return True
    else:
        return False
def main():
    number = random.randint(1,100)
    guessed_num = False
    num_of_g=0
    guess = input("Enter a number betwenn 1 and 100: ")
    while not guessed_num:
        if not validate(guess):
            guess=input("Enter the required output and try again")
            continue
        else:
            guess=int(guess)
            num_of_g+=1

        if guess<number:
            guess=input("num low...try again")
        elif guess>number:
            guess=input("num high...try again")
        else:
            print("You got in",num_of_g,"guesses")
            guessed_num=True
main()




import random
def roll(sides):
    sides = 6
    roll_num = random.randint(1,sides)
    return roll_num
def main():
    s1=0
    sides=6
    s2=0
    rolling = True
    
    while rolling:
        if s1>=100 or s2>=100:
            if s1>s2:
                print("Player 1 wins, score: ",s1)
                break
            else:
                print("Player 2 wins, score: ",s2)
                break
        else:
            s1+=roll(sides)
            
            s2+=roll(sides)
      
    print("Game over")
main()






import random
import matplotlib.pyplot as plt
def roll(sides=6):
    sides=6
    roll_num = random.randint(1,sides)
    return roll_num
 
a=[]
c={1:0,2:0,3:0,4:0,5:0,6:0}
sides=6
for i in range(1000):
    a.append(roll(sides))
print(a)
for j in a:
  c[j]+=1
print(c)

b=['1','2','3','4','5','6']
plt.bar(b,c.values())
plt.show()




import random
def validate(s):
    if s.isdigit() and (int(s)>=1 and int(s)<=100):
        return True
    else:
        return False

def main():
    #guessed_num = False
    a = random.randint(1,100)
    print(a)
    num_g = input("Enter a number between 1 and 100: ")
    while True:
        
        if validate(num_g):
                         
            if int(num_g) == a:
                print("Correct prediction")
                #guessed_num = True
                break
                
            else:
                if int(num_g)>a:
                    num_g=input("Number predicted is high. Try again")
                    
                    
                elif int(num_g)<a:
                    num_g=input("Number predicted is low. Try again")
        else:
            num_g=input("Please enter the Correct input")

main()




import random
def validate(s):
    if s.isalpha():
        return True
    else:
        return False
words_list = ['ant','best','triumphant','predict','lower','ferocious','analyze','oblivion','imagine','device','ranch']
chances = 7
word_select = words_list[random.randint(0,len(words_list)-1)]
blanks=[]
print(word_select)
for i in range(len(word_select)):
    blanks.append('_')
print(blanks)
h = True
if chances==0:
    print("Sorry, You lost the game")
else:
    guess_letter = input("Guess a letter: ")
    while h:
        if validate(guess_letter):

            if guess_letter in word_select:
                blanks[word_select.find(guess_letter)] = guess_letter
                print(blanks)
                guess_letter = input("It's a hit. go again ")

            elif '_' not in blanks:
                print("Congratulations! You win")
                h=False
                break
            
            else:
                guess_letter=input("Wrong guess. Try again ")
                chances=chances-1

        else:
            guess_letter=input("Enter Correct input")

"""


'''
total_students = int(input())
    name = input()
    score = float(input())
    all_scores=[]
    
    
    for i in range(total_students):
        
        all_scores.append([name,score])
    
    all_scores.sort(key=lambda x:x[1])
    all_scores.sort(key = lambda x:x[0])
    #print(all_scores)
    
    if all_scores[0][1]==all_scores[1][1]:
        print(all_scores[0][0])
        print(all_scores[1][0])
    else:
        print(all_scores[0][0])

'''

n = int(input())
for i in range(n):
    name,number = input().split("  ")
    print(name)
    print(number)