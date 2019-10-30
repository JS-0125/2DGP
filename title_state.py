import game_framework
from pico2d import *
import main_state


name = "TitleState"
image_title = None
image_text = None

def enter():
    global image_title, image_text
    image_title = load_image('title.png')
    image_text = load_image('press_space_text.png')


def exit():
    global image_title, image_text
    del(image_title)
    del(image_text)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN,SDLK_ESCAPE) :
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(main_state)


def draw():
    clear_canvas()
    image_title.draw(280, 300)
    image_text.draw(280,300)
    update_canvas()

def update():
    pass


def pause():
    pass


def resume():
    pass