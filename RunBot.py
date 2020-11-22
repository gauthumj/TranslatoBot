from subprocess import Popen

filename = 'server.py'

while True:
    print('Starting bot ...')
    p = Popen("python "+ filename, shell=True )
    p.wait()