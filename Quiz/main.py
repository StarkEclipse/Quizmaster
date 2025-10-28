import pgzrun

TITLE = "Quiz Master"
WIDTH = 870
HEIGHT = 650

timeleft = 10

question_index = 0
question_count = 0
questions_file_name = "questions.txt"
questions = []

mbox1 = Rect(0, 0, 880, 80)
qbox = Rect(10, 90, 600, 160)
tbox = Rect(620, 90, 240, 160)
sbox = Rect(620, 260, 240, 380)
abox1 = Rect(10, 260, 295, 185)
abox2 = Rect(10, 460, 295, 190)
abox3 = Rect(315, 260, 295, 185)
abox4 = Rect(315, 460, 295, 190)

answerboxes = [abox1, abox2, abox3, abox4]

def draw():
    screen.clear()
    screen.draw.filled_rect(mbox1, "grey")
    screen.draw.filled_rect(qbox, "grey")
    screen.draw.filled_rect(tbox, "grey")
    screen.draw.filled_rect(sbox, "grey")
    for i in answerboxes:
        screen.draw.filled_rect(i, "white")

    screen.draw.textbox("Welcome to QuizMaster", mbox1, color = "white")
    screen.draw.textbox("Skip", sbox, color = "white", angle = -90)
    screen.draw.textbox(str(timeleft), tbox, color = "white")
    screen.draw.textbox(qu[0], qbox, color = "white")

def on_mouse_down(pos):
    pass

def update():
    move_message()

def create_question():
    global question_count, questions
    qfile = open("questions.txt", "r")
    for r in qfile:
        questions.append(r)
        question_count += 1
    qfile.close()

def read_next_question():
    global question_index
    question_index +=1
    return questions.pop(0).split(",") 

def move_message():
    mbox1.x -= 2
    if mbox1.right < 0:
        mbox1.left = WIDTH

create_question()
qu = read_next_question()


pgzrun.go()