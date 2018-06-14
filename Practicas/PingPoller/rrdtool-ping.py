#!/usr/bin/python
import rrdtool, time, sys
from ping import ping

fname = 'ping.rrd'
#hostname = '10.0.1.254'
#hostname = 'google.com'
hostname = sys.argv[1]
################################################################################

# Se actualiza la bd con valores de [0, 1000] ms cada segundo.
#while True:
ping_time = ping(hostname)
#rrdtool.update(fname, 'N:%d' % ping_time)

rrdtool.update(
    fname,
    '-t', 'ping_%s' % hostname.replace('.', '_'),
    '%d:%d' % (int(time.time()), ping_time)
)
#time.sleep(1)

