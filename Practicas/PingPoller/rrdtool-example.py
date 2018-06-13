import rrdtool , time , random

tMinute = 60
tHour = tMinute * 60
tDay = tHour * 24
################################################################################
fname = 'test.rrd'
gfname = 'test.png'
duration = tHour
step = 1  # One second.
time_average = 10  # Time interval to average. (10 sec)
################################################################################
dpoints = duration / step
stime = int(time.time())
etime = stime + dpoints


# Un archivo round robin, que promedia las muestras de 5s durante una hora.
rrdtool.create(
    'test.rrd',
    '--start', str(stime),
    '--step', str(step),
    'DS:ping:GAUGE:3s:U:U',
    'RRA:AVERAGE:0.5:%d:%d' % (time_average, duration / time_average),
)

time = stime + 1
# Se crea una lista de n puntos, con valores de [10, 1000] ms.
for i in xrange(dpoints):
    ping_time = random.randint(10, 1000)
    #rrdtool.update(fname, 'N:%d' % ping_time)
    #time.sleep(1)
    rrdtool.update(fname, '%d:%d' % (time, ping_time))
    time += 1

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
    'DEF:rate=%s:ping:AVERAGE' % fname,
    'CDEF:ms=rate',
    'VDEF:msmax=ms,MAXIMUM',
    'VDEF:msavg=ms,AVERAGE',
    'VDEF:msmin=ms,MINIMUM',
    'LINE1:ms#FF0000:Retardo',
    r'GPRINT:msmax:Max\: %6.1lf ms',
    r'GPRINT:msavg:Prom\: %6.1lf ms',
    r'GPRINT:msmin:Min\: %6.1lf ms\l',
)
