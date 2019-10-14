from pico2d import*

def handle_events():
    global running
    global dir
    global frameX
    global frameY

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
                frameX = 0
                frameY = 4
            elif event.key == SDLK_LEFT:
                dir -= 1
                frameX = 0
                frameY = 4
            elif event.key == SDLK_a:
                frameY = 0
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                 dir -= 1
                 frameX = 2
                 frameY = 3
            elif event.key == SDLK_LEFT:
                 dir += 1
                 frameX = 2
                 frameY = 3

open_canvas(512,1024)

grass = load_image('20180417022947-1-576x1024.jpg')
character = load_image('Mobile - Cookie Run - Roll Cake Cookie.png')

enemy1 = load_image()

x = 0
dir = 0
frameX = 0
frameY = 4
running = True

while running:
    while (x < 512):
        clear_canvas()
        grass.draw(238, 512)
        character.clip_draw(frameX * 360, frameY * 360, 250, 250, x, 500)
        update_canvas()
        handle_events()

        if(frameY == 4):
            frameX = (frameX + 1) % 4
        elif (frameY == 0):
            frameX = (frameX + 1) % 19
            if( frameX == 0):
                frameY = 4
        x += dir * 10
        delay(0.03)

    close_canvas()
