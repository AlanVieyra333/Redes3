#!/bin/python
import rrdtool , time , random, sys

tMinute = 60
tHour = tMinute * 60
tDay = tHour * 24
################################################################################
hostname = sys.argv[1].replace('.', '_')
fname = 'ping.rrd'
gfname = 'ping_' + hostname + '.png'
duration = 10 * tMinute
step = 1  # One second.
time_average = 10  # Time interval to average. (10 sec)
################################################################################
dpoints = duration / step
etime = int(time.time())
stime = etime - dpoints

rrdtool.graph(
    gfname,
    '--imgformat', 'PNG',
    '-w', '1100',
    '-h', '300',
    '--title', 'Pings',
    '--vertical-label', 'Tiempo (s)',
    '--lower-limit', '0',
    '--start', str(stime - 1),
    '--end', str(etime + 1),
    'DEF:rate=%s:ping_%s:AVERAGE' % (fname, hostname),
    'CDEF:ms=rate',
    'VDEF:msmax=ms,MAXIMUM',
    'VDEF:msavg=ms,AVERAGE',
    'VDEF:msmin=ms,MINIMUM',
    'LINE1:ms#FF0000:Retardo',
    r'GPRINT:msmax:Max\: %6.1lf ms',
    r'GPRINT:msavg:Prom\: %6.1lf ms',
    r'GPRINT:msmin:Min\: %6.1lf ms\l',
)
