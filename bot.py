def bot():
######-----------------------BRAIN--------------------------------########
    import random
    import os
    import sys
    
    lookup={"your age":"i am a week old","cyborg":"i am a bot created by MrVang..","your name":"my name is Cyborg, MrVang created me a week ago","mrvang":"MrVang is anonymous"}
    
    if sys.platform[:5] == 'linux':
        os.mkdir('/storage/sdcard0/Cyborg')
        os.chdir('/storage/sdcard0/Cyborg')
    elif sys.platform[:3] == 'win':
        os.mkdir('C:\/Users\/USER\/Documents\/Cyborg')
        os.chdir('C:\/Users\/USER\Documents\/Cyborg')
    file=open("botMemory.txt","a")
    file=open("botMemory.txt","r")
    try:
        print("loading memories...")
        while True:
            filedoc=next(file)
            filedoc=filedoc.split("&|&")
            filedoc2={filedoc[0]:filedoc[1]}
            lookup.update(filedoc2)
    except StopIteration:
        print("all memories loaded!")
    file.close()
    
    visitorName=input("Welcome what is your name : ")
    if visitorName == "MrVang" or visitorName == "mrvang" or visitorName == "vang" or visitorName == "Vang":
        print("Hi BOSS, wlcome MrVang hope you\'re doing well today!\n")
    else:
        print("Hi %s , i\'m Cyborg created by MrVang, welcome...\n" %(visitorName))
    
#######-------------------FUNCTIONS------------------------------#########
    def quize():
        i=0
        score=0
        highlight=1
        print("✴✴✴ quiz! quiz! math quiz!™ ✴✴✴")
        while i<5:
            num1=random.randrange(1,50)
            num2=random.randrange(1,50)
            question={"%s + %s"%(num1,num2):num1+num2,"%s - %s"%(num1,num2):num1-num2,"%s * %s"%(num1,num2):num1*num2,"%s / %s"%(num1,num2):num1//num2}
            ques=random.choice(list(question.items()))
            quize,ans=ques
            ans=str(ans)
            print("( ",highlight," )         "+quize+"          ")
            answer=input("please enter your answer :  ")
            if answer.isspace()==True:
                print("\n you left it blank.. wrong!\n")
                i+=1
                score+=0
            elif answer==ans:
                print("\n you got it right\n")
                i+=1
                score+=10
            else:
                print("\n wrong!, try to work it right next time...\n The answer is :%s\n"%(ans))
                i+=1
                score+=0
            highlight+=1
        print("you score %d out of 50 \n Bye bye from quiz \n"%(score))
    
    
    def addMemory():
        keyword=input("Please enter the keyword : ")
        description=input("Please enter the keword description : ")
        memory={keyword:description}
        innerMemory=keyword+"&|&"+description
        print("Do you want to add %s to memory?"%(keyword))
        answ=input(" input yes or no  : ")
        if "yes" in answ:
            lookup.update(memory)
            file=open("botMemory.txt","a+")
            botMemory=(innerMemory+"\n")
            file.write(botMemory)
            file.close()
            print("succesfully added to memory : %s"%(keyword))
        else:
            print("Thanks for fooling me!")
    
    def displayMemory():
        print("make statement with the followings : \n",list(lookup.keys()))
    
    def displayFunction():
        print("Here are my Functions : [display functions, display memory, add to memory, credit card pin, math quiz, quit]")
    def ccpinloader():
        import random
        x=str(input("\nDo you have any suggestion? \n if No leave it blank, if yes, \n Enter your suggestion :"))
        z=list(str(random.randrange(10)**4))
        y=0
        if (x.isspace() is True) or len(x)==0:
            while y<4:
                print(random.randrange(10),random.randrange(10),random.randrange(10),random.randrange(10))
                y+=1
        elif len(x)==1:
            x=list(str(x))
            x.extend(z[0:3])
            while y<4:
                print(random.choice(x),random.choice(x),random.choice(x),random.choice(x))
                y+=1
        elif len(x)==2:
            x=list(str(x))
            x.extend(z[0:2])
            while y<4:
                print(random.choice(x),random.choice(x),random.choice(x),random.choice(x))
                y+=1
        elif len(x)==3:
            x=list(str(x))
            x.extend(z[0])
            while y<4:
                print(random.choice(x),random.choice(x),random.choice(x),random.choice(x))
                y+=1
        elif len(x)==4:
            x=list(x)
            while y<4:
                print(random.choice(x),random.choice(x),random.choice(x),random.choice(x))
                y+=1
        elif len(x)>=5:
            print("Suggestion must be lesser than or equal to 4 string")
            ccpinloader()
        else:
            print("Good Bye  @Vang")
        print("Good Bye from MrVang \n Remember it is your luck! , i have tried my best...")
    
###-------------------QUESTIONARE------------------------------###########
    print("help: type one of the following to execute!")
    displayFunction()
    while True:
        def questionare():
            randQue=["How may i help you?", "What can i do for you?", "Oya hit me!", "Any question of the day?", "Don't you like asking me a question?", "Please just a question!"]
            question=input(random.choice(randQue)+"\n")#define input question
            
            for name in lookup.keys():
                if name in question:
                    print("\n++ "+lookup[name]+"\n")
                    questionare()
                elif "add to memory" == question:
                    addMemory()
                    questionare()
                elif "display memory" == question:
                    displayMemory()
                    questionare()
                elif "display functions" == question:
                    displayFunction()
                    questionare()
                elif "math quiz" == question:
                    quize()
                    questionare()
                elif "credit card pin" == question:
                    print("%s, Here what i can do for you!"%(visitorName))
                    ccpinloader()
                    questionare()
                elif question=="quit" or question=="exit": #exiting bot
                    boolean=input("are you sure you want to exit? ")
                    if boolean == "yes":
                        print("Thank you %s, have a nice day!"%(visitorName))
                        quit()
                    else:
                        print("ask me a question %s, don\'t be shy!" %(visitorName))
                    questionare()# goes back to questionare
            else:
                print("i don\'t know what you\'re talking about (%s), it\'s not registered in me!"%(question))
                addup=input("Or do you want to brief me what it is? : ")
                if "yes" in addup:
                    addMemory()
                    questionare()
                else:
                    print("i think that question is not relevant")
                questionare()
        questionare()

bot()