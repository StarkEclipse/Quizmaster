import pgzrun


TITLE = "Quiz Master"
WIDTH = 870
HEIGHT = 650

timeleft = 10

is_game_over = False
score = 0
question_index = 0
question_count = 0
questions_file_name = "questions.txt"
questions = []
answers = []

mbox1 = Rect(0, 0, 880, 80)
qbox = Rect(10, 90, 600, 160)
tbox = Rect(620, 90, 240, 160)
sbox = Rect(620, 260, 240, 380)
abox1 = Rect(10, 260, 295, 190)
abox2 = Rect(10, 460, 295, 180)
abox3 = Rect(315, 260, 295, 190)
abox4 = Rect(315, 460, 295, 180)

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

    index = 1
    for i in answerboxes:
        screen.draw.textbox(qu[index].strip(), i, color = "black")
        index = index + 1
        
def correct_answer():
    global score, questions, timeleft, qu
    score += 1
    if questions:
        qu = read_next_question()
        timeleft = 10
    else:
        gameover()

def gameover():
    global qu, timeleft
    qu = ["Game Over!","-","-","-","-",5]
    timeleft = 0

def on_mouse_down(pos):
    index = 1
    for i in answerboxes:
        if i.collidepoint(pos):
            if index == int(qu[5]):
                correct_answer()
            else:
                gameover()
        index += 1
    if sbox.collidepoint(pos):
        skip_question()
        
def skip_question():
    global qu, timeleft
    if questions and not is_game_over:
        qu = read_next_question()
        timeleft = 10

def update_timeleft():
    global timeleft
    if timeleft:
        timeleft -= 1
    else:
        gameover()

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

clock.schedule_interval(update_timeleft, 1)
create_question()
qu = read_next_question()


pgzrun.go()