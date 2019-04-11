import subprocess

def TerminalCommand(command, shell=False):
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
