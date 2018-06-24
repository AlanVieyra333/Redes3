#!/bin/sh

# Comprobar numero de argumentos.
if [ -z "$1"] ; then
	echo "Uso: ./get_backups.sh <IP> <NAME_ROUTER>"
	exit 1
fi

# Crear respaldo en el enrutador.
nc -v ${1} 443 << EOF
vtysh -c write
filetool.sh -b
cp /mnt/sda1/tce/mydata.tgz /home/tc
exit
EOF

# Obtener el respaldo creado anteriormente.
ftp -in ${1} << EOF
quote USER tc
quote PASS ""
bin
get mydata.tgz
bye
EOF

# Renombrar y mover el respaldo del enrutador.
mv mydata.tgz Redes3/config/router/${2}/mydata_$(date +%Y-%m-%d_%H-%M-%S).tgz
#tar -zcvf /root/ftp/quagga-1_$(date +%Y-%m-%d_%H-%M-%S).tar.gz /etc/quagga/
