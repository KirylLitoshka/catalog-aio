import pathlib
import yaml

BASE_DIR = pathlib.Path(__file__).parent.parent
TEMPLATE_DIR = BASE_DIR / 'templates'
STATIC_DIR = BASE_DIR / 'static'
CONFIG_PATH = BASE_DIR / 'config' / 'test_config.yaml'


def get_config(path):
    with open(path) as file:
        config = yaml.safe_load(file)
    return config
