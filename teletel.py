mport telnetlib, re, os, sys
from optparse import OptionParser

def get_servers(file):
    
    #Need to add some code here
    
    return servers

def get_cmd(list):
    
    #Need to add some code here
    
    return cmds

def do_log(data):
    
    #Need to add some code here
    
    return

def send_cmd(cmd):
    global tn
    if opts.verbose:
        if opts.quiet == False:
            print("Sending command " + cmd)
    tn.write(cmd + "\r\n")
    output = tn.read_until("\n# ")
    ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
    return ansi_escape.sub('', output)

def tel_login():
    global tn
    if opts.verbose:
        if not opts.quiet:
            pass
    print("Connecting to "+s)
    tn.read_until("login: ")
    tn.write(opts.username + "\r\n")
    tn.read_until("Password:")
    tn.write(opts.password + "\r\n")
    tn.read_until("\n# ")
    return

def get_opts():
    parse = OptionParser()
    parse.add_option("-s", "--serverlist", dest="serverlist", metavar="FILE", help="File containing list of servers to run commands on.")
    parse.add_option("-m", "--machine", dest="server", metavar="MACHINE", action="append", help="Run command(s) on one machine [MACHINE].")
    parse.add_option("-c", "--commandlist", dest="cmdlist", metavar="FILE", help="File containing a list of commands to run.")
    parse.add_option("-x", "--execute", dest="command", metavar="COMMAND", action="append", help="Execute single command COMMAND only.")
    parse.add_option("-o", "--output", dest="outfile", metavar="OUTFILE", help="Specify an option output file.")
    parse.add_option("--parallel", dest="parallel", default="False", action="store_true", help="Use Multithreading and run commands in parallel.")
    parse.add_option("-v", dest="verbose", action="store_true", help="Be verbose about what is going on.")
    parse.add_option("-u", "--user", dest="username", metavar="USERNAME", help="Specify a username to login to server(s).")
    parse.add_option("-p", "--password", dest="password", metavar="PASSWORD", help="Specify a password to login to server(s).")
    parse.add_option("-q", "--quiet", dest="quiet", action="store_true", help="Don't display any output.")

    (options, args) = parse.parse_args()

    if options.serverlist and options.server:
        parse.error("Must specify either single machine [-m MACHINE] or file with list of machines [-s FILE].")
    if options.command and options.cmdlist:
        parse.error("Must specify either a single command [-x COMMAND] or file with list of commands [-c FILE].")
    if options.parallel == "True":
        parse.error("Sorry. This isn't supported yet.")
    if not options.username or not options.password:
        parse.error("You must specify both a USERNAME and PASSWORD!")
    if options.quiet == True and not options.outfile:
        print("WARNING: Quiet mode enabled with no output file specified. There will be no logging.")

    return options

if __name__ == '__main__':
    opts = get_opts()
    if opts.serverlist:
        server = get_servers(opts.serverlist)
    else:
        server = opts.server
    if opts.cmdlist:
        command = get_cmds(opts.cmdlist)
    else:
        command = opts.command

    for s in server:
        print("Running on "+s)
        tn = telnetlib.Telnet(s)
        tel_login()
        for c in command:
            print("Running "+c+" on "+s)
            data = send_cmd(c)
            if not opts.quiet:
                print data
            if opts.outfile:
                do_log(data)
    tn.close()
