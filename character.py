import game_framework
from pico2d import *
import title_state
import main_state
import game_world

# Boy Run Speed
# fill expressions correctly
PIXEL_PER_METER = (10.0 / 0.2)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
# fill expressions correctly
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 4


TIME_PER_COLLIDE_ACTION = 0.5
ACTION_PER_COLLIDE_TIME = 1.0 / TIME_PER_COLLIDE_ACTION
FRAMES_PER_COLLIDE_ACTION = 11
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

    @staticmethod
    def draw(character):
        character.image.clip_draw(int(character.frameX) * 360, 3 * 360, 360, 360, int(character.x), int(character.y), character.size, character.size)


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
        print(RUN_SPEED_PPS)
        if(character.dirY == 0):
            if (character.frameY == 4):
                character.frameX = (character.frameX + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
                character.x += character.dir * RUN_SPEED_PPS * game_framework.frame_time * character.alpha_speed
            elif (character.frameY == 6):
                character.frameX = (character.frameX - FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
                character.x += character.dir * RUN_SPEED_PPS * game_framework.frame_time * character.alpha_speed
            character.x = clamp(120, character.x, 450)
        else:
            character.y += character.dirY

    @staticmethod
    def draw(character):
        character.image.clip_draw(int(character.frameX) * 360, character.frameY * 360, 360, 360, int(character.x), int(character.y), character.size, character.size)


class AttackState:
    @staticmethod
    def enter(character, event):
        if (event == A_DOWN):
            character.attack.play()
            if (character.dir == -1):
                character.frameY = 7
                character.frameX = 19
            else :
                character.frameY = 0
                character.frameX = 0
        elif event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)

    @staticmethod
    def exit(character, event):
        pass

    @staticmethod
    def do(character):
        if(character.dirY == 0):
            if (character.frameY == 0):
                character.frameX = (character.frameX + 1) % 19
                if (character.frameX == 0):
                    character.frameY = 3
                    character.frameX = 2
                    for tile in main_state.tile1:
                        if main_state.collide(tile, character):
                            if tile.mode == 2 and (tile.x - character.x)**2 < 2256.25:
                                main_state.tile1.remove(tile)
                                game_world.remove_object(tile)
            elif (character.frameY == 7):
                character.frameX = (character.frameX - 1) % 19
                if (character.frameX == 0):
                    character.frameY = 3
                    character.frameX = 2
                    for tile in main_state.tile1:
                        if main_state.collide(tile, character):
                             if tile.mode == 2 and (tile.x - character.x)**2 < 2256.25:
                                 main_state.tile1.remove(tile)
                                 game_world.remove_object(tile)
        else:
            character.y += character.dirY

    @staticmethod
    def draw(character):
        character.image.clip_draw(int(character.frameX) * 365, character.frameY * 360, 360, 360, int(character.x), int(character.y), character.size, character.size)


class CoillidMonsterState:
    @staticmethod
    def enter(character, event):
        #character.frameX = 6
        #character.frameY = 1
        pass

    @staticmethod
    def exit(character, event):
        pass

    @staticmethod
    def do(character):
        if character.frameX < 1:
            character.cur_state = IdleState

        character.frameX = (character.frameX + 0.2) % 11
        print(character.frameX)

        character.y += 1
        character.x = clamp(120, character.x, 450)

    @staticmethod
    def draw(character):
        character.image.clip_draw(int(character.frameX) * 360, 1 * 360, 360, 360, int(character.x), int(character.y), character.size, character.size)


next_state_table = {
    IdleState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState, A_DOWN: AttackState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: RunState, RIGHT_DOWN: RunState, A_DOWN: AttackState},
    AttackState: {LEFT_DOWN: RunState, RIGHT_DOWN: RunState, LEFT_UP: IdleState, RIGHT_UP: IdleState, A_DOWN: AttackState},
    CoillidMonsterState: {LEFT_DOWN: CoillidMonsterState, RIGHT_DOWN: CoillidMonsterState, LEFT_UP: CoillidMonsterState, RIGHT_UP: CoillidMonsterState, A_DOWN: CoillidMonsterState}
}


class Chatacter:
    def __init__(self):
        self.x, self.y = 120, 1200
        self.frameX, self.frameY = 2, 3
        self.image = load_image('resourse/character.png')
        self.dir, self.dirY = 0, 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)
        self.attack = load_wav('resourse/attack.wav')
        self.attack.set_volume(64)
        self.get_hit = load_wav('resourse/get_hit.wav')
        self.get_hit.set_volume(64)
        self.alpha_speed = main_state.inventory.speed
        self.size = 160

    def add_event(self, event):
        self.event_que.insert(0, event)

    def get_bb(self):
        return self.x - 15, self.y - self.size / 2, self.x + 15, self.y - 20

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def stop(self):
        self.dirY = 0