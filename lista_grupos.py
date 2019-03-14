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


hostgroups = zapi.hostgroup.get({
    "output": ['name'],
    "monitored_hotst": 1
})


for hostgroup in hostgroups:
    hostgroup_id = hostgroup['groupid']
    hostgroup_name = hostgroup['name']
    print('{} - {} '.format(hostgroup_id, hostgroup_name))
