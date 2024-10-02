from ai2thor.controller import Controller
from ai2thor.platform import CloudRendering
import os
import sys
sys.path.append(os.path.join(os.environ['ALFRED_ROOT']))
from env.thor_env import ThorEnv

env = ThorEnv(player_screen_width=300, player_screen_height=300)

c = Controller(platform=CloudRendering)
# c.start()
event = c.step(dict(action="MoveAhead"))
assert event.frame.shape == (300, 300, 3)
print(event.frame.shape)
print("Everything works!!!")
