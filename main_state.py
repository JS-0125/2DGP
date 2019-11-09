from pico2d import *

import game_world
import game_framework
import shop_state
import game_over_state
import maptool
import crystal_keyboard

from character import Chatacter
from grass import Grass
from monster1 import Enemy
from Life import Life

name = "MainState"

character = None
grass = None
monster1 = None
tile1 = None
life = None
crystal = None

def enter():
    global character, grass, monster1, tile1, life, crystal
    character = Chatacter()
    grass = Grass()
    monster1 = Enemy()
    life= Life()

    game_world.add_object(character, 1)
    game_world.add_object(monster1, 1)
    game_world.add_object(grass, 0)
    game_world.add_object(life, 1)


    maptool.ReadPos()

    tile1 = maptool.tiles
    game_world.add_objects(tile1, 0)

    crystal = maptool.tri_obses
    game_world.add_objects(crystal,1)

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
    TileCollide()

    if character.y <= 100:
        delay(1)
        game_framework.change_state(shop_state)

    if collide(monster1, character):
        life.stop()
        for i in [0,0,0,1,1,1,2,2,2,3,3,3,4,4,4,4,4,4,4,4,4,4]:
            character.collide_monster(i)
            draw()
        if life.count == 0:
            game_framework.change_state(game_over_state)

    for crystal_tmp in crystal:
        if collide(crystal_tmp, character):
            game_world.remove_object(crystal_tmp)
            crystal.remove(crystal_tmp)
            game_framework.push_state(crystal_keyboard)
            break

    for game_object in game_world.all_objects():
        game_object.update()



def TileCollide():
    for tile in tile1:
        if collide(tile, character):
            grass.delY = 0
            for tile_tmp in tile1:
                tile_tmp.delY = 0
            if tile.y - grass.y - 47.5 < character.y - 80:
                character.stop()
            else:
                if character.dir == 1:
                    character.dir = 0
                    character.x = tile.x - 80
                elif character.dir == -1:
                    character.dir = 0
                    character.x = tile.x + 80
            break
        else:
            if (character.y <= 400):
                if grass.y <= -700:
                    character.dirY = -8
                    grass.delY = 0
                else:
                    character.dirY = 0.01
                    grass.delY = -8
                    for tile_tmp in tile1:
                        tile_tmp.delY = 8
            else:
                character.dirY = -8
                grass.delY = -8
                for tile_tmp in tile1:
                    tile_tmp.delY = 8

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

def pause():
    pass

def resume():
    pass