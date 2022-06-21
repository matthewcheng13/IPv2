from icmplib import ping

print(ping('7.7.7.7', 1).is_alive)
print(ping('google.com', 1).is_alive)
