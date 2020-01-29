import numpy as np
from PIL import ImageGrab
import cv2
import time
import random
import math

import win32api
import win32con
from PIL import Image


VK_CODE = {'backspace': 0x08,
           'tab': 0x09,
           'clear': 0x0C,
           'enter': 0x0D,
           'shift': 0x10,
           'ctrl': 0x11,
           'alt': 0x12,
           'pause': 0x13,
           'caps_lock': 0x14,
           'esc': 0x1B,
           'spacebar': 0x20,
           'page_up': 0x21,
           'page_down': 0x22,
           'end': 0x23,
           'home': 0x24,
           'left_arrow': 0x25,
           'up_arrow': 0x26,
           'right_arrow': 0x27,
           'down_arrow': 0x28}


class clubdance():
  # leftsign = (58, 65)
  # upsign = (148, 65)
  # downsign = (227, 65)
  # rightsign = (319, 65)
  # sign_empty_color = (166, 166, 166)
  # validgame = (967, 139)
  # validgamecolor = (254, 254, 254)

  leftsign = [(52, 50), (60, 45)]
  upsign = [(130, 55), (150, 40)]
  downsign = [(210, 45), (230, 40)]
  rightsign = [(325, 50), (325, 45)]
  sign_empty_color = (166, 166, 166)
  validgame = (967, 139)
  validgamecolor = (254, 254, 254)

  # Can add features over here for use
  upsign_col = (255, 226, 2)
  rightsign_col = (0, 61, 0)
  downsign_col = (55, 174, 0)
  leftsign_col = (213, 108, 0)


def isup(nums):
  return nums[0:2] == clubdance.upsign_col[0:2]
  # return math.sqrt(abs(nums[0]-255)**2 + abs(nums[1]-226)**2 + abs(nums[2]-5)**2) <= 10
def isleft(nums):
  return nums[0:2] == clubdance.leftsign_col[0:2]
  # return math.sqrt(abs(nums[0]-213)**2 + abs(nums[1]-108)**2 + abs(nums[2]-24)**2) <= 10
def isright(nums):
  return nums[0:2] == clubdance.rightsign_col[0:2]
  # return math.sqrt(abs(nums[0]-84)**2 + abs(nums[1]-124)**2 + abs(nums[2]-223)**2) <= 10 or math.sqrt(abs(nums[0])**2 + abs(nums[1]-61)**2 + abs(nums[2]-208)**2) <= 10
def isdown(nums):
  return nums[0:2] == clubdance.downsign_col[0:2]
  # return math.sqrt(abs(nums[0]-55)**2 + abs(nums[1]-174)**2 + abs(nums[2]-90)**2) <= 10

def scangame(image=None):
  '''
  scangame() returns str: 4 with 0 or 1 depending on wether there is an arrow or not.
  '''
  if image == None:
    image = ImageGrab.grab()
  string = ["0", "0", "0", "0"]
  '''
    if image.getpixel(clubdance.leftsign) != clubdance.sign_empty_color:
        string[0] = "1"
    if image.getpixel(clubdance.upsign) != clubdance.sign_empty_color:
        string[1] = "1"
    if image.getpixel(clubdance.rightsign) != clubdance.sign_empty_color:
        string[2] = "1"
    if image.getpixel(clubdance.downsign) != clubdance.sign_empty_color:
        string[3] = "1"
    '''
  if isleft(image.getpixel(clubdance.leftsign[0])):
    string[0] = "1"
  if isup(image.getpixel(clubdance.upsign[0])):
    string[1] = "1"
  if isright(image.getpixel(clubdance.rightsign[0])):
    string[3] = "1"
  if isdown(image.getpixel(clubdance.downsign[0])):
    string[2] = "1"
  return ''.join(string)

def press(args):
  '''
  one press, one release.
  accepts as many arguments as you want. e.g. press('left_arrow', 'a','b').
  '''
  for i in args:
    win32api.keybd_event(VK_CODE[i], 0, 0, 0)
    win32api.keybd_event(VK_CODE[i], 0, win32con.KEYEVENTF_KEYUP, 0)


def main():

  FPS_SMOOTHING = 0.9
  fps = 0.0
  prev = time.time()
  time.sleep(3)
  # last_time = time.time()
  prev = "0000"
  while True:
    executed = ["0", "0", "0", "0"]
    # screen = ImageGrab.grab()
    screen = ImageGrab.grab(bbox=(10, 450, 600, 600))
    # new_screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)

    # print('Frame took {} seconds'.format(time.time()-last_time))

    # last_time = time.time()
    # now = time.time()
    # fps = (fps*FPS_SMOOTHING + (1/(now - prev))*(1.0 - FPS_SMOOTHING))
    # prev = now

    # print("fps: {:.1f}".format(fps))
    # new_screen = process_img(screen)
    # cv2.imshow('window', np.array(screen))
    results = scangame(screen)
    # print(keys_)
    c = ["left_arrow", "up_arrow", "down_arrow", "right_arrow"]
    tomodify = []
    for i in range(0, 4):
      if results[i] == "1" and prev[i] == "0":
        tomodify.append(c[i])
        executed[i] = "1"
    press(tomodify)
    prev = results

    # cv2.imshow('window', cv2.cvtColor(np.array(screen), cv2.COLOR_BGR2RGB))
    # if cv2.waitKey(25) & 0xFF == ord('q'):
    #   cv2.destroyAllWindows()
    #   break
    # if cv2.waitKey(0) == 'a':
    # test_control()/
    # break
    screen.save("output.png")
    exit(0)

    # if results != "0000":
    #   print('  '.join(list(results)), "".join(executed), flush=True)


if __name__ == "__main__":
  main()


# 78, 304
