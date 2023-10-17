import tkinter as tk
from tkinter import messagebox,Toplevel
import numpy as np
import math


BTN_PLACEMENT_Y = 250
BTN_PLACEMENT_X = 40
BTN_WIDTH = 10
BTN_HEIGHT = 1



class Ball:

    def __init__(self,x,y,speed_x,speed_y, radius, color) -> None:
        self.x = x
        self.y = y
        self.x_speed = speed_x
        self.y_speed = speed_y
        self.radius = radius
        self.color = color
        self.area = math.pi * math.pow(self.radius,2)

    def move(self):

        # moving the ball
        self.x += self.x_speed
        self.y += self.y_speed
    

        # checking for collisions against the boarders
        if self.x + self.radius >= 600 or self.x - self.radius <= 0:
            self.x_speed = - self.x_speed
        
        if self.y + self.radius >= 900 or self.y - self.radius <= 0:
            self.y_speed = - self.y_speed
        
    def draw(self, canvas):
        canvas.create_oval(self.x - self.radius, self.y - self.radius,
                          self.x + self.radius, self.y + self.radius, 
                          fill=self.color, outline='black')
    
    def ball_collides_with(self, other):
        distance = math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
        return distance < (self.radius + other.radius)



def stop_btn_clicked():
    global stop
    global is_running
    stop = True
    is_running = False



def show_non_blocking_message_box():
    
    dialog = Toplevel(root)

    label = tk.Label(dialog, text="Want to retry or cancel?")
    label.pack(padx=20, pady=10)

    ok_button = tk.Button(dialog, text="OK", command=on_ok)
    ok_button.pack(side="left", padx=5, pady=20)

    cancel_button = tk.Button(dialog, text="Cancel", command=on_cancel)
    cancel_button.pack(side="right", padx=5, pady=20)


def refresh():
    
    if not stop:

        canvas.delete('all')

        for ball in tot_balls:
            ball.move()
            ball.draw(canvas)

        check_collision()    

        # if len(tot_balls) <= 1:
        #     #show_non_blocking_message_box()
        #     return

        root.after(speed_of_sim,refresh)
    



def reset():
    global stop
    if stop:
        canvas.delete('all')
        stop = False


def check_collision():
    
    for i, ball_a in enumerate(tot_balls):
        for j, ball_b in enumerate(tot_balls):
            if i != j and ball_a.ball_collides_with(ball_b):
                if ball_a.area > ball_b.area:
                    new_radius = math.sqrt((ball_a.area + ball_b.area) / math.pi)
                    ball_a.radius = new_radius
                    ball_a.area = ball_a.area + ball_b.area
                    tot_balls.pop(j)
                else:
                    
                    new_radius = math.sqrt((ball_a.area + ball_b.area) / math.pi)
                    ball_b.radius = new_radius
                    ball_b.area = ball_a.area + ball_b.area
                    tot_balls.pop(i)
    return



def start_btn_clicked():
    global tot_balls
    global stop
    global is_running
    if not is_running:
        tot_balls = []
    
    if not stop and not is_running:
        try:
            tot_num_balls = int(txt_numb.get())
            global  speed_of_sim
            speed_of_sim = int(txt_speed_of_sim.get())
            a = 1
        except ValueError:
            messagebox.showwarning(title="Invalid Input")

        
        for _ in range(tot_num_balls):
            tot_balls.append(Ball(np.random.uniform(70, 530),
                                np.random.uniform(70, 830),
                                np.random.uniform(-5,5),
                                np.random.uniform(-5,5),
                                np.random.uniform(3,20),
                                color='green'))
        
        is_running = True
        refresh()
    else:
        return
    



#region Tkinter setup

# Root, frames
root = tk.Tk()
root.title("Ball Game")
root.geometry('800x900')
root.resizable(False,False)
input_frame = tk.Frame(root,width=200,height=900)
global canvas 
canvas = tk.Canvas(root, width=600, height=900, background='darkgray')

######## Widget creation ############
# Buttons
start_btn = tk.Button(input_frame, text= 'Start', width=BTN_WIDTH, height=BTN_HEIGHT, command=start_btn_clicked)
exit_btn = tk.Button(input_frame, text= 'Exit', width=BTN_WIDTH, height=BTN_HEIGHT,foreground='red', command=root.destroy)
stop_btn = tk.Button(input_frame, text= 'Stop', width=BTN_WIDTH, height= BTN_HEIGHT, command=stop_btn_clicked)
reset_btn = tk.Button(input_frame, text='Reset', width=BTN_WIDTH, height= BTN_HEIGHT, command=reset)

# txtbox
txt_numb = tk.Entry(input_frame, width=13)
txt_speed_of_sim = tk.Entry(input_frame, width=13)

# labels
lbl_numb = tk.Label(input_frame, text='Number:')
lbl_speed_of_sim = tk.Label(input_frame, text='speed:')



###### Placement #######
#Frames
canvas.pack(side='left')
input_frame.pack(side='right')
        
# Buttons
start_btn.place(x=BTN_PLACEMENT_X, y=BTN_PLACEMENT_Y - 90)
stop_btn.place(x=BTN_PLACEMENT_X, y=BTN_PLACEMENT_Y - 60)
reset_btn.place(x=BTN_PLACEMENT_X, y=BTN_PLACEMENT_Y - 30)
exit_btn.place(x=BTN_PLACEMENT_X, y=BTN_PLACEMENT_Y)


# input boxes
txt_numb.place(x=70, y=50)
lbl_numb.place(x=10,y=52)

txt_speed_of_sim.place(x=70, y=90)
lbl_speed_of_sim.place(x=15, y=92)
  
#endregion



#if len(TOT_BALLS) == 1:
#    show_non_blocking_message_box() 

stop = False
is_running = False

root.mainloop()



        
