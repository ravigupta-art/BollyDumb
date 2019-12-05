import pyglet
from pyglet.window import key

# import the random function
import random

# import the floor function
from math import floor

# open the txt file into a variable named movielist
movielist = open('MovieListComplete.txt', 'r')

# set the time on the timer
timer = False
time = 60.0

# getting the total number of movies in the list
number_of_movies = 0
for movie in movielist.readlines():
    number_of_movies += 1
movielist.close()

# open the file again to read from beginning of the file
movielist2 = open('MovieListComplete.txt', 'r')

# set the random movie
random_movie = random.randint(0, number_of_movies - 1)

window = pyglet.window.Window(1000, 720)
image = pyglet.image.SolidColorImagePattern((105, 105, 105, 255)).create_image(1000, 720)

label = pyglet.text.Label('WELCOME TO THE BOLLYWOOD DUMBCHARADES',
                          bold=True,
                          color=(10, 50, 20, 255),
                          font_name='serif',
                          font_size=20,
                          x=window.width // 2, y=window.height // 1.2,
                          anchor_x='center', anchor_y='center')

label3 = pyglet.text.Label("Press 'Esc' on keyboard to exit.",
                           font_name='san serif',
                           font_size=14,
                           x=window.width // 2, y=window.height // 2.8,
                           anchor_x='center', anchor_y='center')

label4 = pyglet.text.Label("Press 'Enter' on keyboard to generate. Press 'Enter' again to re-generate.",
                           font_name='san serif',
                           font_size=14,
                           x=window.width // 2, y=window.height // 1.4,
                           anchor_x='center', anchor_y='center')

label5 = pyglet.text.Label("Press 'Tab' to start/stop the Timer. Press 'Shift + Tab' to reset the timer.",
                           font_name='san serif',
                           font_size=14,
                           x=window.width // 2, y=window.height // 1.5,
                           anchor_x='center', anchor_y='center')
window.set_caption('BollyDumb v0.1-alpha')

@window.event
def on_draw():
    label.draw()
    label5.draw()
    label4.draw()
    label3.draw()


def update(dt):
    global timer
    global time
    global random_movie
    window.clear()
    image.blit(0, 0)
    t_label_color = (225, 237, 59, 255)
    # change the time if the timer is running
    if timer == True:
        time -= dt
    # end the timer if time is up
    if time <= 0 and timer == True:
        t_label_color = (200, 0, 0, 255)
        if timer == True:
            timer = False
            time = 0
    # set the text
    t_label = pyglet.text.Label("{:.2f}".format(time),
                                color=t_label_color,
                                font_name='san serif',
                                font_size=36,
                                x=window.width // 2, y=window.height // 1.75,
                                anchor_x='center', anchor_y='center')
    t_label.draw()

    # draw the random_movie
    movielist2 = open('MovieListComplete.txt', 'r')
    label2 = pyglet.text.Label(
            "Here is a random movie for the Dumb Charades:    " + movielist2.readlines()[random_movie],
            color=(10, 50, 20, 255),
            font_name='san serif',
            font_size=16,
            x=window.width // 2, y=window.height // 2.2,
            anchor_x='center', anchor_y='center')
    label2.draw()
    movielist2.close()
    
pyglet.clock.schedule_interval(update, 0.01)


@window.event
def on_key_press(symbol, modifiers):
    global time
    global timer
    global random_movie
    if symbol == key.ENTER:
        movielist2 = open('MovieListComplete.txt', 'r')
        random_movie = random.randint(0, number_of_movies - 1)
        print(random_movie)
    elif symbol == key.TAB:
        if modifiers & key.MOD_SHIFT:
            timer = False
            time = 60
        else:
            if time <= 0:
                time = 60
            timer = not timer
    elif symbol == key.ESCAPE:
        pyglet.app.exit()


pyglet.app.run()
movielist.close()
