from tkinter import *
import math

PINK = "#e2979c"
RED = '#e7305b'
GREEN = '#9bdeac'
YELLOW = '#f7f5dd'
FONT_NAME = 'Courier'
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = '✔'
REPS = 0
timer = None


def reset_timer():
    window.after_cancel(timer)
    timer_show.config(text='Timer', fg=GREEN, font=(FONT_NAME, 40, 'bold'), bg=PINK)
    canvas.itemconfig(timer_text, text='00:00')
    check.config(text='')
    global REPS
    REPS = 0
def start_count_down():
    global REPS
    REPS +=1
    if REPS%8 == 0:
        long_break = LONG_BREAK_MIN * 60
        count_down(long_break)
        timer_show.config(text='LongBreak Time',fg=RED,font=(FONT_NAME, 40, 'bold'),bg=PINK)
    elif REPS%2 == 0:
        short_break =  SHORT_BREAK_MIN * 60
        count_down(short_break)
        timer_show.config(text='Break Time', fg=RED, font=(FONT_NAME, 40, 'bold'), bg=PINK)
    else:
        work_sec = 10
        count_down(work_sec)
        timer_show.config(text='Work Time', fg=GREEN, font=(FONT_NAME, 40, 'bold'), bg=PINK)


def count_down(count):
    count_sec = count % 60
    count_min = math.floor(count/60)

    if count_sec < 10:
        count_sec = '0'+ f'{count_sec}'
    canvas.itemconfig(timer_text,text=f'{count_min}:{count_sec}')
    if count>0:
        global timer
        timer = window.after(1000,count_down,count-1)
    else:
        start_count_down()
        mark = ''
        work_session = math.floor(REPS/2)
        for _ in range(work_session):
            mark += CHECKMARK
        check.config(text=mark, fg=GREEN, font=(FONT_NAME, 40, 'bold'), bg=PINK)



window = Tk()
window.title('your loom')
window.minsize(width=500,height=500)
window.config(pady=10,padx=10,bg=PINK)


#label
timer_show = Label()
timer_show.config(text='Timer',fg=GREEN,font=(FONT_NAME, 40, 'bold'),bg=PINK)
timer_show.grid(row=0,column=1)


check = Label()
check.config(fg=GREEN,font=(FONT_NAME, 40, 'bold'),bg=PINK)
check.grid(row=2,column=1)


#button
start = Button()
start.config(text='Start',fg=RED,font=(FONT_NAME, 10, 'bold'),bg=YELLOW,highlightthickness=0,command = start_count_down)
start.grid(row=2,column=0)

reset = Button()
reset.config(text='Reset',fg=RED,font=(FONT_NAME, 10, 'bold'),bg=YELLOW,highlightthickness=0,command = reset_timer)
reset.grid(row=2,column=2)

#canvas
canvas = Canvas(width=500,height=500,bg=PINK, highlightthickness=0)
img = PhotoImage(file='b8fa8f291632f8fe68842e4fb100d8e0-square-rectangle-shape.png')
canvas.create_image(250,240,image=img)
timer_text = canvas.create_text(250,220,text='00:00',font=(FONT_NAME, 85, 'bold'))
canvas.grid(row=1,column=1)



window.mainloop()
