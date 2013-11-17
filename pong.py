# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
width = 600
height = 400       
ball_radius = 20
paddle_width = 8
paddle_height = 80
half_pad_width = paddle_width / 2
half_pad_height = paddle_height / 2
ball_pos = [width/2,height/2]
ball_vel = [-random.randrange(60, 180)/60,random.randrange(120, 240)/60]
paddle1_pos = height/2
paddle2_pos = height/2

# NOTHING TO SEE HERE !!!  (added just for fun, who notices this in here? Comment)
harmless_variable_one = False
rainbows_and_unicorns = False
please_ignore = False
inconspicuous = False

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
# def ball_init(right):
def spawn_ball(right):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [width/2,height/2]
    ball_vel[1] = -random.randrange(60, 180)/60
    if right == True:
        ball_vel[0] = random.randrange(120, 240)/60
    else:
        ball_vel[0] = -random.randrange(120, 240)/60
    pass

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are floats
    global score1, score2  # these are ints
    paddle1_pos = height/2
    paddle2_pos = height/2
    paddle1_vel = 0
    paddle2_vel = 0
    score1 = 0
    score2 = 0
    spawn_ball(0 == random.randrange(0,11) % 2)
    pass

def draw(c):
    global score1, score2, paddle1_vel, paddle2_vel, paddle1_pos, paddle2_pos, ball_pos, ball_vel
       
    # draw mid line and gutters
    c.draw_line([width / 2, 0],[width / 2, height], 1, "White")
    c.draw_line([paddle_width, 0],[paddle_width, height], 1, "White")
    c.draw_line([width - paddle_width, 0],[width - paddle_width, height], 1, "White")

    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    if ball_pos[1] >= (height - ball_radius) or ball_pos[1] <= (ball_radius):
        ball_vel[1] = -ball_vel[1]
    if ball_pos[0] <= (paddle_width + ball_radius):
        if ball_pos[1] < (paddle1_pos - half_pad_height) or ball_pos[1] > (paddle1_pos + half_pad_height):
            spawn_ball(True)
            score2 += 1
        else:
            ball_vel[0] = -ball_vel[0] * 1.1
            
    if  ball_pos[0] >= (width - paddle_width - ball_radius):
        if ball_pos[1] < (paddle2_pos - half_pad_height) or ball_pos[1] > (paddle2_pos + half_pad_height):
            spawn_ball(False)
            score1 += 1
        else:
            ball_vel[0] = -ball_vel[0] * 1.1
    # draw ball
    c.draw_circle(ball_pos, ball_radius, 2, "White", "White")

    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos < (half_pad_height) and paddle1_vel < 0:
        paddle1_vel = 0
    if paddle2_pos < (half_pad_height) and paddle2_vel < 0:
        paddle2_vel = 0
    if paddle1_pos > (height - (half_pad_height)) and paddle1_vel > 0:
        paddle1_vel = 0
    if paddle2_pos > (height - (half_pad_height)) and paddle2_vel > 0:
        paddle2_vel = 0    
    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel 
        
    # draw paddles
    c.draw_polygon([(0, paddle1_pos-half_pad_height), (0, paddle1_pos+half_pad_height), (paddle_width-2, paddle1_pos+half_pad_height),(paddle_width-2,paddle1_pos-half_pad_height)], paddle_width-1, "White","White")
    c.draw_polygon([(width, paddle2_pos-half_pad_height), (width, paddle2_pos+half_pad_height), (width-paddle_width+2, paddle2_pos+half_pad_height),(width-paddle_width+2,paddle2_pos-half_pad_height)], paddle_width-1, "White","White")

    # draw scores
    c.draw_text(str(score1), (170, 50), 36, "White")
    c.draw_text(str(score2), (400, 50), 36, "White")    
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = -4
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel = 4
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel = -4
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel = 4
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel = 0

# create frame
frame = simplegui.create_frame("Pong", width, height)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game, 100)


# start frame
new_game()
frame.start()
