# implementation of card game - Memory

import simplegui
import random

WIDTH = 800 // 16
HEIGHT = 100 * 0.7
OFFSET = 10
turns = 0

# helper function to initialize globals
def new_game():
    global deck, exposed, state, turns, card1, card2
    list1 = range(8)
    list2 = range(8)
    exposed = [False] * 16
    state = 0
    turns = 0
    card1 = []
    card2 = []
    
    deck = list1 + list2
    random.shuffle(deck)
    label.set_text("Turns = 0")
    
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global deck, exposed, state, turns, card1, card2
    
    #flips the card over to expose the card value
    index = pos[0]/50
    
    if state == 0: 
        exposed[index] = True
        card1 = [deck[index], index]
        state = 1
    if not exposed[index]:
        if state == 1:
            exposed[index] = True
            card2 = [deck[index], index]
            state = 2
            turns += 1
            label.set_text("Turns = " + str(turns))
        elif state == 2:
            if card1[0] != card2[0]:
                exposed[card1[1]] = False
                exposed[card2[1]] = False
        
            exposed[index] = True
            card1 = [deck[index], index]
            state = 1
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global deck, exposed, turns
    
    count = 0
    for num in deck:
        canvas.draw_text(str(num), 
                         ((WIDTH * count) + OFFSET, HEIGHT), 
                         70, "White")
        if not exposed[count]:
            canvas.draw_line(((WIDTH * count + 25), 2), 
                             ((WIDTH * count + 25), 98), 
                             45, 'Green')
        count += 1      

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = " + str(turns))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric