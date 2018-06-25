#!/usr/bin/python
import rrdtool, time, sys
from ping import ping
from email import sendEmail

DIR='/root/ping_poller'
hostname = sys.argv[1]
fname = DIR + '/ping_' + hostname.replace('.', '_') + '.rrd'
################################################################################

fail=0
fixing=False

# Se actualiza la bd con valores de [0, 1000] ms cada segundo.
while True:
    ping_time = ping(hostname)

    if ping_time == -1:
      ping_time=1.0
      fail=fail + 1
    else:
      fail=0
      fixing=False

    rrdtool.update(fname, 'N:%d' % ping_time)

    # Send email after 3 seconds of not ping.
    if fail>3:
      if not fixing: 
        sendEmail(hostname, 1)
      fixing=True

    time.sleep(1)
