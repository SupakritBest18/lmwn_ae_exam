import duckdb

# Connect to the DuckDB file
con = duckdb.connect('C:\\Users\\supak\\Downloads\\LMWN-AE-Exam\\Data Sources\\ae_exam_db.duckdb')

# Show all tables
tables = con.execute("SHOW TABLES").fetchall()
print("Tables:", tables)

# Optional: Automatically preview data from each table
# for (table_name,) in tables:
#     print(f"\n--- {table_name} ---")
#     df = con.execute(f"SELECT * FROM {table_name} LIMIT 5").fetchdf()
#     print(df)
