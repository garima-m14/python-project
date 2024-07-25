from random import shuffle
qus=[
   ("what is the name of your country","india"),
   ("what is the name of your country","india"),
   ("what is the capital of your country","new delhi"),
   ("what is the national flower", "lotus"),
    ("what is the name of your national animal","tiger")
]
shuffle(qus)
right = 0
wrong = 0
for question, right_ans in qus:
   ans = input(question + ' ')
   if ans.lower() == right_ans:
        right +=1
   else:
     print("No the right ans is:",right_ans)
     wrong +=1

print("congratulation!")
print("you got", right,"right answer and",wrong,"wrong answer")
