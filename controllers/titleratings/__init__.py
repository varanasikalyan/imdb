import platform

if platform.sys.version_info.major < 3:
	from titleratingscontroller import *
else:
	from .titleratingscontroller import *