# launchlog/queries.py
from .db import get_connection


def list_launches(limit: int | None = None):
    sql = """
        SELECT l.mission_name, l.launch_date,
               a.name AS agency, r.name AS rocket,
               l.destination, l.outcome
        FROM launches l
        JOIN agencies a ON l.agency_id = a.id
        JOIN rockets r  ON l.rocket_id = r.id
        ORDER BY l.launch_date DESC
    """

    params: list[object] = []
    if limit is not None:
        sql += " LIMIT %s"
        params.append(limit)

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, params)
            rows = cur.fetchall()

    # thanks to row_factory=dict_row, each row is a dict-like object
    return rows


def launches_by_year(year: int):
    sql = """
        SELECT mission_name, launch_date, destination, outcome
        FROM launches
        WHERE EXTRACT(YEAR FROM launch_date) = %s
        ORDER BY launch_date;
    """

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (year,))
            rows = cur.fetchall()

    return rows


def success_rate_by_agency():
    sql = """
        SELECT
            a.name AS agency,
            COUNT(*) AS total_launches,
            SUM(CASE WHEN l.outcome = 'success' THEN 1 ELSE 0 END) \
            AS successful_launches,
            ROUND(
                100.0 * SUM(CASE WHEN l.outcome = 'success' THEN \
                1 ELSE 0 END) / COUNT(*),
                2
            ) AS success_rate_pct
        FROM launches l
        JOIN agencies a ON l.agency_id = a.id
        GROUP BY a.id
        ORDER BY success_rate_pct DESC;
    """

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
            rows = cur.fetchall()

    return rows
