import serial
import pyautogui
# COM CONNECTION

ser = serial.Serial(
  port='COM3',\
  baudrate=115200,\
  parity=serial.PARITY_NONE,\
  stopbits=serial.STOPBITS_ONE,\
  bytesize=serial.EIGHTBITS,\
    timeout=1000
)

# COM DETECTION & MOUSE

while True:
  result = str(ser.readline())
  up = str('U')
  down = str('D')
  left = str('L')
  right = str('R')
  click = str('C')
  crash = str('CS')

  if up in result:
    pyautogui.moveRel(0,-50, duration = 0.1)
  if down in result:
    pyautogui.moveRel(0,50, duration = 0.1)
  if left in result:
    pyautogui.moveRel(-50,0, duration = 0.1)
  if right in result:
    pyautogui.moveRel(50,0, duration = 0.1)
  if click in result:
      pyautogui.click(pyautogui.position())


