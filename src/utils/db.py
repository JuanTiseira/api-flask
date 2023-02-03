"""
"""

import os



def get_connection_url() -> str:
    """
    
    """
    try:
        env = os.environ["ENV"]
    except KeyError:
        env = "prod"

    # Local development credentials aren't stored in a Secret
    if env in {"local"}:
        return os.environ['PG_DATABASE_URL']

    if env == "test":
        return os.environ['PG_DATABASE_URL']

    hostname = os.environ['DB_HOST']
    username = os.environ['DB_USER']
    password = os.environ['DB_PASSWORD']
    database = os.environ['DB_NAME']

    return f"postgresql+psycopg2://{username}:{password}@{hostname}/{database}"