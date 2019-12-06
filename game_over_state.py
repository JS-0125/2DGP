import game_framework
from pico2d import *
import game_world
import title_state

name = "GameOverState"
gameover = None
bgm = None

def enter():
    global gameover, bgm
    gameover = load_image('resourse/game_over.png')
    bgm = load_music('resourse/fail.mp3')
    bgm.set_volume(64)
    bgm.repeat_play()

def exit():
    global gameover, bgm
    del(gameover)
    bgm.stop()
    del(bgm)
    game_world.clear()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN,SDLK_ESCAPE) :
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(title_state)


def draw():
    clear_canvas()
    gameover.draw(280, 450)

    update_canvas()

def update():
    pass

def pause():
    pass

def resume():
    pass