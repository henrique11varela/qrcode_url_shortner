from sqlalchemy import create_engine, text
import uuid

myuuid = uuid.uuid4()

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)

with engine.connect() as conn:
    conn.execute(text("CREATE TABLE some_table (x int, y int, z text)"))
    conn.execute(
        text("INSERT INTO some_table (x, y, z) VALUES (:x, :y, :z)"),
        [{"x": 1, "y": 1, "z": f'{myuuid}'}, {"x": 2, "y": 4, "z": "test"}],
    )
    conn.commit()

with engine.connect() as conn:
    result = conn.execute(text("SELECT x, y, z FROM some_table"))
    for row in result:
        print(f"x: {row.x}  y: {row.y}  z: {row.z}")

with engine.connect() as conn:
    result = conn.execute(text("SELECT x, y FROM some_table WHERE z LIKE :t"), {"t": f'{myuuid}'})
    for row in result:
        print(f"x: {row.x}  y: {row.y}")