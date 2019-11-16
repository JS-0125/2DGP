import game_framework
import pico2d

import start_state
import title_state
import main_state

pico2d.open_canvas(560, 800, 576)

game_framework.run(start_state)

pico2d.close_canvas()