import os


def run_os(cmd, address):
    return os.system("ping -{} 1 {}".format(cmd, address))

address = '7.7.7.7'
print([run_os('n',address) == 0])
print(run_os('c',address) == 0)

print(run_os('n','google.com') == 0)