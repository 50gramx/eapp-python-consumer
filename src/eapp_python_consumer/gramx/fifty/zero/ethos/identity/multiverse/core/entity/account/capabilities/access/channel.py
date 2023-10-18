import grpc

import yaml

CONFIG_FILE_PATH = "/opt/ethos/apps/service/eapp-python-consumer/src/eapp_python_consumer/gramx/fifty/zero/ethos/identity/multiverse/developer_config.yaml"


def create_developer_channel(service_name, insecure=True):
    with open(CONFIG_FILE_PATH, 'r') as config_file:
        developer_config = yaml.safe_load(config_file)
    config = developer_config[service_name]
    if not insecure:
        developer_certificate_path = config['developer_certificate_path']
        ssl_credentials = grpc.ssl_channel_credentials(open(developer_certificate_path, 'rb').read())
        return grpc.secure_channel(f"{config['host']}:{config['port']}", ssl_credentials)
    else:
        return grpc.insecure_channel(f"{config['host']}:{config['port']}")
