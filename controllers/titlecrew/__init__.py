import platform

if platform.sys.version_info.major < 3:
	from titlecrewcontroller import *
else:
	from .titlecrewcontroller import *