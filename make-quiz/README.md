# make_quiz
Quiz sample where you can add as many questions as you want. ( for beginners) <br/>
Classes:
-
"Question" class :
--
Methods

In __init__ method
It contains text, choices and answer attributes.

"text" attribute is where the questions are written
"choices" attribute is where the options are written
"answer" attribute is correct answers of the questions

In checkAnswer method
It returns the correct answer.


"Quiz" class  :
--
Methods:

In __init__ method
It contains questions, score and questionIndex attributes.

In getQuestion method
It returns the question.

In displayQuestion method
It's calling getQuestion method and printing index of the question and question.
It displays choices via for loop and shows the answer.

In guess method
If you give correct answer, you'll get +1 points.
It increases the index of the question so that you can answer other questions.

In showScore method
It'll show your total score.

In displayProgress method
It'll show you were in which question.
