tinkercademy.crash_sensor_setup(DigitalPin.P13)
pins.digital_read_pin(DigitalPin.P0)

def on_forever():
    if pins.analog_read_pin(AnalogPin.P1) >= 1020:
        # UP
        serial.write_line("U1")
    if pins.analog_read_pin(AnalogPin.P1) <= 10:
        # DOWN
        serial.write_line("D1")
    if pins.analog_read_pin(AnalogPin.P2) <= 10:
        # LEFT
        serial.write_line("L1")
    if pins.analog_read_pin(AnalogPin.P2) >= 1020:
        # RIGHT
        serial.write_line("R1")
    if tinkercademy.crash_sensor():
        # DETECTION
        serial.write_line("CS1")

basic.forever(on_forever)
