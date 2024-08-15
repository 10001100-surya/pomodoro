from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = .2
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
reps = 0
timer = ""

# to pop the window on screen after some time
def bring_to_front():
    # Raise the window to the front
    window.deiconify()
    window.lift()
    # Force the window to focus
    window.focus_force()
    # Ensures the window is not minimized
    window.attributes('-topmost', True)
    window.attributes('-topmost',False)
    window.after(3000, window.iconify)


# ---------------------------- TIMER RESET ------------------------------- # 
def restart_timer():
    canvas.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    function_state.config(text="Timer")
    global reps
    reps = 0
    start_button.config(state="normal")


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    start_button.config(state="disabled")
    global reps
    reps+=1
    work = WORK_MIN*60
    short_break = SHORT_BREAK_MIN*60
    long_break = LONG_BREAK_MIN*60

    if reps % 2 == 0:
        count_down(short_break)
        function_state.config(text='break',foreground='#e7305b',font=(FONT_NAME, 35, "bold"),bg=YELLOW)
    elif reps % 8 == 0:
        count_down(long_break)
        function_state.config(text='break', foreground='#e7305b', font=(FONT_NAME, 35, "bold"), bg=YELLOW)
    else:
        count_down(work)
        function_state.config(text='Work', foreground='#9bdeac', font=(FONT_NAME, 35, "bold"), bg=YELLOW)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    min = math.floor(count/60)
    sec = math.floor(count%60)
    if min < 10:
        min = f'0{min}'
    if sec < 10:
        sec = f'0{sec}'
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
        if count < 3:
            bring_to_front()
    else:
        start_timer()
        marks = ''
        for _ in range(math.floor(reps / 2)):
            marks += "✔"
            marks_count.config(text=marks)

    canvas.itemconfig(timer_text, text=f'{min}:{sec}')



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro app")
window.config(padx=100,pady=50,bg=YELLOW)

# canvas
canvas = Canvas(width=200,height=224,highlightthickness=0, bg=YELLOW)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 100, image=tomato_image)
timer_text = canvas.create_text(100, 113, text="", font=(FONT_NAME,35,"bold"), fill="white")
canvas.grid(row=1, column=1, sticky="nswe")



# labels
function_state = Label(text="Timer",foreground='#000000',font=(FONT_NAME, 35, "bold"),bg=YELLOW)
function_state.grid(row=0, column=1, sticky="nswe")
marks_count = Label(text='',foreground='#9bdeac',font=(FONT_NAME, 16, "bold"),bg=YELLOW)
marks_count.grid(row=2, column=1, sticky="nswe")

# button click
start_button = Button(text="Start",bg='#9bdeac', width=10, command=start_timer)
start_button.grid(row=2, column=0, sticky='we')
reset_button = Button(text="Reset",bg='#808080', width=10, command=restart_timer)
reset_button.grid(row=2, column=2, sticky='we')

window.mainloop()