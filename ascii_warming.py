import os
import numpy as np


rows, columns = os.popen('stty size', 'r').read().split()

print(columns)

temp_data = 'data/global_temps.csv'
temps = np.genfromtxt(temp_data, delimiter=",", usecols=(5))[1:]
temps_normed = ((temps - temps.min(0)) / temps.ptp(0)) * (len(temps) - 1)
print (temps)
elements = len(temps)
x_lbls = np.arange(elements)
print (x_lbls)

class Colors:
  FG_DEFAULT = "\033[39m"
  FG_BLACK = "\033[30m"
  FG_RED = "\033[31m"
  FG_LRED = "\033[91m"
  FG_YELLOW = "\033[33m"
  FG_LGRAY = "\033[37m"
  FG_WHITE = "\033[97m"
  FG_LBLUE = "\033[94m"
  FG_BLUE = "\033[34m"
  BG_DEFAULT = "\033[49m"
  BG_BLACK = "\033[40m"
  BG_RED = "\033[41m"
  BG_LRED = "\033[101m"
  BG_YELLOW = "\033[43m"
  BG_LGRAY = "\033[47m"
  BG_WHITE = "\033[107m"
  BG_LBLUE = "\033[104m"
  BG_BLUE = "\033[44m"
  RESET = "\033[0m"

palette = [
    # [char, style fg, fg color, style bg, bg color]
    ["░", Colors.FG_RED, Colors.BG_BLACK],
    ["▒", Colors.FG_RED, Colors.BG_BLACK],
    ["▓", Colors.FG_RED, Colors.BG_BLACK],
    ["█", Colors.FG_RED, Colors.BG_BLACK],
    ["░", Colors.FG_LRED, Colors.BG_RED],
    ["▒", Colors.FG_LRED, Colors.BG_RED],
    ["▓", Colors.FG_LRED, Colors.BG_RED],
    ["█", Colors.FG_LRED, Colors.BG_RED],
    ["░", Colors.FG_LGRAY, Colors.BG_LRED],
    ["▒", Colors.FG_LGRAY, Colors.BG_LRED],
    ["▓", Colors.FG_LGRAY, Colors.BG_LRED],
    ["█", Colors.FG_LGRAY, Colors.BG_LRED],
    ["░", Colors.FG_WHITE, Colors.BG_LGRAY],
    ["▒", Colors.FG_WHITE, Colors.BG_LGRAY],
    ["▓", Colors.FG_WHITE, Colors.BG_LGRAY],
    ["█", Colors.FG_WHITE, Colors.BG_LGRAY],
    ["░", Colors.FG_LBLUE, Colors.BG_WHITE],
    ["▒", Colors.FG_LBLUE, Colors.BG_WHITE],
    ["▓", Colors.FG_LBLUE, Colors.BG_WHITE],
    ["█", Colors.FG_LBLUE, Colors.BG_WHITE],
    ["░", Colors.FG_BLUE, Colors.BG_LBLUE],
    ["▒", Colors.FG_BLUE, Colors.BG_LBLUE],
    ["▓", Colors.FG_BLUE, Colors.BG_LBLUE],
    ["█", Colors.FG_BLUE, Colors.BG_LBLUE],
]

print(Colors.RESET)
def print_palette(pal):
  for item in pal:
    print(item[1] + item[2] + item[0] + Colors.RESET)

print_palette(palette)
print(len(palette))

  
