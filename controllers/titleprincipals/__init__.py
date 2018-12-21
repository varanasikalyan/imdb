import platform

if platform.sys.version_info.major < 3:
	from titleprincipalscontroller import *
else:
	from .titleprincipalscontroller import *