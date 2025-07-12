from sqlalchemy import create_engine, text
import os

db_path_list = ['database', 'db.db']
db_path = os.path.join(*db_path_list)

new_db = False
if not os.path.exists(db_path):
    os.makedirs(os.path.join(*db_path_list[:-1]))
    with open(db_path, 'w') as fp:
        pass
    new_db = True
    print('Created DB file')

engine = create_engine(f"sqlite+pysqlite:///{os.path.abspath(db_path)}", echo=True)

if new_db:
    with engine.connect() as conn:
        conn.execute(text("CREATE TABLE test_table (id INTEGER PRIMARY KEY ASC, test TEXT)"))
        conn.commit()






