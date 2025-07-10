
import click
import os
import sys
from urllib.parse import urlparse
from schema_reader import get_table_names


@click.command()
@click.option('--db', required=True, help='PostgreSQL connection string')
@click.option('--scripts', required=True, type=click.Path(exists=True), help='Path to folder containing SQL files')
@click.option('--output', default='diff_output.sql', help='Output file for generated diff SQL script')
@click.option('--dry-run', is_flag=True, help='Run without writing output, just show planned changes')
def main(db, scripts, output, dry_run):
    click.echo("🔍 Starting schema diff...")

    try:
        if not db.startswith("postgresql://"):
            raise ValueError("Invalid PostgreSQL connection string. It must start with 'postgresql://'")

        if not os.path.isdir(scripts):
            raise FileNotFoundError(f"The specified scripts path '{scripts}' is not a valid directory.")

        click.echo(f"📦 DB connection: {db}")
        click.echo(f"📂 SQL files directory: {scripts}")
        click.echo(f"📄 Output file: {output}")
        click.echo(f"🧪 Dry run: {'Yes' if dry_run else 'No'}")

        # Call schema reader to get list of tables
        click.echo("🔗 Connecting to database and fetching tables...")
        tables = get_table_names(db)
        click.echo("📋 Found the following tables:")
        for schema, table in tables:
            click.echo(f"  - {schema}.{table}")

        # TODO: Call file_parser, comparator, script_generator modules
        click.echo("🚧 Feature implementation pending.")

    except ValueError as ve:
        click.secho(f"❌ Error: {ve}", fg='red')
        sys.exit(1)

    except FileNotFoundError as fe:
        click.secho(f"❌ Error: {fe}", fg='red')
        sys.exit(1)

    except Exception as e:
        click.secho(f"❌ Unexpected error: {e}", fg='red')
        sys.exit(1)


if __name__ == '__main__':
    main()