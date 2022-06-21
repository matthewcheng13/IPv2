import subprocess


def ping(addr):
    return subprocess.check_output("ping -c 1 " + addr, shell=True)


print(ping('7.7.7.7'))
print(ping('google.com'))
