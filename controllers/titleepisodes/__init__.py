import platform

if platform.sys.version_info.major < 3:
	from titleepisodescontroller import *
else:
	from .titleepisodescontroller import *