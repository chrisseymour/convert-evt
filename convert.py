import subprocess
import os
import sys

#dir_name = sys.argv[1]
#print( 'folder to read: {}'.format(dir_name) )

def TerminalCommand(command, shell=True):
    print( 'running command: ', command )
    proc = subprocess.Popen(
                            command,
                            shell=shell,
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                           )
    msg = 'running command: "{}"'.format(command).encode('utf-8')
    stdout_value, stderr_value = proc.communicate(msg)

    print('pass through:', repr(stdout_value.decode('utf-8')))
    print('stderr      :', repr(stderr_value.decode('utf-8')))

def getFiles(directory, filetype='.evt'):
    cwd = os.getcwd()   # get current working directory
    pth = os.path.join(cwd, directory)  # combine cwd and pth with '/' between
    # get the names of stuff in the directroy and check if they're files
    filelist = [f for f in os.listdir(
        pth) if os.path.isfile(os.path.join(pth, f))]
    evts = [f for f in filelist if filetype in f]  # only use the .evt files
    return cwd, evts

def evt2rootCommand( filename, indir, outdir, evtdir ):
    outname = filename[:-10]+'.root'
    #outname = filename[:-4]+'.root'
    print(outname)
    cmd = '{}evt2root -o {}/{} {}/{}'.format(evtdir, outdir, outname, indir, filename)
    TerminalCommand( str(cmd) )

if __name__ == '__main__':
    indir = sys.argv[1]
    outdir = sys.argv[2]
    evtdir = '../evt2root/exec/'
    d, files = getFiles( indir)
    print( files )
    for f in files:
        evt2rootCommand(f , indir, outdir, evtdir ) 
        break
