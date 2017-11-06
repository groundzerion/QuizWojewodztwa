import random

stolice = {'lodzkiego':'Lodz','wielkopolskiego':'Poznan','kujawsko-pomorskiego':'Bydgoszcz','zachodnipomorskiego':'Szczecin','pomorskiego':'Gdansk','warminsko-mazurskiego':'Olsztyn','lubuskiego':'Gorzow Wielkopolski','lubelskiego':'Lublin','podkarpackiego':'Rzeszow','podlaskiego':'Bialystok','swietokrzyskiego':'Kielce','slaskiego':'Katowice','dolnoslaskiegogo':'Wroclaw','malopolskiego':'Krakow','mazowieckiego':'Warszawa','opolskiego':'Opole'}

#print(len(stolice))

for quizNum in range(10):
    quizFile = open('quiz_numer_%s.txt' % (quizNum+1), 'w')
    answerFile = open('answer_file_numer_%s.txt' %(quizNum+1), 'w')

    quizFile.write(' '*20 + 'QUIZ WOJEWODZTW NUMER %s \n\n'%(quizNum+1))
    quizFile.write('Imie:\n\nData:\n\nRocznik:\n\n')

    wojewodztwa = list(stolice.keys())
    random.shuffle(wojewodztwa)

    for questionNum in range(16):
        correctAnswer = stolice[wojewodztwa[questionNum]]
        wrongAnswers = list(stolice.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOption = wrongAnswers + [correctAnswer]
        random.shuffle(answerOption)

        #zapisanie pytania i proponowanych odpowiedzi do pliku
        quizFile.write('%s. Jakie miasto jest stolica wojewodztwa %s?\n' %(questionNum +1, wojewodztwa[questionNum]))

        for i in range(4):
            quizFile.write('%s. %s\n'%('ABCD'[i], answerOption[i]))
        quizFile.write('\n')

        #zapisanie poprawnej odpowiedzi do pliku AnswerFile
        answerFile.write('%s. %s\n' % (questionNum+1, 'ABCD'[answerOption.index(correctAnswer)]))


    quizFile.close()
    answerFile.close()








