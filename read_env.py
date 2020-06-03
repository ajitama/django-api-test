import environ
import os
from config.settings import BASE_DIR #後ほど設定

import logging
logger = logging.getLogger(__file__)

def get_env_dict(env_path):
    env = {}
    try:
        read_env = environ.Env()
        environ.Env.read_env(env_path)

        #以下に、.envファイルから読み込むパラメータについて書く。
        if read_env('DEBUG') == 'True' or True:
            env['DEBUG'] = True
        elif read_env('DEBUG') == 'False' or False:
            env['DEBUG'] = False

        #secret keys
        env['SECRET_KEY'] = read_env('SECRET_KEY')

        #DB setting
        env['DB_NAME'] = read_env('DB_NAME')
        env['DB_USER'] = read_env('DB_USER')
        env['DB_PASS'] = read_env('DB_PASS')

    except environ.ImproperlyConfigured as e:
        logger.info('設定されていないkeyが設定されている: {}'.format(e))

    except Exception as e:
        logger.info('環境変数設定のエラー: {e}'.format(e))

    return env


env_path = os.path.join(BASE_DIR, '.env')
env = get_env_dict(env_path)
