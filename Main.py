import re
import sys
import os
import help
import sshing
import writelog
import bcolors

#######################################################################
# Validation of SYS ARGV
def validate_sysargv(hostfile):
    host = []
    try:
        for line in open(hostfile, 'r'):
            hostsearch = re.search("^(\d+\.\d+\.\d+\.\d+).*",line)
            if hostsearch:host.append(hostsearch.group(1))
    except:
        os.system("clear")
        print bcolors.bcolors.FAIL + " Cannot read the provided file "+ bcolors.bcolors.ENDC, sys.argv[1]
    return host

#######################################################################
# FUNCTION - CREATE FOLDER IF IS DOESNT EXIST
def createFolders(logpath):
	if not os.path.exists(logpath):os.makedirs(logpath)

#######################################################################
# MAIN
def main():
# Variables Criation
    logpath = './logpath/'
    commands = ["terminal lenght 0","show running-config"] # Array for comand's to send over ssh

    createFolders(logpath)
    hostip=validate_sysargv(sys.argv[1])
    for IP in hostip:
        tolog=sshing.sshing(IP,commands)
        writelog.writelog(tolog[1],tolog[0],logpath)
    print bcolors.bcolors.OKGREEN + "scritp ended" + bcolors.bcolors.ENDC

#######################################################################
# ACCESS TO MAIN
if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 2 :
        help.help()
    else:
        main()
