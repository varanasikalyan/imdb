import platform

if platform.sys.version_info.major < 3:
	from namebasicscontroller import *
else:
	from .namebasicscontroller import *