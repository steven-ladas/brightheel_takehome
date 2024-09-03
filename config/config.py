import os

class MissingEnvironmentError(Exception):
    """
    raise this when cant find required environment
    """
    pass

class Config:
    """
    environment sponge for config
    bails out immediately if it can't find something it needs
    """

    def __init__(self):

        self._env = os.environ
        self.runtime_config = None

        # required env

        #MySQL DB loader
        self.mysql_host = self.get_env_var('MYSQL_HOST')
        self.mysql_user = self.get_env_var('MYSQL_USER')
        self.mysql_password = self.get_env_var('MYSQL_PASSWORD')
        self.mysql_port = self.get_env_var('MYSQL_PORT')
        self.mysql_db = self.get_env_var('MYSQL_DB')
        self.mysql_destination_table_name = self.get_env_var('MYSQL_DESTINATION_TABLE_NAME')

        #AWS
        #self.aws_access_key_id = self.get_env_var('AWS_ACCESS_KEY_ID')
        #self.aws_secret_access_key = self.get_env_var('AWS_SECRET_ACCESS_KEY')


    def set_runtime_config(self, config):
        self.runtime_config = config

    def get_env_var(self,env_key):
        """
        assign all required environment using this function in the constructor 
        """
        try:
            return self._env[env_key]
        except KeyError:
            raise MissingEnvironmentError(f'{env_key} required in environment')
        
