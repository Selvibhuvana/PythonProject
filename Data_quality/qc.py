

import sqlite3


def run_data_quality_checks():
    # 1. Connect to your SQLite database
    # Replace 'my_database.db' with the actual path to your DB file
    conn = sqlite3.connect(r"C:\Users\selvi\PycharmProjects\PythonProject\sqlite.db")
    cursor = conn.cursor()

    print("--- Starting Data Quality Checks ---")
    failures = 0

    # CHECK 1: Look for NULL emails
    cursor.execute("SELECT COUNT(*) FROM users WHERE email IS NULL")
    null_count = cursor.fetchone()[0]

    if null_count > 0:
        print(f"❌ FAIL: Found {null_count} rows with missing emails.")
        failures += 1
    else:
        print("✅ PASS: No missing emails found.")

    # CHECK 2: Look for duplicate user_ids
    cursor.execute("""
        SELECT COUNT(*) FROM (
            SELECT user_id FROM users GROUP BY user_id HAVING COUNT(*) > 1
        )
    """)
    duplicate_count = cursor.fetchone()[0]

    if duplicate_count > 0:
        print(f"❌ FAIL: Found {duplicate_count} duplicate user_id(s).")
        failures += 1
    else:
        print("✅ PASS: All user_ids are unique.")

    # 3. Summary
    print("------------------------------------")
    if failures > 0:
        print(f"DQ Run Completed: {failures} check(s) failed. Action required!")
    else:
        print("DQ Run Completed: All checks passed smoothly!")

    conn.close()


if __name__ == "__main__":
    run_data_quality_checks()