from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# SQLite Connection String:
CONNECTION_STRING = "sqlite:///data.db"

# DB Engine:
engine = create_engine(CONNECTION_STRING)

# DB Session(Oturum):
Session = sessionmaker(bind=engine)

def get_session():
    return Session()