let lcd_text = ""
tinkercademy.crashSensorSetup(DigitalPin.P13)
pins.digitalReadPin(DigitalPin.P0)
I2C_LCD1602.ShowString(lcd_text, 0, 0)
I2C_LCD1602.LcdInit(39)
basic.forever(function on_forever() {
    
    let angle = pins.analogReadPin(AnalogPin.P1)
    pins.servoWritePin(AnalogPin.P13, angle)
    if (pins.analogReadPin(AnalogPin.P1) >= 1020) {
        // UP
        serial.writeLine("U")
    }
    
    if (pins.analogReadPin(AnalogPin.P1) <= 10) {
        // DOWN
        serial.writeLine("D")
    }
    
    if (pins.analogReadPin(AnalogPin.P2) >= 1020) {
        // LEFT
        serial.writeLine("L")
    }
    
    if (pins.analogReadPin(AnalogPin.P2) <= 10) {
        // RIGHT
        serial.writeLine("R")
    }
    
    if (tinkercademy.crashSensor()) {
        // DETECTION CRASH
        serial.writeLine("crash")
    }
    
    if (input.buttonIsPressed(Button.A)) {
        // BUZZER
        pins.digitalWritePin(DigitalPin.P14, 1)
    } else {
        // BUZZER
        pins.digitalWritePin(DigitalPin.P14, 0)
    }
    
})
