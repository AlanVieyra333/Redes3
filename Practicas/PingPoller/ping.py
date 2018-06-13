import subprocess, re

def ping(hostname):
  ping_response = subprocess.Popen(
      ['ping', '-c1', '-w1', hostname],
      stdout=subprocess.PIPE
  ).stdout.read()

  # Verify packet recived.
  packets_recived = int(re.search(
      r'([\w|\s|.|\(|\)|\-|:|,\|=|\n]*)([0|1])( received)', ping_response)
      .group(2))

  if (packets_recived == 1):
    time = int(re.search(
        r'([\w|\s|.|\(|\)|\-|:|,\|=|\n]*)(time=)([0-9]*)( ms)', ping_response)
        .group(3))
    return time
  else:
    return -1

################################################################################
################################################################################

hostname = 'google.com'
#hostname = '133.133.133.1'

time = ping(hostname)

if time != -1:
  print 'Tiempo: %d ms' % time
else:
  print 'Host: ' + hostname + ', not found.'
