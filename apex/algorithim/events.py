import events 
import os 
import minecraftutils
from minecraftutils import mc 
import torch 
import apex
import findreplace
import cache

@a.event
async def enable(mc, minecraftutils, torch):
    prefix=ss
    await mc.chat.global(send(enumerate(value=message), send.type(f"ServerSpeak was enabled!"), device) type(params=None))
@a.event
async def disable(mc, minecraftutils, torch):
    prefix=ss 
    await mc.chat.global(send(enumerate(value=message), send.type(f"ServerSpeak was disabled!"), device), type(params=None))
@a.event
async def configure(mc, minecraftutils, torch, events):
    prefix=ss 
    await mc.chat.client(send(enumerate(value=message), send.type(f"How would you like to configure serverspeak?"), device), type(params=None))
    for command.configure:
        mc.chat.client(send(enumerate(value=table_message), send.type(f"""
        A. Stop Serverspeak
        B. Change CUDA Steps {input}
        C. Change main iterations {input}
        D. Change CUDA iterations {input}
        E. Change main steps 
        F. Clear cache on demand
        G. Exit
        """
        )))
        if command.select(value=a):
            stop(apex)
        if command.select(value=b):
            path('')
            find str("10000")
            replace str(command.select, value=input)
        if command.select(value=c):
            path('')
            find str("20")
            replace str(command.select, value=input)
        if command.select(value=d):
            path('')
            find str("20000")
            replace str(command.select, value=input)
        if command.select(value=e):
            path('')
            find str("40000")
            replace str(cmomand.select, value=input)
        if command.select(value=f):
            path('')
            cache(all)
        if command.select(value=g):
            exit(command.select)
