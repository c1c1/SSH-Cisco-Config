import re
import sys
import os
import sshing
import writelog
import validating_files
import gooey
from gooey import GooeyParser

#######################################################################
# FUNCTION - CREATE FOLDER IF IS DOESNT EXIST
def createFolders(logpath):
	if not os.path.exists(logpath):os.makedirs(logpath)

#######################################################################
# Main Fuction
@gooey.Gooey(program_name='SSH Cisco Config')
def main():
    local = 'gui'
    parser = GooeyParser(description='Script for changing devices configurations')
    parser.add_argument('hostfile',help='File with hosts ID\'s', widget='FileChooser')
    parser.add_argument('comandfile',help='File with command\'s to execute on hosts', widget='FileChooser')
    parser.add_argument('logpath',help='Path where it will be saved the log\'s from SSH sessions')
    args = parser.parse_args()
    createFolders(args.logpath)
    hostid=validating_files.validate_hostfile(args.hostfile)
    commands=validating_files.validate_commandfile(args.comandfile)
    for IP in hostid:
        tolog=sshing.sshing(IP,commands,local)
        writelog.writelog(tolog[1],tolog[0],args.logpath)
    scriptend = "scritp ended"
    print "\n" + scriptend.center(150, ' ')


#######################################################################
# ACCESS TO MAIN
if __name__ == "__main__":
        main()
