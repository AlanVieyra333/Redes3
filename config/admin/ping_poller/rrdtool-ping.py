#!/usr/bin/python
import rrdtool, time, sys
from ping import ping
from email import sendEmail
from snmp import getCPU

DIR='/root/ping_poller'
hostname = sys.argv[1]
fname = DIR + '/ping_' + hostname.replace('.', '_') + '.rrd'
################################################################################

fail=0
failCPU=0

# Se actualiza la bd con valores de [0, 1000] ms cada segundo.
while True:
    ping_time = ping(hostname)

    if ping_time == -1:
      ping_time=1.0
      fail=fail + 1
    else:
      fail=0
      cpu=getCPU(hostname)
      
      if cpu > 0.5:
        failCPU=failCPU + 1
      else:
        failCPU=0

    rrdtool.update(fname, 'N:%d' % ping_time)

    # Send email after 3 seconds of not ping.
    if fail==3:
      sendEmail(hostname, 1)

    # send email after 3 second of CPU eigher
    if failCPU==3:
      sendEmail(hostname, 2)      

    time.sleep(1)
