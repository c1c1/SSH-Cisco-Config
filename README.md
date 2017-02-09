# SSH-Cisco-Config

  - Basic Script with GUI or on CLI for SSH to Cisco Routers or Switches and run some commands on it.

### Before use:

  - Python Version 2
  - Needed an hostfile with the name of the device (EX:192.68.2.250), see example file called Hosts.
  - Needed an configurationfile with the commands to send via ssh to device, see example file called Commands.
  - If using GUI.py change lines 10 & 11 of sshing.py to correct user and password, on CLI.py it is asked to user, for each equipment.

### Modules used:

  - re
  - sys
  - os
  - [gooey]
  - [wxpython] for [gooey]
  - getpass
  - pexpect
  - from pexpect used pxssh

### Help for wxpython:

 - After Gooey is installed, make sure [wxPython] is installed on your machine as well. Unfortanately, this cannot be done from the CLI and should be manually downloaded from the [wxPython website].

### To use:

There are two ways to run this script one is form Shell or with a GUI :

```sh
  $ python CLI.py <hostfile> <commandsfile>
  or
  $ python GUI.py
```

Or simply double click on GUI.py

### To do:
  - Create hide textbox for password on gooey
  - Add textbox for Username and Password on gooey



License
----

MIT


**USE IT ON YOUR OWN RISK !**


[gooey]: <https://github.com/chriskiehl/Gooey>
[wxPython]: <http://www.wxpython.org/download.php>
[wxPython website]: <http://www.wxpython.org/download.php>
