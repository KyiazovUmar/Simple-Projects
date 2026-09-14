import random
import shutil
import sys
import time


def matrix_rain():
  columns, rows = shutil.get_terminal_size()
  try:
    while True:
      line = "".join(
          random.choice("0123456789ABCDEFHIJKLMNOPQRSTUVWXYZ*#$@&")
          if random.random() > 0.85
          else " "
          for _ in range(columns)
      )
      print(f"\033[32m{line}\033[0m")
      time.sleep(0.05)
  except KeyboardInterrupt:
    sys.exit()


if __name__ == "__main__":
  matrix_rain()