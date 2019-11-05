import game_framework
import main_state

name = "MaptoolState"

from pico2d import*
from grass import Grass

from Tile_1 import Tile
from Tile_2 import Tile_2
from crystal import Crystal

background = None
mode, kind = 0,0
tile_x, tile_y, tile_mode, tri_obs_x, tri_obs_y = [], [],[],[],[]
x, y, mx, my, size_x, size_y = 0, 0, 0, 0, 0, 0
image = None
speed, inspeed = 0.28, 0
stop = True
tiles, tri_obses = [] , []
real_y = 1800
delete_idx = 0


def enter():
    global mode, kind
    mode = 't'
    kind = 1
    global basic_tile_x, basic_tile_y, tile2_x, tile2_y, tri_obs_x, tri_obs_y
    tile_x, tile_y, tile_mode, tri_obs_x, tri_obs_y = [], [], [], [], []
    global image
    image = load_image('resourse/tile_1.png')

    global x, y, mx, my, size_x ,size_y, real_x, stop
    size_x = 100
    size_y = 100
    real_x = 0
    stop = True

    global background, speed, inspeed
    background = Grass()
    speed= 2.8
    inspeed = 0

    global tiles, tri_obses, delete_idx
    delete_idx = "tile"

    ReadPos()
    pass


def exit():
    # 모드를 나갈때 txt파일에 각 장애물, 타일의 pos값을 저장한다.
    f = open('tile_pos.txt', mode='wt')
    for i in range(0,len(tiles)):
        f.write(str(tile_x[i]))
        f.write('\n')
        f.write(str(tile_y[i]))
        f.write('\n')
        f.write(str(tile_mode[i]))
        f.write('\n')
    f.write('end\n')

    f2 = open('crystal.txt', mode = 'wt')
    for i in range(0,len(tri_obses)):
        f2.write(str(tri_obs_x[i]))
        f2.write('\n')
        f2.write(str(tri_obs_y[i]))
        f2.write('\n')
    f2.write('end\n')
    f.close()
    f2.close()

def pause():
    pass


def resume():
    pass


def handle_events():
    global image, size_x, size_y, mx,my,x,y, inspeed, stop, mode, kind
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_1:
                kind = 1
                image = load_image('resourse/tile_1.png')
                size_x = 95
                size_y = 95
            if event.key == SDLK_2:
                kind = 2
                image = load_image('resourse/tile_2.png')
                size_x = 95
                size_y = 95
            if event.key == SDLK_3:
                kind = 3
                image = load_image('resourse/crystal.png')
                size_x = 66
                size_y = 100
            if event.key == SDLK_BACKSPACE:
                DeleteBlock()
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            if event.key == SDLK_s:
                inspeed = 0
                stop = True
            if event.key == SDLK_r:
                inspeed = speed
                stop = False
            if event.key == SDLK_m:
                game_framework.change_state(main_state)
        elif event.type == SDL_MOUSEBUTTONDOWN:
            x = event.x
            y = 800- event.y -1
            Create()
        elif event.type == SDL_MOUSEMOTION:
            mx = event.x
            my = 800 - event.y -1


def update():
    global speed, real_y, inspeed
    if(stop == False):
        background.y -= 1
        background.update()
        real_y -= 1
        for tile in tiles:
            tile.update(inspeed)
        for tri_obs in tri_obses:
            tri_obs.update(inspeed)
    delay(0.01)


def draw():
    hide_cursor()
    clear_canvas()
    background.draw()
    image.draw(mx,my,size_x,size_y)
    for tile in tiles:
        tile.draw()
    for tri_obs in tri_obses:
        tri_obs.draw()
    update_canvas()

    pass

def Create():
    global delete_idx
    if kind == 1:
        #basic tile
        tiles.append(Tile(x,y, 1))
        tile_x.append(x+real_x)
        tile_y.append(y)
        tile_mode.append(1)
        delete_idx = "tile"
    elif kind ==2:
        #tile2
        tiles.append(Tile(x , y, 0))
        tile_x.append(x + real_x)
        tile_y.append(y)
        tile_mode.append(2)
        delete_idx = "tile"
    elif  kind == 3:
        #triangle obstacle
        tri_obses.append(Crystal(x,y))
        tri_obs_x.append(x+real_x)
        tri_obs_y.append(y)
        delete_idx = "tri_obs"


def DeleteBlock():
    if(delete_idx =="tile"):
        del tiles[len(tiles)-1]
        del tile_x[len(tiles)-1]
        del tile_y[len(tiles)-1]
        del tile_mode[len(tile_mode)-1]

    if(delete_idx == "tri_obs"):
        del tri_obses[len(tri_obses)-1]
        del tri_obs_y[len(tri_obs_y)-1]
        del tri_obs_x[len(tri_obs_x)-1]
    pass

def ReadPos():
    global tile_x,tile_y,tile_mode,tri_obs_x,tri_obs_y,tiles,tri_obses
    f = open('tile_pos.txt',mode = 'rt')
    #tile pos read
    while True:
        line = f.readline()
        line.strip('\n')
        if line == 'end\n' or (not line) or line == '':
            break
        tile_x.append(float(line))
        line = f.readline()
        line.strip('\n')
        if  line == 'end\n' or (not line) or line == '':
            break
        tile_y.append(float(line))
        line = f.readline()
        line.strip('\n')
        if  line == 'end\n' or not line or line == '':
            break
        tile_mode.append(int(line))
        if tile_mode[len(tile_mode)-1] == 1:
            tiles.append(Tile(tile_x[len(tile_x)-1],tile_y[len(tile_x)-1],1))
        elif tile_mode[len(tile_mode)-1] == 2:
            tiles.append(Tile(tile_x[len(tile_x)-1],tile_y[len(tile_y)-1],2))

    f2 = open('crystal.txt', mode = 'rt')
    #triangle obstacle pos read
    while True:
        line = f2.readline()
        line.strip('\n')
        if line == "end\n" or not line or line == '':
            break
        tri_obs_x.append(float(line))

        line = f2.readline()
        line.strip('\n')
        if  line == 'end\n' or not line or line == '':
            break
        tri_obs_y.append(float(line))

        tri_obses.append(Crystal(tri_obs_x[len(tri_obs_x)-1],tri_obs_y[len(tri_obs_y)-1]))

    f.close()
    f2.close()
