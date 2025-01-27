from sqlalchemy import MetaData, create_engine
from sqlalchemy.exc import OperationalError

from library_management.configs import env


def get_db_url() -> str:
    return 'postgresql+psycopg2://%s:%s@%s:%s/%s' % (
        env.DB_USER, env.DB_PASSWORD, env.DB_HOST, env.DB_PORT, env.DB_NAME
    )


engine = create_engine(get_db_url())


metadata = MetaData()


