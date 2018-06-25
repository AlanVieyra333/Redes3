#!/usr/bin/python
import rrdtool, time, sys
from ping import ping

hostname = sys.argv[1]
fname = 'ping_' + hostname.replace('.', '_') + '.rrd'
################################################################################

# Se actualiza la bd con valores de [0, 1000] ms cada segundo.
#while True:
ping_time = ping(hostname)

if ping_time == -1:
    ping_time=1.0

rrdtool.update(fname, 'N:%d' % ping_time)

#rrdtool.update(
#    fname,
#    '-t', 'ping_%s' % hostname.replace('.', '_'),
#    '%d:%d' % (int(time.time()), ping_time)
#)
#time.sleep(1)

