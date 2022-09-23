import platform, psutil
from screeninfo import get_monitors

data = dict()

data['os_version'] = platform.platform()
data['pc_name'] = platform.node()
data['cpu'] = platform.machine()
data['ram_size'] = round(psutil.virtual_memory().total / 1024 ** 3, 1)
for i, monitor in enumerate(get_monitors()):
    data[f'monitor_{i}'] = (monitor.width, monitor.height)

print(*map(lambda x: f'{x}: {data[x]}', data), sep='\n')
input('Press ENTER to escape')