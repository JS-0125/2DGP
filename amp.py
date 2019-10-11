from pico2d import*

open_canvas(512,1024)

grass = load_image('20180417022947-1-576x1024.jpg')
character = load_image('Mobile - Cookie Run - Roll Cake Cookie.png')

x = 0
frame = 0

while (x < 800):
    clear_canvas()
    grass.draw(238, 512)

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            x += 5
            frame = (frame + 1) % 8
            running = False

    character.clip_draw(frame * 360, 1450, 250, 250, x, 500)
    update_canvas()


    delay(0.05)
    get_events()


close_canvas()