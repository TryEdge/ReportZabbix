import csv
from zabbix_api import ZabbixAPI

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



arquivo = csv.reader(open('usuarios.csv'),delimiter=';')
for [usuario,grupoid] in arquivo:
	pass

try:
	create_user = zapi.user.create({
		"alias": alias,
		"passwd": '132@mudar',
		"usrgrps": [
		{
			"usrgrpid": grupoid
		}
		]
	})
	print('Usuario  cadastrado : {}'.format(alias))
except Exception as err:
	print('Falha ao cadastrar o usuario : {}'.format(alias))

zapi.user.logout([])
