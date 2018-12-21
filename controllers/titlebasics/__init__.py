import platform

if platform.sys.version_info.major < 3:
	from titlebasicscontroller import *
else:
	from .titlebasicscontroller import *