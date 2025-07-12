from sqlalchemy import text, CursorResult
from connect import engine

def db_query(query: str, values: list | dict | None = None):
    with engine.connect() as conn:
        try:
            if values == None:
                cursor = conn.execute(text(f"{query}"))
                conn.commit()
            else:
                cursor = conn.execute(text(f"{query}"), values)
                conn.commit()

            if cursor.returns_rows:
                result = cursor.fetchall()
                return result
            else:
                return True

        except Exception as e:
            print('----')
            print(e)
            print('----')
            return False

if __name__ == '__main__':
        a = db_query("INSERT INTO test_table (test) VALUES (:test)", [{"test": f'qwe'}, {"test": "qwe2"}])
        print(a)

        b = db_query("SELECT * FROM test_table WHERE test LIKE :t", {"t": 'qwe'})
        print(b)