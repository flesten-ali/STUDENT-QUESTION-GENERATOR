import random

print("---STD Questions Generator---")
print()
print("using this application you can manage stds and quetions")
print(" you can also select a random question for a random std")
stds=["Fatima","Taha","Aras"]
question=["what is the differance between for and while loop" , "how can you print customer error messegae for the runtime error"]
print()
print("Exixsting stds:")
ind = 1
def printStd():
    ind = 1
    for std in stds:
     print(ind, ".", std)
     ind += 1
    print()

printStd()
print("Existing questions")
def printQus():
    ind=1
    for qus in question:
        print(ind, ".", qus)
        ind += 1
    print()
printQus()
print("Choose one of the actions:")
print("A  -> Add std")
print("M  -> Move the std up in the list")
print("R  -> Remove std by name")
print("RL -> Remove the last std")
print("--------------------------------------")
print("a  -> Add question")
print("r  -> Remove question by item num")
print("rl -> Remove the last question")
print("G  -> Randomly assign question to a student")
print("Q  -> Quit the application")

def printStd():
    ind = 1
    for std in stds:
        print(ind, ".", std)
        ind += 1

while True:

    action = input("\nplease choose an action:")

    if action =="A":
        std = input("Enter the std name to be added:")
        stds.append(std)
        print("New std is added.\n")
        printStd()


    elif action == "M":
        ind = 1
        for std in stds:
            print(ind, ".", std)
            ind += 1
        item = int(input("Enter the item num to move up:"))
        if item >=1 and item <= len(stds):
            item-=1
            temp =stds[item]
            stds[item]=stds[item-1]
            stds[item-1]=temp
            print("\n New ordering:")
            printStd()

        else:print("index invalid")
    elif action=="R":

        std=input("Enter the std name to be removed:")

        if std not in stds:
          print("Std name is not exist")

        else:
            student=[]

            for s in stds:
                if s != std:
                    student.append(s)

            stds = student
            print("The std is deleted")
            printStd()


    elif action == "RL":
        stds.pop()
        printStd()

    elif action == "a":
        qus = input("Enter a new Qyestion")
        question.append(qus)
        printQus()
    elif action =="r":
        printQus()
        ind = int( input("Enter the question num to be removed:"))

        if ind >=1 and ind <=len(question):
            question.pop(ind-1)
            print("the question is deleted")
            print()
            printQus()
        else:
            print("Invalid index")


    elif action =="rl":
        print("the last quetion in the list is deleted\n")
        question.pop()
        printQus()

    elif action =="G":
        ranStd = random.choice(stds)
        ranQus = random.choice(question)
        print(ranQus,"\nis asked for",ranStd)

    else:
        print("GoodBye.")
        input("press enter to exit")
        break