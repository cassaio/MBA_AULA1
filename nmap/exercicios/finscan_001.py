#!/usr/bin/python

import nmap3
from datetime import datetime 
from termcolor import colored

msg1 = colored('+', 'green', attrs=['blink'])
msg2 = colored('+', 'cyan')
nmap_start= datetime.now()

target = '11.11.11.171'

pynmap = nmap3.NmapScanTechniques()
finscan = pynmap.nmap_fin_scan(target)

#for _info in finscan[target]:
#    print('[' + msg1 + ']',_info['portid'],_info['protocol'],_info['state'],_info['reason'])
#
#    for chave, valor in _info['service'].items():
#        print ('--[' + msg2 + ']',chave, valor)
#    print()

print('Porta:', finscan['ports']['portid'])
print('Porta:', finscan['ports']['protocol'])
print('Porta:', finscan['ports']['service']['name'])
print('Porta:', finscan['ports']['state']['state'])

nmap_end= datetime.now()
nmap_time = nmap_end - nmap_start
print('[' + msg1 + ']','Tempo de execucao', nmap_time)

print()

