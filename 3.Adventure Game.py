# My Adventure Game

import time
x = 0
dadtalk = 1
wifetalk = 1
sontalk = 1
girltalk = 1

def Game():
    print("""Welcome to the Who Ate My Cake. This is a text-only detective game.
            You are given scenarios and options, and based on the option 
            you choose, the game proceeds.\n""")

    time.sleep(x)

    print("""You are the head of your family, namely dad, and one thing you like
    the most is eating your chocolate cake, well-prepared by yourself night before,
    after the job.\n""")

    time.sleep(x)

    print("""One day, you get back from the job, excited to see love of your life,
   the chocolate cake. You open the fridge, but what is that? Your cake has no 
   chocolate left on it. Somebody not only ruined your cake, but also left it 
   in the crime scene.\n""")

    time.sleep(x)

    print("""You go crazy and decide to dedicate rest of your day trying to find the
    murderer, giving up your best activity, falling asleep on couch watching 
    television.\n""")

    time.sleep(x)

    print("""There are four suspects: Your wife, your son, your daughter and your
    dad. You look at the clock, it is 5 pm. Your children are at school from 9 to 3.
    Your wife is home all day. Your dad is also home almost all day except between 
    12 and 2, in which he meets with his friends to play some poker.\n""")

    QuestionToYourself()

def QuestionToYourself():
    time.sleep(3)
    answer = input("""Before beginning, you have to answer yourself one important 
    question: Do you really think that one of them could do such evil thing?  """)
    if(answer.lower().strip()=='yes'):
        print("Nice. Clearly, you are not a fool.")
        Interrogate()
    elif(answer.lower().strip()=='no'):
        print("\nYou are stupid enough to deserve your cake to be stolen.")
        GameOver()
    else:
        WrongAnswer()
        QuestionToYourself()

def Interrogate():
    time.sleep(3)
    answer = input("Who do you want to interrogate? ")
    if(answer.lower().strip()=='dad'):
        Dad1()
    elif(answer.lower().strip()=='wife'):
        Wife1()
    elif(answer.lower().strip()=='son'):
        Son1()
    elif(answer.lower().strip()=='daughter'):
        Daughter1()
    else:
        WrongAnswer()
        Interrogate()

def Dad1():
    if(dadtalk==1):
       choice = input("""You approach to your dad.
       A.Hey dad, did you see my cake?
       B.Hey dad, how was the game today?""")

       if(choice.lower().strip() == 'a'):
           dadtalk-=1
           print("\nYou: Hey dad, did you see my cake?")
           Dad1a()
       elif(choice.lower().strip=='b'):
           print("\nHey dad, how was the game today?")
           Dad1b()
       else:
           WrongAnswer()
           Dad1()
    else:
        print("\nYou already talked with your dad.")
        Interrogate()

def Refuse(x):
    print("Your",x.lower().strip(),"refuses to continue talking with you anymore.")

def Dad1a():
    print("\nDad: What cake? I didn't see nothing!?")
    Refuse(dad)
    Interrogate()

def Dad1b():
    print("\nDad: It's good that you asked. I beat their asses so hard I had to tell it someone.")
    choice = input("""\nIt looks like your dad is having a beatiful day. What is your next move?
    A. Oh really? As I did to you last night?
    B. You are good.""")
    if(choice.lower().strip()=='a'):
        print("You: Oh really? As I did to you last night?")
        Dad1ba()
    elif(choice.lower().strip()=='b'):
        print("You: You are good.")
        Dad1bb()
    else:
        WrongAnswer()
        Dad1b()

def Dad1ba():
    print("\nDad: It would be a shame if my son wasn't better than me. You know, humanity has to evolve somehow.")
    choice = input("""\nYou are doing pretty good. You need just a bit more to get what you came for. What next?
    A. Would you want to eat chocolate cake with me?
    B. I am tired. I wanna drink my cold beer.""")
    if(choice.lower().strip()=='a'):
        print("\nYou: Would you want to eat chocolate cake with me?")
        Dad1baa()
    elif(choice.lower().strip()=='b'):
        print("\nYou: I am tired. I wanna drink my cold beer.")
        Dad1bab()
    else:
        WrongAnswer()
        Dad1ba()

def Dad1baa():
    print("\nDad: No,thanks. I eat a lot of cookies during the game.")
    Refuse(dad)
    Interrogate()
def Dad1bab():
    print("\nDad: Let me bring your beer.")



def Dad1bb():
    print("It is good to see that you are passionate(!) about my game.")
    DadRefuse()
    Interrogate()


def Wife1():
    print()

def Son1():
    print()

def Daughter1():
    print()


def WrongAnswer():
    print("""You have comprehension skill equal to of a primary school kid's. I give you
    one more chance.""")

def GameOver():
    time.sleep(3)
    print("""\nYou couldn't find who stole your cake and die by the sorrow that surrounds 
    you.\n""")
    time.sleep(3)
    print("------------GAME OVER!!!!------------\n")
    answer = input("Do you want to try your luck once more?")
    if(answer.lower().strip()=='yes'):
        Game()
    if(answer.lower().strip()=='no'):
        print("Okay.")


Game()
