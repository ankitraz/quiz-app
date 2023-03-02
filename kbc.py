import random

def greet(name):
    print("Hello", name.capitalize())


def play():
    questions = ['''What is the capital of India?''',
                ''' What is the full form of CAD in computer graphics?''',
                '''Who is the manufacturer of iphone smartphone?''', 
                '''Which programming language is often used for machine learning and artificial intelligence?''']
    answers = ["New Delhi", "Computer Aided Design", "Apple", "Python"]


    answer_index = question_index = random.randrange(len(questions)-1)

    print("Q. " ,questions[question_index])
    user_ans = (input("Type you ans: "))
    
    if user_ans.title() != answers[answer_index]:
        print("Wrong answer!")
        user_inp = input("Do you want to know the answer? ")
        if user_inp.title() == "Yes":
            print(answers[answer_index])
    else:
        print("Yes that's the write answer! you won 1000$ ")



name = input("Enter your name: ")
greet(name)
play()


while(True):
    print("Do you want to play again?")
    inp = input()
    if inp != "yes":
        print("Thanks for playing.")
        break
    play()

