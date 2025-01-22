from sqlalchemy import MetaData, create_engine
from library_management.configs import env
from sqlalchemy.exc import OperationalError
def get_db_url() -> str:
    return 'postgresql+psycopg2://%s:%s@%s:%s/%s' % (
        env.DB_USER, env.DB_PASSWORD, env.DB_HOST, env.DB_PORT, env.DB_NAME
    )


engine = create_engine(get_db_url())


metadata = MetaData()


try:
    # Try connecting to the database
    connection = engine.connect()
    print("Connection successful!")
    connection.close()
except OperationalError as e:
    print(f"Error connecting to the database: {e}")