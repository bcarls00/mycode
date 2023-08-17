#!/usr/bin/python3

import html


trivia= {
         "category": "Entertainment: Film",
         "type": "multiple",
         "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
         "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
         "incorrect_answers": [
             "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
             "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
             "&quot;Round up the usual suspects.&quot;"
            ]
        }

print(f"Welcome to the game. Today your question will come from the category {trivia.get('category')}. The question type is {trivia.get('type')} choice. Here is your question!")

question = html.unescape(trivia["question"])

correct = html.unescape(trivia["correct_answer"])

incorrect1 = html.unescape(trivia["incorrect_answers"][0])

incorrect2 = html.unescape(trivia["incorrect_answers"][1])

incorrect3 = html.unescape(trivia["incorrect_answers"][2])

print(question, "\n", correct, "(1)\n", incorrect1, "(2)\n", incorrect2, "(3)\n", incorrect3, "(4)")

a = input("Answer 1 -4:")

if a == "1":
    print("CORRECT!!")
else:
    print("NOPE!!")
