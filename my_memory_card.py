#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel)
from random import shuffle
 
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
 
ql = [] 
ql.append(Question('государственный язык Бразилии', 'португальский', 'английский', 'испанский', 'бразильский'))
ql.append(Question('какого цвета нет на флаге России?', 'зелёный', 'красный', 'белый', 'синий'))
ql.append(Question('национальная хижина якутов', 'ураса', 'юрта', 'иглу', 'хата'))
 
app = QApplication([])
 
btn_OK = QPushButton('ответить')
lb_Question = QLabel('самый сложный вопрос в мире!')
 
RadioGroupBox = QGroupBox("варианты ответов") 
rbtn_1 = QRadioButton('вариант 1')
rbtn_2 = QRadioButton('вариант 2')
rbtn_3 = QRadioButton('вариант 3')
rbtn_4 = QRadioButton('вариант 4')
 
RadioGroup = QButtonGroup() 
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
 
lans1 = QHBoxLayout()   
lans2 = QVBoxLayout() 
lans3 = QVBoxLayout()
lans2.addWidget(rbtn_1) 
lans2.addWidget(rbtn_2)
lans3.addWidget(rbtn_3) 
lans3.addWidget(rbtn_4)
 
lans1.addLayout(lans2)
lans1.addLayout(lans3) 
 
RadioGroupBox.setLayout(lans1) 
 
AnsGroupBox = QGroupBox("результат теста")
lb_Result = QLabel('прав ты или нет?') 
lb_Correct = QLabel('ответ будет тут!') 
 
lres = QVBoxLayout()
lres.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
lres.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(lres)
 
lline1 = QHBoxLayout() 
lline2 = QHBoxLayout() 
lline3 = QHBoxLayout()
 
lline1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
lline2.addWidget(RadioGroupBox)   
lline2.addWidget(AnsGroupBox)  
AnsGroupBox.hide()
 
lline3.addStretch(1)
lline3.addWidget(btn_OK, stretch=2) 
lline3.addStretch(1)
 
lcard = QVBoxLayout()
 
lcard.addLayout(lline1, stretch=2)
lcard.addLayout(lline2, stretch=8)
lcard.addStretch(1)
lcard.addLayout(lline3, stretch=1)
lcard.addStretch(1)
lcard.setSpacing(5) 
def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('следующий вопрос')
 
def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('ответить')
    RadioGroup.setExclusive(False) 
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)
 
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
 
def ask(q: Question):
    shuffle(answers) 
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question) 
    lb_Correct.setText(q.right_answer)
    show_question()
 
def show_correct(res):
    lb_Result.setText(res)
    show_result()
 
def check_answer():
    if answers[0].isChecked():
        show_correct('правильно!')
        window.score += 1
        print("статистика\n - всего вопросов ", widow.total, "\n - правильных ответов", window.score)
        print("рейтинг: ", window.score/window/total*100, "%")
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('неверно!')
            print("рейтинг: ", window.score/window/total*100, "%")
 
def next_question():
    window.cur_question = window.cur_question + 1
    if window.cur_question >= len(ql):
        window.cur_question = 0
    q = ql[window.cur_question]
    ask(q)
 
def click_OK():
    if btn_OK.text() == 'ответить':
        check_answer()
    else:
        next_question()
 
window = QWidget()
window.setLayout(lcard)
window.setWindowTitle('memo card')
window.cur_question = -1   

btn_OK.clicked.connect(click_OK)
 
next_question()
window.resize(400, 300)
window.show()
app.exec()
