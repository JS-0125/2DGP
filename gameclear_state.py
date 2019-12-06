import game_framework
from pico2d import *
import game_world
import title_state
import shop_state

PIXEL_PER_METER = (10.0 / 0.2)
FALL_SPEED_KMPH = 1
FALL_SPEED_MPM = (FALL_SPEED_KMPH * 1000.0 / 60.0)
FALL_SPEED_MPS = (FALL_SPEED_MPM / 60.0)
FALL_SPEED_PPS = (FALL_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 1
ACTION_PER_TIME = 0.5 / TIME_PER_ACTION
FRAMES_PER_ACTION = 17
name = "GameClearState"
game_clear = None
congratulations = None
frame = None

def enter():
    global game_clear, congratulations, frame
    frame = 0
    game_clear = load_image('resourse/game_clear.png')
    congratulations = load_image('resourse/congratulations.png')

def exit():
    global game_clear, congratulations, frame
    del(congratulations)
    del(game_clear)
    del(frame)
    game_world.clear()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            title_state.bgm.stop()
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN,SDLK_ESCAPE) :
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(shop_state)


def draw():
    global frame, game_clear, congratulations

    clear_canvas()
    game_clear.draw(280, 450)
    congratulations.clip_draw(int(frame) * 398, 0, 398, 198, 280, 400, 560, 800)
    update_canvas()

def update():
    global frame
    frame = (frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 17

def pause():
    pass

def resume():
    pass