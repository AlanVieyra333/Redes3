#!/usr/bin/python
import sys, rrdtool, time

tMinute = 60
tHour = tMinute * 60
tDay = tHour * 24
################################################################################
hostname = sys.argv[1].replace('.', '_')
fname = 'ping_' + hostname + '.rrd'
step = 1  # Time interval betwen every muestra. (1 sec)
time_average = 1  # Time interval to average. (1 sec)
################################################################################
stime = int(time.time())
duration = tHour

#ret = rrdtool.create(
#    fname,
#    '--step', str(step),
#    '--start', '0',
#    'DS:input:COUNTER:600:U:U',
#    'DS:output:COUNTER:600:U:U',
#    'RRA:AVERAGE:0.5:1:600',
#    'RRA:AVERAGE:0.5:6:700',
#    'RRA:AVERAGE:0.5:24:775',
#    'RRA:AVERAGE:0.5:288:797',
#    'RRA:MAX:0.5:1:600',
#    'RRA:MAX:0.5:6:700',
#    'RRA:MAX:0.5:24:775',
#    'RRA:MAX:0.5:444:797',
#)

# Un archivo round robin, que promedia las muestras de 5s durante una hora.
ret = rrdtool.create(
    fname,
    '--start', str(stime),
    '--step', str(step),
    'DS:ping_%s:GAUGE:3:U:U' % hostname,
    'RRA:AVERAGE:0.5:%d:%d' % (time_average, duration / time_average),
)

if ret:
  print rrdtool.error()
