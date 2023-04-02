# Quiz App

# Question sınıfı
#   Instance Attributes
#       - text (soru), choices (şıklar), answer (cevap)
#   Instance Methods
#       checkAnswer methodu ile cevap kontrolü
#       - q1.checkAnswer('cevap') => True or False

import random
class Question:
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer
    
    def checkAnswer(self,answer):
        if answer not in self.choices:
            pass
        return self.answer == answer

class Quiz:
    def __init__(self,questions):
        self.questions = random.sample(questions, len(questions)) #random.sample komutu questionları random şekilde getirir.
        self.questionIndex = 0 # ilk sorudan başlayıp artacaktı ama yukarıda random yaptığımız için rastgele gelir.
        self.score = 0 #score tutmak için en başta sıfır doğru diyeceğiz her bir doğruda bir arttıracağız
    def getQuestion(self):
        return self.questions[self.questionIndex]
    
    def displayQuestion(self):
        question = self.getQuestion()

        print(f"Soru {self.questionIndex + 1}: {question.text}")
        for q in question.choices:
            print("-" + q)
# Bu aşamaya kadar kullanıcıya soruları gösterdik. Şimdi bir cevap almamız ve kontrol etmemiz lazım

        answer = input("Cevap: ")
        if (question.checkAnswer(answer)):
            self.score += 1 #cevap doğru ise score'u bir artır.
            print("TEBRİKLER")
        self.questionIndex += 1 #bir sonraki soruya geçmesi için indexi bir artırdık
        self.loadQuestion() # loadQuestion'u çağırıyorum ki sonraki soruyu getirsin.
# self.question kaç soru var?
# self.questionIndex kaçıncı sorudayız?

    def loadQuestion(self): # Soruyu yükler. BAŞLANGIÇ
        if len(self.questions) == self.questionIndex: # Eğer son soruya geldiysek scoru yazar yoksa sonraki soruya geçmek için aşağıdaki kodu çalıştırır.
            self.displayScore()
        else:
            self.displayProgress()
            self.displayQuestion()

    def displayScore(self): #score'u gösterek olan def
        print("Quiz Özetiniz".center(80,"*"))
        puan = 100 / len(self.questions)
        toplamPuan =round(self.score * puan)
        print(f"Toplam {len(self.questions)} sorunun {self.score} tanesini bildiniz.")
        print("Kazandığınız Puan: ",toplamPuan) 

    def displayProgress(self): # ilerlemeyi gösterecek olan def
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex +1

        print(f"Toplam {totalQuestion} sorunun {questionNumber}. sorusundasınız.".center(80,'*'))   # Toplam 80 karakter işgal etsin kalanı *'la doldursun.

q1 = Question("en iyi programlama dili hangisidir?", ["python","c#","java","dart"],"python")
q2 = Question("en popüler programlama dili hangisidir?", ["python","c#","dart","java"],"python")
q3 = Question("en çok kazandıran programlama dili hangisidir?", ["python","java","c#","dart"],"python")
q4 = Question("en renkli programlama dili hangisidir?", ["python","java","c#","dart"],"python")
q5 = Question("en sevilen programlama dili hangisidir?", ["python","java","c#","dart"],"python")

sorular = [q1,q2,q3,q4,q5]

quiz = Quiz(sorular)
print(quiz.getQuestion().text) #Index numarasını her seferinde bir artıracağız.

quiz.loadQuestion()
# sonuc = q1.checkAnswer('python')
# print(sonuc)

# Quiz sınıfı
#   Instance Attributes
#       - questions, questionIndex, score
#   Instance Methods
#       - getQuestion()     => questionIndex'e göre question nesnesi getirir.
#       - displayQuestion() => getQuestion() ile alınan nesneyi getirir.
#       - displayScore()    => Score bilgisini gösterir.
#       - displayProgress   => Testteki ilerlemeyi gösterir. (5 sorunun 2.sorusundasınız.)




