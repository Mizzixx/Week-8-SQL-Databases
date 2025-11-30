
from pathlib import Path
import pandas as pd

from app.data.db import connect_database
from app.data.schema import create_all_tables
from app.services.user_service import register_user, login_user
from app.data.incidents import insert_incident, get_all_incidents

# Create folder for all CSV files
DATA_DIR = Path("DATA")
DATA_DIR.mkdir(exist_ok=True)


def load_all_csv_data(conn):
    """
    Reads all CSV files from the DATA folder and inserts them into their
    matching database tables after converting each row into the fields
    expected by the database.
    """
    csv_to_table = {
        "cyber_incidents.csv": "cyber_incidents",
        "datasets_metadata.csv": "datasets_metadata",
        "it_tickets.csv": "it_tickets"
    }

    total_loaded = 0

    for filename, table in csv_to_table.items():
        file_path = DATA_DIR / filename

        if not file_path.exists():
            print(f"Skipped (file not found): {filename}")
            continue

        try:
            df = pd.read_csv(file_path)
            print(f"\nLoaded {filename}")
            print("Columns:", list(df.columns))
            print("Sample row:", df.iloc[0].to_dict())

            # Map CSV → database structure
            mapped_rows = []

            for _, row in df.iterrows():
                if table == "cyber_incidents":
                    mapped_rows.append({
                        "date_reported": row.get("Date", "2024-01-01"),
                        "incident_type": row.get("Type", "Unknown"),
                        "severity": "Medium",
                        "status": "Open",
                        "description": f"{row.get('Title', '')} - {row.get('Description', '')}",
                        "reported_by": "System"
                    })

                elif table == "datasets_metadata":
                    mapped_rows.append({
                        "dataset_name": row.get("dataset_name", "Unnamed Dataset"),
                        "source": row.get("source_organization", "Unknown Source"),
                        "record_count": 0,
                        "last_updated": row.get("last_updated", "2024-01-01"),
                        "description": row.get("description", "No description")
                    })

                elif table == "it_tickets":
                    mapped_rows.append({
                        "ticket_id": f"TICKET_{_ + 1000}",
                        "date_created": "2024-01-01",
                        "priority": row.get("Category", "Medium"),
                        "status": "Open",
                        "description": row.get("Customer Input", "No description"),
                        "assigned_to": "Unassigned"
                    })

            mapped_df = pd.DataFrame(mapped_rows)
            print(f"Prepared {len(mapped_df)} rows for {table}")

            if not mapped_df.empty:
                mapped_df.to_sql(table, conn, if_exists="replace", index=False)
                total_loaded += len(mapped_df)
                print(f"Inserted {len(mapped_df)} rows into {table}")

        except Exception as err:
            print(f"Error processing {filename}: {err}")

    return total_loaded


def setup_database_complete():
    """Creates tables, loads CSV data, and prints a summary."""
    print("\n" + "=" * 60)
    print("Database Setup Started")
    print("=" * 60)

    conn = connect_database()
    create_all_tables(conn)

    total = load_all_csv_data(conn)
    print(f"\nTotal rows imported: {total}")

    # Display table counts
    cursor = conn.cursor()
    summary_tables = ["users", "cyber_incidents", "datasets_metadata", "it_tickets"]

    print("\nDatabase Summary:")
    for tbl in summary_tables:
        cursor.execute(f"SELECT COUNT(*) FROM {tbl}")
        amount = cursor.fetchone()[0]
        print(f" - {tbl}: {amount} rows")

    conn.close()
    print("\nDatabase setup complete.\n")


def main():
    print("=" * 60)
    print("Week 8 — Database Demonstration")
    print("=" * 60)

    setup_database_complete()

    # Test User Features
    print("\n--- Authentication Tests ---")
    success, msg = register_user("alice", "SecurePass123!", "analyst")
    print("Register:", msg)

    success, msg = login_user("alice", "SecurePass123!")
    print("Login:", msg)

    # Create sample incident
    print("\n--- CRUD Test ---")
    inc_id = insert_incident(
        "2024-11-05",
        "Phishing",
        "High",
        "Open",
        "Test incident",
        "alice"
    )
    print(f"Created example incident #{inc_id}")

    # Check dataset
    incidents_df = get_all_incidents()
    print(f"Total incidents stored: {len(incidents_df)}")

    print("\n" + "=" * 60)
    print("System Ready")
    print("=" * 60)


if __name__ == "__main__":
    main()


# Quick CSV check (optional)
df = pd.read_csv("DATA/cyber_incidents.csv")
print("Columns:", df.columns.tolist())
print("First row:", df.iloc[0].to_dict())