#######################################################################
# WRITING LOG to FILE
def writelog(host,write,logpath):
    filepath = logpath + host + ".txt"
    with open(filepath,"w") as configFile:
        for line in write:configFile.write(line)
