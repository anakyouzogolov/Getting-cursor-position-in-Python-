from pynput.mouse import Controller
from pynput.mouse import Listener

my_mouse = Controller()

# set mouse position to 0,0 
my_mouse.position = (0,0)


# to get your mouse position 
print(my_mouse.position)

# to set new position values 
x = 500
y = 500
my_mouse.position = (x, y)


def mouse_move(x,y):
  print("Mouse position is : {0}".format((x,y)))


# get mouse position in live mode using listener

with Listener(on_move = mouse_move) as listener:
  listener.join()


