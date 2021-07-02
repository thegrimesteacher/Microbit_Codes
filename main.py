def on_pin_pressed_p0():
    pass
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def on_button_pressed_a():
    basic.show_leds("""
        . # # # .
        # . . . .
        . # # # .
        . . . . #
        . # # # .
        """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_pulsed_p1_high():
    basic.show_icon(IconNames.HEART)
pins.on_pulsed(DigitalPin.P1, PulseValue.HIGH, on_pulsed_p1_high)

def on_button_pressed_b():
    basic.show_string("Wazzup!")
input.on_button_pressed(Button.B, on_button_pressed_b)

pins.digital_write_pin(DigitalPin.P1, 0)