from datetime import datetime


def insert_account_snapshot(conn, data):
    sql = """
    INSERT INTO account_snapshot
    (account_id, balance, equity, unrealized_pnl, currency, ts)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    ts_value = datetime.fromisoformat(data["ts"]).strftime("%Y-%m-%d %H:%M:%S")

    values = (
        data["account_id"],
        data["balance"],
        data["equity"],
        data["unrealized_pnl"],
        data["currency"],
        ts_value
    )

    with conn.cursor() as cursor:
        cursor.execute(sql, values)

    conn.commit()