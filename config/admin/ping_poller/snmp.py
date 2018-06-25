#!/usr/bin/python
import subprocess, re

oid='.1.3.6.1.4.1.2021.10.1.3.1'

def getCPU(hostname):
  cpu=subprocess.Popen(
    ['snmpget',
      '-v', '2c',
      '-c', 'public',
      hostname,
      oid],
    stdout=subprocess.PIPE
  ).stdout.read()

  cpu = float(re.search(r'([\w|\s|.|\(|\)|\-|:|,\|=|\n]*)(STRING: ")([0-9]*.[0-9]*)(")', cpu).group(3))
  #time = int(re.search(r'([\w|\s|.|\(|\)|\-|:|,\|=|\n]*)(time=)([0-9]*)([.|0-9]*)( ms)', ping_response).group(3))

  return cpu

################################################################################
# Example

hostname = '10.0.1.1'
print getCPU(hostname)
