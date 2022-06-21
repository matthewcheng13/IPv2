import subprocess

address = '7.7.7.7'

subprocess.check_output("ping -c 1 " + address, shell=True)