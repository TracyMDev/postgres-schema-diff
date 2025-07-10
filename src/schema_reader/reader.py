import psycopg2

def get_table_names(conn_str):
    """
    Connects to a PostgreSQL database and returns a list of (schema, table_name) tuples.
    """
    try:
        conn = psycopg2.connect(conn_str)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT table_schema, table_name
            FROM information_schema.tables
            WHERE table_type = 'BASE TABLE'
              AND table_schema NOT IN ('pg_catalog', 'information_schema')
            ORDER BY table_schema, table_name;
        """)
        results = cursor.fetchall()
        conn.close()
        return results
    except Exception as e:
        raise RuntimeError(f"Failed to fetch tables: {e}")
