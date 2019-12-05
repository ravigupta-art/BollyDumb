import pyglet
from pyglet.window import key

# import the random function
import random

# import the floor function
from math import floor

# open the txt file into a variable named movielist
movielist = open('MovieListComplete.txt', 'r')
timer = False
time = 60

# getting the total number of movies in the list
number_of_movies = 0
for movie in movielist.readlines():
    number_of_movies += 1
movielist.close()

# open the file again to read from beginning of the file
movielist2 = open('MovieListComplete.txt', 'r')

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

label4 = pyglet.text.Label("Press 'Enter' on keyboard to generate. Press 'Enter' again to re-generate.\nPress 'Tab' to start/pause the Timer. Press 'Shift + Tab' to reset the timer. ",
                           font_name='san serif',
                           font_size=14,
                           x=window.width // 2, y=window.height // 1.4,
                           anchor_x='center', anchor_y='center')

t_label = pyglet.text.Label("1:00.0",
                            font_name='san serif',
                            font_size=14,
                            x=window.width // 2, y=window.height // 1.4,
                            anchor_x='center', anchor_y='center')
window.set_caption('BollyDumb v0.1-alpha')

@window.event
def on_draw():
    label.draw()
    label4.draw()
    label3.draw()
    t_label.draw()


def update(dt):
    t_label_color = (225, 237, 59, 255)
    if timer == True:
        time -= dt
    if time <= 0 and timer == True:
        timer = False
        time = 0
        t_label_color = (200, 0, 0, 255)
    t_label = pyglet.text.Label("{}:{:02.1d}".format(floor(time/60),time%60),
                                color=t_label_color
                                font_name='san serif',
                                font_size=18,
                                x=window.width // 2, y=window.height // 1.6,
                                anchor_x='center', anchor_y='center')
    t_label.draw()
    
pyglet.clock.schedule_interval(update, 0.1)


@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.ENTER:
        window.clear()
        image.blit(0, 0)
        movielist2 = open('MovieListComplete.txt', 'r')
        random_movie = random.randint(0, number_of_movies - 1)
        print(random_movie)
        label2 = pyglet.text.Label(
            "Here is a random movie for the Dumb Charades:    " + movielist2.readlines()[random_movie],
            color=(10, 50, 20, 255),
            font_name='san serif',
            font_size=16,
            x=window.width // 2, y=window.height // 2.2,
            anchor_x='center', anchor_y='center')
        label2.draw()
        movielist2.close()
    elif symbol == key.TAB:
        if modifiers & MOD_SHIFT:
            time = 60
        else:
            if time <= 0:
                time = 60
            timer = not timer
    elif symbol == key.ESCAPE:
        pyglet.app.exit()


pyglet.app.run()
movielist.close()
