import re
import sys
import os

#######################################################################
# Validation of commandfile
def validate_commandfile(commandfile):
    command = []
    try:
        for line in open(commandfile, 'r'):
            isline = re.search("(.*)\n$",line)
            if isline:command.append(isline.group(1))
            else:command.append(line)

    except:
        print " Cannot read the provided file "
    return command

#######################################################################
# Validation of hostfile
def validate_hostfile(hostfile):
    host = []
    try:
        for line in open(hostfile, 'r'):
            hostsearch = re.search("^(\d+\.\d+\.\d+\.\d+).*",line)
            if hostsearch:host.append(hostsearch.group(1))
    except:
        print " Cannot read the provided file "
    return host
