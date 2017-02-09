import bcolors
import getpass
import pexpect
from pexpect import pxssh

#######################################################################
# SSHING
def sshing(host,commands,local):
    if local == 'gui':
        user = 'Username'
        pswd = 'Password'
    elif local == 'cli':
        user = raw_input('Username: ')
        pswd = getpass.getpass('Password: ')
    tout = 360
    failed = 0
    output_string=''
    try:
        ssh = pxssh.pxssh()
        ssh = pxssh.pxssh(options={
                    "StrictHostKeyChecking": "no",
                    "UserKnownHostsFile": "/dev/null"})
        ssh.login( host, user, pswd, auto_prompt_reset=False)
        ssh.sendline('\n')
        ssh.expect('#', timeout=tout)
        h = ssh.before
        hostname = h.lstrip()
        output_string+= ssh.before
        for command in commands:
            ssh.sendline(command)
            ssh.expect('#', timeout=tout)
            output_string+= '#' + ssh.before
        if local == 'gui':print "Device " + hostname + " configured."
        elif local == 'cli':print bcolors.bcolors.OKGREEN + "Device " + hostname + " configured." + bcolors.bcolors.ENDC
        return (output_string,hostname)
    except pxssh.ExceptionPxssh as e:
        output_string=''
        if local == 'gui':print "pxssh failed to login to : " + host + " ."
        elif local == 'cli':print bcolors.bcolors.FAIL + "pxssh failed to login to : " + host + " ." + bcolors.bcolors.ENDC
        output_string += str(e)
        return (output_string,host)
