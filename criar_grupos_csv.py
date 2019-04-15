import csv
from zabbix_api import ZabbixAPI, Already_Exists

URL = 'http://zabbix.fortalnet.net.br/zabbix/api_jsonrpc.php'
USERNAME = 'zabbix'
PASSWORD = ''

try:
	zapi = ZabbixAPI(URL, timeout=180)
	zapi.login(USERNAME, PASSWORD)
	print('Conectado na API do Zabbix, versao: {}'.format(zapi.api_version()))



except Exception as err:
	print('Falha ao Conectar na API no Zabbix')
	print('Erro: {}'.format(err))




def hostgroup_create(name):
	try:
		create_hostgroup = zapi.hostgroup.create({
			"name": name
		})
		print('Grupo  {}  cadastrado  '.format(name))
	except Already_Exists:
		print('Grupo {} já cadastrado'.format(name))
	except Exception as err:
		print('Falha ao cadastrar grupo : {}'.format(name))

arquivo = csv.reader(open('grupos.csv'),delimiter=';')
for [name] in arquivo:
	hostgroup_create(name)


zapi.user.logout([])
