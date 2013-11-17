# template for "Stopwatch: The Game"

import simplegui

# define global variables
# global variables for each frame of time

tenths = 0
on_second = 0
starts_count = 0
stops_count = 0
minutes = 0
seconds = 0
s = 0
t = 0
status = 0
interval = 100

# define helper function format that converts integer
# counting tenths of seconds into formatted string A:BC.D
# this variable provided by template -- building on it

def format(t):
    minutes = str(tenths//600)
    t = str(tenths % 10)
    seconds = tenths//10
    s = str(seconds % 60)
    if seconds < 10:
        s = "0"+str(tenths//10)      
    else:
        seconds = str(tenths//10)
    return minutes+":"+s+"."+t

# define event handlers for buttons; "Start", "Stop", "Reset"
# define start timer

def start_timer():
    global starts_count,status
    if status == 0:
        starts_count += 1
        status = 1
        timer.start()

# define stop timer

def stop_timer():
    global stops_count,status,on_second
    if status == 1:
        status = 0
        stops_count += 1
        timer.stop()
        if tenths % 10 == 0:
            on_second +=1

# define reset timer

def reset_timer():
    global minutes, seconds, status, t, tenths, starts_count,stops_count,on_second
    minutes = 0
    seconds = 0
    t = 0
    on_second = 0
    starts_count = 0
    stops_count = 0
    tenths = 0
    status = 0
    timer.stop()

# define event handler for timer with 0.1 sec interval

def tick():
    global tenths
    tenths += 1

# define where objects are drawn on the canvas

def draw(canvas):
    canvas.draw_text(format(t), [65,105], 30, "White")
    canvas.draw_text(str(stops_count), [170, 20], 18, "White")
    canvas.draw_text("/", [162,20], 18, "White")
    canvas.draw_text(str(on_second), [150, 20], 18, "White")

# create frame

frame = simplegui.create_frame("Stopwatch", 200, 200)

# register event handlers

start_button = frame.add_button("Start", start_timer)
stop_button = frame.add_button("Stop", stop_timer)
reset_button = frame.add_button("Reset", reset_timer)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(interval, tick)

# start timer and frame

frame.start()


