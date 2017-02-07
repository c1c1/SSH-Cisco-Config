# SSH-Cisco-Config

Basic Script for SSH to Cisco Routers or Switches and run some commands on it.


#Before use:
Python Version 2

Needed an hostfile with the name of the device (EX:192.68.2.250), this file must be an text file or a file without extension see file called host.

On module sshing.py change lines 8 & 9 to correct user and password.

On Main.py change line 32 array commands to your suitable commands.

#Modules used:
re

sys

os

pexpect

from pexpect used pxssh

#To use:
simply run:" python Main.py <hostfile> "

#To do:
Prompt for Username && Password (Now HARDCODED)

Add commandsfile by sys.argv (Now HARDCODED)
