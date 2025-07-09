# PostgreSQL Schema Diff Tool

A lightweight command-line tool that compares a live PostgreSQL database schema against a set of SQL files in version control and generates SQL scripts to reconcile the differences.

## 🔧 Features

- Compare live PostgreSQL database schema with SQL files
- Detect changes in tables, columns, indexes, functions, and constraints
- Generate migration SQL scripts
- Dry-run mode to preview changes

## 📦 Installation

```bash
pip install -r requirements.txt
```

## 🚀 Usage

```bash
# Compare a DB to a folder of .sql files
pgschemadiff --db "postgresql://user:pass@host:port/db" --scripts ./db_scripts

# Output migration script
pgschemadiff --output ./migrations/changes.sql

# Dry-run mode
pgschemadiff --dry-run
```

## 📁 Project Structure

- `src/` – Source code
  - `schema_reader/` – Connects to DB and retrieves current schema
  - `file_parser/` – Parses SQL files into in-memory structures
  - `comparator/` – Compares DB schema and SQL files
  - `script_generator/` – Generates the SQL diff output
  - `cli.py` – Command-line interface
- `tests/` – Unit tests
- `example_project/` – Sample .sql schema for testing

## 🛠 Requirements

- Python 3.8+
- `psycopg2`
- `sqlparse`
- `click`

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Contributions are welcome! Open an issue or submit a pull request to get started.
