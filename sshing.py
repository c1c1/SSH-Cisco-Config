import bcolors
import pexpect
from pexpect import pxssh

#######################################################################
# SSHING
def sshing(host,commands):
    user='user'
    password='password'
    tout = 360
    failed = 0
    output_string=''
    try:
        ssh = pxssh.pxssh()
        ssh = pxssh.pxssh(options={
                    "StrictHostKeyChecking": "no",
                    "UserKnownHostsFile": "/dev/null"})
        ssh.login( host, user, password, auto_prompt_reset=False)
        ssh.sendline('\n')
        ssh.expect('#', timeout=tout)
        h = ssh.before
        hostname = h.lstrip()
        output_string+= ssh.before
        for command in commands:
            ssh.sendline(command)
            ssh.expect('#', timeout=tout)
            output_string+= '#' + ssh.before
        print bcolors.bcolors.OKGREEN + "Device " + hostname + " configured." + bcolors.bcolors.ENDC
        return (output_string,hostname)
    except pxssh.ExceptionPxssh as e:
        output_string=''
        print bcolors.bcolors.FAIL + "pxssh failed to login to : " + host + " ." + bcolors.bcolors.ENDC
        output_string += str(e)
        return (output_string,host)
