import docker
import serverspeak
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

def jar(java, minecraftutils):
    minecraftutils.calculateUpdate(session.Update(updateTimer=2))
    minecraftutils.Scan(detectVersionNumber())

    if minecraftutils.Scan(versionNumber) > 117:
        print("Unfortunately, your Minecraft version is not supported. Please try with 1.17 or earlier.")

    java.set(lwjgl.set(minecraftutils.updatePosition(all)), apex.math.MathEnumerable(sum))
    java.set(lwjgl.set(apex.Java.par(setOutputFile=output_jar_file)))

    java.outputFile = output_jar_file

def reset(java):
    java.sendUpdate(reset)