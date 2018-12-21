import platform

if platform.sys.version_info.major < 3:
	from titleakascontroller import *
else:
	from .titleakascontroller import *