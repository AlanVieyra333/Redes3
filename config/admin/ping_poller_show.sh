#!/bin/bash

# Router quagga-1
/root/Redes3/Practicas/PingPoller/rrdtool-draw.py 10.0.100.1
# Router quagga-2
/root/Redes3/Practicas/PingPoller/rrdtool-draw.py 10.0.100.2
# PC-1
/root/Redes3/Practicas/PingPoller/rrdtool-draw.py 10.0.2.1
# PC-2
/root/Redes3/Practicas/PingPoller/rrdtool-draw.py 10.0.2.2
# PC-3
/root/Redes3/Practicas/PingPoller/rrdtool-draw.py 10.0.3.1
# PC-4
/root/Redes3/Practicas/PingPoller/rrdtool-draw.py 10.0.3.2

mv ping_10* Redes3/Practicas/PingPoller/
