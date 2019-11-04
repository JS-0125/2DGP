from pico2d import *

import game_world
import game_framework
import shop_state
import game_over_state

from character import Chatacter
from grass import Grass
from Tile_1 import Tile
from Tile_2 import Tile_2
from monster1 import Enemy
from Life import Life

name = "MainState"

character = None
grass = None
monster1 = None
tile1 = None
tile2 = None
life = None

def enter():
    global character, grass, monster1, tile1, tile2, life
    character = Chatacter()
    grass = Grass()
    monster1 = Enemy()
    life= Life()

    game_world.add_object(character, 1)
    game_world.add_object(monster1, 1)
    game_world.add_object(grass, 0)
    game_world.add_object(life,1)

    xpos = [139.5, 139.5, 139.5, 234.5, 234.5, 234.5, 234.5, 234.5, 329.5, 329.5, 329.5, 329.5, 424, 424, 424, 424]
    ypos = [1500, 1000, 900, 1500, 1000, 1000, 500, 1000, 1500, 900, 500, 200, 1200, 900, 500, 200]
    tile1 = [Tile() for i in range(0,16)]
    for i in range(16):
        tile1[i].x = xpos[i]
        tile1[i].y = ypos[i]
    game_world.add_objects(tile1, 1)

    xpos = [139.5, 139.5, 139.5,234.5,0,0,0,0,0,0,0,0,0,0,0,0]
    ypos = [200, 500,400,200,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000]
    tile2 = [Tile_2() for i in range(0,16)]
    for i in range(16):
        tile2[i].x = xpos[i]
        tile2[i].y = ypos[i]
    game_world.add_objects(tile2, 1)


def exit():
    game_world.clear()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            character.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()

    for tile in tile1:
        if collide(tile, character):
            if tile.y - 42.5 < character.y - 80:
                character.stop()
            else:
                character.x = tile.x - 50
            break
        else:
            character.dirY = -8

    for tile in tile2:
        if collide(tile, character):
            character.stop()
            break

    if character.y <= 100:
        delay(1)
        game_framework.change_state(shop_state)

    if collide(monster1, character):
        life.count -= 1
        if life.count == 0:
            game_framework.change_state(game_over_state)

def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()
    delay(0.02)

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True