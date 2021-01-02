nástroj = 0

def on_button_pressed_a():
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global nástroj
    nástroj = randint(0, 1)
    if nástroj == 0:
        basic.show_icon(IconNames.YES)
    if nástroj == 1:
        basic.show_icon(IconNames.NO)
input.on_button_pressed(Button.B, on_button_pressed_b)


