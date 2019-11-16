import game_framework
from pico2d import *
import game_world
import main_state
import shop_state


name = "IventoryState"
font = None


def enter():
    global font
    shop_state.draw()
    font = load_font('ENCR10B.TTF', 16)


def exit():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN,SDLK_ESCAPE) :
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_a):
                game_framework.pop_state()
            elif event.type == SDL_MOUSEMOTION:
                x, y = event.x, 800 - 1 - event.y
            elif event.type == SDL_MOUSEBUTTONDOWN:
                x, y = event.x, 800 - 1 - event.y
                main_state.inventory.click(x, y)


def draw():
    main_state.inventory.draw()
    font.draw(80, 600, 'main_state.inventory.money', (255, 255, 0))
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass

