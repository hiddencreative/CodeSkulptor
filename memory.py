# implementation of card game - Memory

import simplegui
import random

# get image of the back of a playing card
image = simplegui.load_image("http://www.dreamstime.com/stock-photo-playing-card-back-side-62x90-mm-image17636780")

# define the global variables
WIDTH = 800
HEIGHT = 100
FIELDS = 16
FIELD_WIDTH = 800 // 16
NUMBER_SPACES = 50
LINE_WIDTH = 2

# helper function to initialize globals
# gets numbers in range, shuffles cards, resets state, 
def new_game():
    global numbers, exposed, state, moves
    numbers = [i % 8 for i in range(16)]
    random.shuffle(numbers)
    exposed = [False for i in range(16)]
    state = 0
    moves = 0  
    
# define event handlers
def mouseclick(pos):
    # add game state logic here
    # determines state of cards 
    global exposed, state, last_exposed, last_last_exposed, moves
    field_number = pos[0] // FIELD_WIDTH
    if not exposed[field_number]: 
        if state == 0:
            exposed[field_number] = True    
            last_last_exposed = field_number
            state = 1
        elif state == 1:
            exposed[field_number] = True
            last_exposed = field_number
            state = 2
        elif state == 2:
            exposed[field_number] = True
            if numbers[last_last_exposed] == numbers[last_exposed]:
                pass
            else:
                exposed[last_last_exposed] = False
                exposed[last_exposed] = False
            last_last_exposed = field_number
            state = 1
            moves += 1
                                               
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global moves
    for i in range(0, FIELDS - 1):
        x = (i+1) * FIELD_WIDTH
        canvas.draw_line((x, 0), (x, HEIGHT), LINE_WIDTH, "White")
    field = 0
    offset = NUMBER_SPACES / 5
    for n in numbers:
        canvas.draw_text(str(n), (offset + field * NUMBER_SPACES, 65), 42, "White")
        field += 1
    field = 0
    for n in numbers:
        if not exposed[field]:

            canvas.draw_polygon([[field * FIELD_WIDTH, 0], [(field + 1) * FIELD_WIDTH, 0], [(field + 1) * FIELD_WIDTH, HEIGHT], [field * FIELD_WIDTH, HEIGHT]], LINE_WIDTH, "White", "Green")
        field += 1
    label.set_text("Turns = " + str(moves))
    

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
