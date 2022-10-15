import yaml

def read_config(config_path):
    with open(config_path) as config_path:
        content = yaml.safe_load(config_path)
    return content