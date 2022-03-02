lcd_text = ""
tinkercademy.crash_sensor_setup(DigitalPin.P13)
pins.digital_read_pin(DigitalPin.P0)
I2C_LCD1602.show_string(lcd_text, 0, 0)
I2C_LCD1602.lcd_init(39)

def on_forever():
    global lcd_text

    angle = pins.analog_read_pin(AnalogPin.P1)
    pins.servo_write_pin(AnalogPin.P13, angle)

    if pins.analog_read_pin(AnalogPin.P1) >= 1020:
        #UP
        serial.write_line("U")
    if pins.analog_read_pin(AnalogPin.P1) <= 10:
        #DOWN
        serial.write_line("D")
        
    if pins.analog_read_pin(AnalogPin.P2) >= 1020:
        #LEFT
        serial.write_line("L")
    if pins.analog_read_pin(AnalogPin.P2) <= 10:
        #RIGHT
        serial.write_line("R")
    if tinkercademy.crash_sensor():
        #DETECTION CRASH
        serial.write_line("crash")

    if input.button_is_pressed(Button.A):
        #BUZZER
        pins.digital_write_pin(DigitalPin.P14, 1)
    else:
        #BUZZER
        pins.digital_write_pin(DigitalPin.P14, 0)

basic.forever(on_forever)
