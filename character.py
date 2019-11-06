import game_framework
from pico2d import *
import title_state
import main_state
import game_world

# Boy Run Speed
# fill expressions correctly
PIXEL_PER_METER = 0
RUN_SPEED_KMPH = 0
RUN_SPEED_MPM = 0
RUN_SPEED_MPS = 0
RUN_SPEED_PPS = 0

# Boy Action Speed
# fill expressions correctly
TIME_PER_ACTION = 0
ACTION_PER_TIME = 0
FRAMES_PER_ACTION = 0

# Boy Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, A_DOWN, ESCAPE = range(6)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_a): A_DOWN,
}

# States
class IdleState:
    @staticmethod
    def enter(character, event):
        if(event == RIGHT_UP):
            character.dir = 0
            character.frameX = 2
            character.frameY = 3
        elif(event==LEFT_UP):
            character.dir = 0
            character.frameX = 2
            character.frameY = 3
        elif event == ESCAPE:
            game_framework.change_state(title_state)

    @staticmethod
    def exit(character, event):
        pass
    @staticmethod
    def do(character):
        character.y += character.dirY
        if (character.frameY == 4):
            character.frameX = (character.frameX + 1) % 4
            character.x += character.dir * 10
        elif (character.frameY == 6):
            character.frameX = (character.frameX - 1) % 4
            character.x += character.dir * 10
        character.x = clamp(120, character.x, 450)

    @staticmethod
    def draw(character):
        character.image.clip_draw(character.frameX * 360, 3 * 360, 360, 360, character.x, character.y, 160, 160)

class RunState:
    @staticmethod
    def enter(character, event):
        if (event == RIGHT_DOWN):
            character.dir = 1
            character.frameX = 0
            character.frameY = 4
        elif (event == LEFT_DOWN):
            character.dir = -1
            character.frameX = 0
            character.frameY = 6

    @staticmethod
    def exit(character, event):
        pass

    @staticmethod
    def do(character):
        if(character.dirY == 0):
            if (character.frameY == 4):
                character.frameX = (character.frameX + 1) % 4
                character.x += character.dir * 10
            elif (character.frameY == 6):
                character.frameX = (character.frameX - 1) % 4
                character.x += character.dir * 10
            character.x = clamp(120, character.x, 450)
        else:
            character.y += character.dirY


    @staticmethod
    def draw(character):
        character.image.clip_draw(character.frameX * 360, character.frameY * 360, 360, 360, character.x, character.y, 160, 160)

class AttackState:
    @staticmethod
    def enter(character, event):
        if (event == RIGHT_DOWN):
            character.dir += 1
            character.frameX = 0
            character.frameY = 4
        elif (event == LEFT_DOWN):
            character.dir -= 1
            character.frameX = 0
            character.frameY = 6
        elif (event == A_DOWN):
            if (character.dir == -1):
                character.frameY = 7
                character.frameX = 19
            else :
                character.frameY = 0
        elif event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)

    @staticmethod
    def exit(character, event):
        pass

    @staticmethod
    def do(character):
        if(character.dirY==0):
            if (character.frameY == 0):
                character.frameX = (character.frameX + 1) % 19
                if (character.frameX == 0):
                    character.frameY = 3
                    character.frameX = 2
                    for tile in main_state.tile1:
                        if main_state.collide(tile, character):
                            if tile.mode == 2:
                                 main_state.tile1.remove(tile)
                                 game_world.remove_object(tile)
                            else:
                                pass
            elif (character.frameY == 7):
                character.frameX = (character.frameX - 1) % 19
                if (character.frameX == 0):
                    character.frameY = 3
                    character.frameX = 2
                    for tile in main_state.tile1:
                        if main_state.collide(tile, character):
                             if tile.mode == 2:
                                 main_state.tile1.remove(tile)
                                 game_world.remove_object(tile)
                             else:
                                 pass
        else:
            character.y += character.dirY

    @staticmethod
    def draw(character):
        character.image.clip_draw(character.frameX * 365, character.frameY * 360, 360, 360, character.x, character.y, 160, 160)

next_state_table = {
    IdleState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState, A_DOWN: AttackState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: RunState, RIGHT_DOWN: RunState, A_DOWN: AttackState},
    AttackState: {LEFT_DOWN: RunState, RIGHT_DOWN: RunState, LEFT_UP: IdleState, RIGHT_UP: IdleState, A_DOWN: AttackState}
}

class Chatacter:
    def __init__(self):
        self.x, self.y = 120, 800
        self.frameX, self.frameY = 2, 3
        self.image = load_image('resourse/character.png')
        self.dir, self.dirY = 0, -8
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def get_bb(self):
        return self.x - 20, self.y - 80, self.x + 15, self.y - 20

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        draw_rectangle(*self.get_bb())

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def stop(self):
        self.dirY = 0

    def collide_monster(self, i):
        self.frameX = 5 + i
        self.frameY = 1
        self.x -= 7
        self.x = clamp(120, self.x, 450)
