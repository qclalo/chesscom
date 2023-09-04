from pynput.mouse import Listener

def on_move(x, y):
    print(f"Mouse moved to ({x}, {y})")

# Create a listener that calls the on_move function when the mouse is moved
with Listener(on_move=on_move) as listener:
    listener.join()

# 320, 175 --------------- 1070,175
# 320, 925 --------------- 1070,925

# 265, 140 --------------- 1070, 140
# 265, 945 --------------- 1070, 945