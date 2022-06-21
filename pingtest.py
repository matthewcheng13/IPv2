import subprocess

address = '7.7.7.7'

print(subprocess.check_output("ping -c 1 " + address, shell=True))