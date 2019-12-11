import game_framework
from pico2d import *
import title_state

name = "HelpState"
image_help = None

def enter():
    global image_help
    image_help = load_image("resourse/help.png")
    title_state.draw()


def exit():
    global image_help
    del(image_help)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            title_state.bgm.stop()
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN,SDLK_ESCAPE) :
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
                game_framework.pop_state()


def draw():
    image_help.draw(280,400)
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass