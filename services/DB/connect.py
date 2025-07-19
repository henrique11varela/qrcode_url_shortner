from sqlalchemy import create_engine, text
import os

engine = None

def create_db_connection(file_path: str, create_db_commands: list[str], echo: bool = False):
    global engine

    db_path_list = file_path.split('/')
    db_path = os.path.join(*db_path_list)

    new_db = False
    if not os.path.exists(db_path):
        os.makedirs(os.path.join(*db_path_list[:-1]))
        with open(db_path, 'w') as fp:
            pass
        new_db = True
        print('Created DB file')

    engine = create_engine(f"sqlite+pysqlite:///{os.path.abspath(db_path)}", echo=echo)

    if new_db:
        with engine.connect() as conn:
            for comm in create_db_commands:
                conn.execute(text(comm))
            

            # conn.execute(text("CREATE TABLE test_table (id INTEGER PRIMARY KEY ASC, test TEXT)"))
            
  
            conn.commit()

if __name__ == '__main__':
    file_path = 'database/db.db'

    create_db_commands = [
        """
        CREATE TABLE users (
            id INTEGER,
            username TEXT,
            password TEXT,
            email TEXT,
            image TEXT,
            PRIMARY KEY (id)
        )
        """,
        """
        CREATE TABLE sessions (
                    user_id INTEGER,
                    token TEXT,
                    expiration_date INT,
                    FOREIGN KEY (user_id) REFERENCES users (id),
                    PRIMARY KEY (user_id, token)
        """,
        """
        CREATE TABLE sessions (
                    user_id INTEGER,
                    token TEXT,
                    expiration_date INT,
                    FOREIGN KEY (user_id) REFERENCES users (id),
                    PRIMARY KEY (user_id, token)
                )
        """,
        """
CREATE TABLE domains (
                    id INTEGER PRIMARY KEY ASC,
                    domain TEXT
                )
        """,
        """
CREATE TABLE links (
                    domain_id INTEGER,
                    uuid TEXT,
                    target_link TEXT,
                    expires_at INTEGER,
                    hidden INTEGER,
                    number_of_visits INTEGER,
                    user_id TEXT,
                    FOREIGN KEY (domain_id) REFERENCES domains (id)
                    FOREIGN KEY (user_id) REFERENCES users (id)
                    PRIMARY KEY (domain_id, uuid)
                );
        """,
        """
INSERT INTO users
                    (username, password, email)
                VALUES
                    ('henrique', 'example', 'email@example.pt')
        """,
        """
  INSERT INTO domains
                    (domain)
                VALUES
                    ('henriquevarela.app')
""",
    ]

    create_db_connection(file_path=file_path, create_db_commands=create_db_commands)