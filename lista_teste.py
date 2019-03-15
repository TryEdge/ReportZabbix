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


hosts = zapi.host.get({
    "output": ['host', 'name', 'status'],
    "filter": {"host": 'machine1'}
})


if hosts:
	for host in hosts:
		host_id = host['hostid']
		host_name = host['host']
		host_visiblename = host['name']
		host_status = host['status']
		print('{} - {} - {} - {}'.format(host_id, host_name, host_visiblename, host_status))	

else:
    print('Host não encontrado')
