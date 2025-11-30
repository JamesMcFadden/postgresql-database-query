# launchlog/queries.py
from .db import get_connection, get_cursor_dict

def list_launches(limit: int | None = None):
    conn = get_connection()
    cur = get_cursor_dict(conn)

    sql = """
        SELECT l.mission_name, l.launch_date,
               a.name AS agency, r.name AS rocket,
               l.destination, l.outcome
        FROM launches l
        JOIN agencies a ON l.agency_id = a.id
        JOIN rockets r  ON l.rocket_id = r.id
        ORDER BY l.launch_date DESC
    """

    params = []
    if limit:
        sql += " LIMIT %s"
        params.append(limit)

    cur.execute(sql, params)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def launches_by_year(year: int):
    conn = get_connection()
    cur = get_cursor_dict(conn)

    # launch_date is DATE, so cast to text and use substring
    sql = """
        SELECT mission_name, launch_date, destination, outcome
        FROM launches
        WHERE EXTRACT(YEAR FROM launch_date) = %s
        ORDER BY launch_date;
    """

    cur.execute(sql, (year,))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def success_rate_by_agency():
    conn = get_connection()
    cur = get_cursor_dict(conn)

    sql = """
        SELECT
            a.name AS agency,
            COUNT(*) AS total_launches,
            SUM(CASE WHEN l.outcome = 'success' THEN 1 ELSE 0 END) AS successful_launches,
            ROUND(
                100.0 * SUM(CASE WHEN l.outcome = 'success' THEN 1 ELSE 0 END) / COUNT(*),
                2
            ) AS success_rate_pct
        FROM launches l
        JOIN agencies a ON l.agency_id = a.id
        GROUP BY a.id
        ORDER BY success_rate_pct DESC;
    """

    cur.execute(sql)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows
