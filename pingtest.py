import subprocess


def ping(address):
    try:
        return subprocess.check_output("ping -c 1 " + address, shell=True)
    except subprocess.CalledProcessError:
        return "Subprocess"
    except:
        return "Other"


print(ping('7.7.7.7'))
print(ping('google.com'))
