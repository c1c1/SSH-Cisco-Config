import re
import sys
import os
import help
import sshing
import writelog
import validating_files
import bcolors

#######################################################################
# FUNCTION - CREATE FOLDER IF IS DOESNT EXIST
def createFolders(logpath):
	if not os.path.exists(logpath):os.makedirs(logpath)

#######################################################################
# MAIN
def main():
	local = 'cli'
    logpath = './logpath/'
    createFolders(logpath)
    hostip=validating_files.validate_hostfile(sys.argv[1])
    commands=validating_files.validate_commandfile(sys.argv[2])
    for IP in hostip:
        tolog=sshing.sshing(IP,commands,local)
        writelog.writelog(tolog[1],tolog[0],logpath)
    print bcolors.bcolors.OKGREEN + "scritp ended" + bcolors.bcolors.ENDC

#######################################################################
# ACCESS TO MAIN
if __name__ == "__main__":
    if len(sys.argv) < 3 or len(sys.argv) > 3 :
        help.help()
    else:
        main()
