import sys, rrdtool

tMinute = 60
tHour = tMinute * 60
tDay = tHour * 24
step = 1
fname = 'ping.rrd'

ret = rrdtool.create(
    fname,
    '--step', str(step),
    '--start', '0',
    'DS:input:COUNTER:600:U:U',
    'DS:output:COUNTER:600:U:U',
    'RRA:AVERAGE:0.5:1:600',
    'RRA:AVERAGE:0.5:6:700',
    'RRA:AVERAGE:0.5:24:775',
    'RRA:AVERAGE:0.5:288:797',
    'RRA:MAX:0.5:1:600',
    'RRA:MAX:0.5:6:700',
    'RRA:MAX:0.5:24:775',
    'RRA:MAX:0.5:444:797',
)

if ret:
  print rrdtool.error()
