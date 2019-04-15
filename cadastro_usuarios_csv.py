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

usergroups = zapi.usergroup.get({
	"output": ['name'],
	"selectUsers":['alias']

})

if usergroups:
	for usergroup in usergroups:
		usergroup_name = usergroup['name']
		usergroup_users = usergroup['users']
		if usergroup_users:
			for user in usergroup_users:
					user_alias = user['alias']
					print('{} - {}'.format(usergroup_name,user_alias))



zapi.user.logout([])
