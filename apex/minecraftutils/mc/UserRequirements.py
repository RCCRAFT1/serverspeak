import user_agents
import userrequirements
from minecraftutils import mc


for mc.player(user):
    requirements(
        #define player dataset
        mc.player.op=True
        mc.player.interaction=True 
        mc.player.chat(global)=True
    )
for mc.entity():
    requirements(
        #define entity dataset
        mc.entity.interaction=True
        mc.entity.player_interaction=True
    )
for bool(param 0: object):
    license(none)
