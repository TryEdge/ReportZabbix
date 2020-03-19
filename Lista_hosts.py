#coding:utf-8
import csv
from zabbix_api import ZabbixAPI
from datetime import date
URL = 'http://zabbix/zabbix/api_jsonrpc.php'
USERNAME = 'user_zabbix'
PASSWORD = 'user_zabbix_pass'
data_atual = date.today().strftime('%d-%m-%Y')
header=["ID","HOST","NOME VISIVEL","STATUS"]
try:
	zapi = ZabbixAPI(URL, timeout=180)
	zapi.login(USERNAME, PASSWORD)
	print('Conectado na API do Zabbix, versao: {}'.format(zapi.api_version()))

except Exception as err:
	print('Falha ao Conectar na API no Zabbix')
	print('Erro: {}'.format(err))


# print("TODOS OS GRUPOS\n")
# hostgroups = zapi.hostgroup.get({
#     "output": ['name'],
#     "monitored_hotst": 1
# })
#
#
# for hostgroup in hostgroups:
#     hostgroup_id = hostgroup['groupid']
#     hostgroup_name = hostgroup['name']
#     print('{} - {} '.format(hostgroup_id, hostgroup_name))

print("\nTODOS OS HOSTS")
hosts = zapi.host.get({
	"output": ['host', 'name', 'status']
	})

if hosts:
	for host in hosts:
		host_id = host['hostid']
		host_name = host['host']
		host_visiblename = host['name']
		host_status = host['status']
		print('{} - {} - {} - {}'.format(host_id, host_name, host_visiblename, host_status))


with open('zabbix_list_host-'+data_atual+'.csv', mode='w') as file:
   output = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
   output.writerow(header)
   for host in hosts:
      row=[host['hostid'],host['host'],host['name'],host['status']]
      output.writerow(row)
