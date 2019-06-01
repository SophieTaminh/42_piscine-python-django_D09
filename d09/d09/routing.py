from channels.routing import include
from websocketapp.routing import list_routing

channel_routing = [
	include(list_routing,path='^/List')
	]