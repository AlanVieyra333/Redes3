#!/usr/bin/python
import subprocess

email_to='alan.vieyra376@gmail.com'
email_from='alan.vieyra376@gmail.com'
subjects = ['Equipo inaccesible', 'Equipo saturado']
bodies = ['El equipo con ip X no responde.\nFavor de checar la conexion.',
          'El equipo con ip X ha rebasado el 50% de utilizacion.\nFavor de reiniciarlo o cambiarlo']


def sendEmail(hostname, option):
  subject='Subject: ' + subjects[option-1]
  body=bodies[option-1].replace('X', hostname)
      
  subprocess.Popen(
    ['swaks',
      '--to', email_to,
      '--from', email_from,
      '--header', subject,
      '--body', body,
      '--server', 'smtp.gmail.com:587',
      '--auth', 'LOGIN',
      '--auth-user', email_from,
      '--auth-password', '********',
      '-tls'],
    stdout=subprocess.PIPE
  )

################################################################################
# Example

#hostname = '10.0.1.1'
#sendEmail(hostname, 2)
