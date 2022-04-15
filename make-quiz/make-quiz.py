# Question
class Question:
  def __init__(self, text, choices, answer):
    self.text = text
    self.choices = choices
    self.answer = answer
  
  def checkAnswer(self, answer):
    return self.answer == answer
  
# Quiz  
class Quiz:
  def __init__(self, questions):
    self.questions = questions
    self.score = 0
    self.questionIndex = 0
  
  def getQuestion(self):
    return self.questions[self.questionIndex]

  def displayQuestion(self):
    question = self.getQuestion()
    print(f'Question {self.questionIndex + 1}: {question.text}')

    for q in question.choices:
      print('-'+q)
    
    answer = input('Your answer:')
    self.guess(answer)
    self.loadQuestion()
  
  def guess(self, answer):
    question = self.getQuestion()
    
    if question.checkAnswer(answer):
      self.score += 1
    self.questionIndex += 1
  
  def loadQuestion(self):
    if len(self.questions)== self.questionIndex:
      self.showScore()
    else:
      self.displayProgress()
      self.displayQuestion()
  
  def showScore(self):
    print("Score:", self.score)
  
  def displayProgress(self):
    total_question = len(self.questions)
    question_number = self.questionIndex + 1

    if question_number > total_question:
      print('Quiz is over.')
    else:
      print(f'Question {question_number} of {total_question}'.center(100, "*"))

question_1 = Question('What is the best programming language?', ['Javascript', 'Python', 'C#', 'Java', 'Go'],'Python')
question_2 = Question('What is the most popular programming language?', ['Python', 'Go','C#', 'Java', 'Javascript'],'Python')
question_3 = Question('What is the most profitable programming language?', ['Go', 'Python', 'C#','Javascript' 'Java'],'Python')
questions = [question_1, question_2, question_3]

quiz = Quiz(questions)
quiz.loadQuestion()
