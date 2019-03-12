from zabbix_api import ZabbixAPI

URL = 'http://zabbix.fortalnet.net.br/zabbix/api_jsonrpc.php'
USERNAME = 'zabbix'
PASSWORD = ''

zapi = ZabbixAPI(URL, timeout=180)
zapi.login(USERNAME, PASSWORD)
print('Conectado na API do Zabbix, versao: {}'.format(zapi.api_version()))
