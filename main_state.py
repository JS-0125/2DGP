from pico2d import *

import game_world
import game_framework
import shop_state
import game_over_state
import maptool
import crystal_keyboard

from character import Chatacter
from character import CoillidMonsterState
from grass import Grass
from Life import Life
from inventory import Inventory

name = "MainState"

PIXEL_PER_METER = (10.0 / 0.2)
FALL_SPEED_KMPH = 25.0
FALL_SPEED_MPM = (FALL_SPEED_KMPH * 1000.0 / 60.0)
FALL_SPEED_MPS = (FALL_SPEED_MPM / 60.0)
FALL_SPEED_PPS = (FALL_SPEED_MPS * PIXEL_PER_METER)


character = None
grass = None
monster1 = None
tile1 = None
life = None
crystal = None
inventory = None
count = 0


def enter():
    global character, grass, monster1, tile1, life, crystal, inventory, count
    count += 1
    character = Chatacter()
    grass = Grass()

    life = Life()
    if count == 1:
        inventory = Inventory()

    game_world.add_object(character, 1)
    game_world.add_object(grass, 0)
    game_world.add_object(life, 1)

    maptool.ReadPos()

    tile1 = maptool.tiles
    game_world.add_objects(tile1, 0)

    crystal = maptool.tri_obses
    game_world.add_objects(crystal, 2)

    monster1 = maptool.monsters
    game_world.add_objects(monster1, 3)


def exit():
    tile1.clear()
    crystal.clear()
    monster1.clear()
    game_world.clear()


def handle_events():
    global crystal, character
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_s:
            for crystal_tmp in crystal:
                if collide(crystal_tmp, character):
                    game_world.remove_object(crystal_tmp)
                    crystal.remove(crystal_tmp)
                    game_framework.push_state(crystal_keyboard)
                    break
        else:
            character.handle_event(event)


def update():
    global monster1, character, tile1

    if life.count == 0:
        game_framework.change_state(game_over_state)

    TileCollide()

    if character.y <= 100:
        delay(1)
        game_framework.change_state(shop_state)

    for monster in monster1:
        if collide(monster, character):
            life.stop()
            character.frameX = 6
            character.frameY = 1
            character.cur_state = CoillidMonsterState
            break

    for game_object in game_world.all_objects():
        game_object.update()


def TileCollide():
    global tile1, character, monster1
    for tile in tile1:
        if collide(tile, character):
            grass.delY = 0
            for tile_tmp in tile1:
                tile_tmp.delY = 0
                character.stop()
            break
        else:
            if (character.y <= 400):
                if grass.y <= -700:
                    character.dirY = -(FALL_SPEED_PPS * game_framework.frame_time)
                    grass.delY = 0
                else:
                    character.dirY = 0.01
                    grass.delY = -(FALL_SPEED_PPS * game_framework.frame_time)
                    for tile_tmp in tile1:
                        tile_tmp.delY = (FALL_SPEED_PPS * game_framework.frame_time)
            else:
                character.dirY = -(FALL_SPEED_PPS * game_framework.frame_time)
                grass.delY = 0
                for tile_tmp in tile1:
                    tile_tmp.delY = (FALL_SPEED_PPS * game_framework.frame_time)

    for tile in tile1:
        if collide_tile_side(tile, character):
            if character.dir == 1:
                character.dir = 0
                character.x = tile.x - 80
            elif character.dir == -1:
                character.dir = 0
                character.x = tile.x + 80

    for monster in monster1:
        for tile in tile1:
            if collide(tile, monster):
                monster.delY = 0
                break
            else:
                monster.delY = -(FALL_SPEED_PPS * game_framework.frame_time)

    for monster in monster1:
        for tile in tile1:
            if collide_tile_side(tile, monster):
                if monster.monsterDelX > 0:
                    monster.x = tile.x - 80
                    monster.monsterDelX = -1

                elif monster.monsterDelX < 0:
                    monster.x = tile.x + 80
                    monster.monsterDelX = 1



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


def collide_tile_side(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb_tile_side()
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