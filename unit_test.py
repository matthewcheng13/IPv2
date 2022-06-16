import os
from unittest.mock import Mock
from main import pingable

can_ping = '''Pinging 7.7.7.7 with 32 bytes of data:
Reply from 7.7.7.7: bytes=32 time=1ms TTL=59
Reply from 7.7.7.7: bytes=32 time=1ms TTL=59
Reply from 7.7.7.7: bytes=32 time=1ms TTL=59
Reply from 7.7.7.7: bytes=32 time=1ms TTL=59

Ping statistics for 7.7.7.7:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 1ms, Maximum = 1ms, Average = 1ms
'''
cant_ping = '''Pinging google.com [64.233.185.100] with 32 bytes of data:
Request timed out.
Request timed out.
Request timed out.
Request timed out.

Ping statistics for 64.233.185.100:
    Packets: Sent = 4, Received = 0, Lost = 4 (100% loss),
'''
cant_find = '''Ping request could not find host asdfghjkl. Please check the name and try again.
'''

class dummy:

    def __init__(self):
        self.value = 0

    def read(self):
        return 0


dummy.read = Mock()

os.popen = Mock()

'''
def pingable(address):
    """
    Checks to see if the given address is pingable.

    :param address: Host name or ip address
    :return: True if pingable, false if not
    """
    output_stream = os.popen("ping " + address)
    ping_output = output_stream.read()
    if "Reply from" in ping_output:
        can_ping = True
    else:
        can_ping = False
    return can_ping
'''

def check_pingable():
    """
    This function checks to see if the function pingable correctly produces the right output (address is pingable).
    :rtype: object
    """
    return pingable('test')

os.popen.return_value = dummy()

# Mock read() to return pingable output from cmd
dummy.read.return_value = can_ping
# Test if pingable output is matched with True
assert check_pingable()
print('Passed case 1')

# Mock read() to return non-pingable output from cmd
dummy.read.return_value = cant_ping
# Test if non-pingable output is matched with False
assert not check_pingable()
print('Passed case 2')

# Mock read() to return non-existent output from cmd
dummy.read.return_value = cant_find
# Test if non-existant output is matched with False
assert not check_pingable()
print('Passed case 3')