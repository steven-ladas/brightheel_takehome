import argparse
import src.etl as etlify
from utils.utils import read_runtime_config
from config.config import Config

def handler(runtime_config):
    """
    entrypoint when run as a service
    """
    
    cfg = Config()
    cfg.set_runtime_config(runtime_config)

    source_name = cfg.runtime_config.get('source_name')

    factory = etlify.get_factory(source_name)
    etl = factory(cfg)
    etl.run()


if __name__ == '__main__':
    """
    to run locally + easy to test
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("source_name", help="origin of the lead data to be processed")
    parser.add_argument("runtime_config_filename", help="relative path to config file")

    args = parser.parse_args()

    runtime_config = read_runtime_config(args.runtime_config_filename)
    runtime_config.update(vars(args))

    handler(runtime_config)
