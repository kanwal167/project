#the quiz program is a simple user that asks the user a series of question and keeps track of their score...
#list of questions and answers 
questions =[{"question":"what is the syntax of define the function?","answer":"def name():"},
            {"question":"what stands for oop in python?","answer":"object oriented program"},
            {"question":"what you mean by dunder in python?","answer":"double underscore"},
            {"question":"the process to solve the error what we called in python?","answer":"debugging"}
            ]
score=0
for question in questions:
    user_answer=input(question["question"] +"")
    if user_answer.lower()==question["answer"].lower():
        
        print("correct")
        score+=1
    else:
        print("incorrect,the correct answer is" + question["answer"])
print("your final score is"+str(score)+"/"+str(len(questions)))
