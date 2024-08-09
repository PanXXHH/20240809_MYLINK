import re

def parse_site_config_file(filename):
    config = {}

    with open(filename, 'r') as config_file:
        lines = config_file.readlines()

    current_block = None
    for line in lines:
        line = line.strip()
        if not line or line.startswith("#"):
            continue

        if line.startswith("server"):
            current_block = 'server'
            config['server'] = {}
        elif current_block == 'server':
            match = re.match(r'^(\w+)\s+(.*)$', line)
            if match:
                key = match.group(1)
                value = match.group(2)
                config['server'][key] = value

    return config

# 解析站点配置文件
filename = 'site.conf'
parsed_config = parse_site_config_file(filename)

# 打印解析的配置信息
print(parsed_config)
