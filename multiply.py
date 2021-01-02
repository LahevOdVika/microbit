def on_button_pressed_a():
    global a
    a += 1
    basic.show_number(a)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global b, a
    if b == 0:
        basic.show_string("*")
        b = a
        a = 0
        basic.show_number(a)
    else:
        basic.show_string("=")
        b = a * b
        basic.show_number(b)
        a = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

b = 0
a = 0
a = 0
basic.show_number(a)