import random

def userinput():
    a=input("Enter one letter to guess : ").lower()
    if(len(a)>1):
        print("\n")
        print("Please enter only one letter.")
        print("[ You have",count-1,"chances left. ]")
        print("-----------------------------------------------------------------")
        return userinput()
    elif(len(a)<1):
        print("Please enter atleast one letter.")
        print("[ You have",count-1,"chances left. ]")
        print("-----------------------------------------------------------------")
        return userinput()
    elif(a.isdigit()):
        print("\n")
        print("Please enter a letter not number.")
        print("[ You have",count-1,"chances left. ]")
        print("-----------------------------------------------------------------")
        return userinput()
    else:
        if(a in log):
            print("\n")
            print("This letter already used.")
            print("[ You have",count,"chances left. ]")
            print("-----------------------------------------------------------------")
            return userinput()
        else:
            return a

def markedindex(word,letter):
    temp=[]
    flag=0
    for i in word:
        flag+=1
        if(i==letter):
            temp.append(flag)
            log.append(i)
    return temp
        
    
def data(x):
    fruitData=["mango","banana","apple","cherry","grape","coconut","watermelon","orange","berry","kiwi"]
    animalData=["lion","tiger","dog","cat","elephant","horse","chicken","cow","fish","pig"]
    birdData=["parrot","crow","owl","duck","peacock","egale","pigeon","bulbul","woodpecker","bat"]
    flowerData=["rose","poppy","tulip","sunflower","lotus","lily","jasmine","dahlia","marigold"]
    if(x=="Fruits"):
        return fruitData
    elif(x=="Animal"):
        return animalData
    elif(x=="Birds"):
        return birdData
    else:
        return flowerData
    
topics=["Fruits","Animal","Birds","Flower"]
hint=random.choice(topics)
print("Guess The Word. [ Hint: Word is a name of",hint,"]")
print("-----------------------------------------------------------------")
dataset=data(hint)
word=random.choice(dataset)
n=len(word)
clock=0
result=[]
log=[]
key=0;
output=[]
for i in range(0,n):
    output.append("_")
count=n+2
while(count):
    if(clock!=n):
        letter=userinput()
        if(letter in word):
            result=markedindex(word,letter)
            p=len(result)
            for i in range(0,p):
                output[result[i]-1]=letter
                clock+=1
            for i in range(0,n):
                print(output[i],end=" ")
            print("\n")
            print("\n[ You have",count-1,"chances left. ]")
            print("-----------------------------------------------------------------")
        else:
            print(letter,"is not in the word.")
            print("\n")
            print("[ You have",count-1,"chances left. ]")
            print("-----------------------------------------------------------------")
        count -=1
        if(count==0):
            key=1
    else:
        print("\n-----------------------------------------------------------------")
        print("Congratulations! You guessed the word.")
        break
        
if(count==0 and clock!=n):
    print("\n-----------------------------------------------------------------")
    print("Sorry, All chances over. The word is ,",word,".")
elif(count==0 and key==1):
    print("\n-----------------------------------------------------------------")
    print("Congratulations! You guessed the word.")

input("Press Enter To Exit...")
    

