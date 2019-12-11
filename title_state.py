import game_framework
from pico2d import *
import main_state
import maptool
import help_state

name = "TitleState"
image_title = None
image_text = None
image_help = None
bgm = None

def enter():
    global image_title, image_text, bgm, image_help
    image_title = load_image('resourse/title.png')
    image_text = load_image('resourse/press_space_text.png')
    image_help = load_image("resourse/press_p_help.png")
    bgm = load_music('resourse/dodadag_main_bgm.mp3')
    bgm.set_volume(64)
    bgm.repeat_play()


def exit():
    global image_title, image_text, image_help
    del(image_help)
    del(image_title)
    del(image_text)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            bgm.stop()
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN,SDLK_ESCAPE) :
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(main_state)
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_h):
                game_framework.change_state(maptool)
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
                game_framework.push_state(help_state)


def draw():
    clear_canvas()
    image_title.draw(280, 300)
    image_text.draw(280,250)
    image_help.draw(280,180)
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass