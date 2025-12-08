# tests/test_queries.py

from datetime import date

import pytest

from launchlog import queries


@pytest.fixture
def launches():
    """
    Fixture to fetch all launches once.
    Assumes the database is up and seeded.
    """
    return queries.list_launches()


def test_list_launches_returns_rows(launches):
    # Should return a list (or list-like) of rows
    assert isinstance(launches, list)
    assert len(launches) > 0

    row = launches[0]
    # Because we use psycopg row_factory=dict_row, rows should be dict-like
    assert "mission_name" in row
    assert "launch_date" in row
    assert "agency" in row
    assert "rocket" in row
    assert "destination" in row
    assert "outcome" in row


def test_list_launches_sorted_by_date_desc(launches):
    # Ensure launches are ordered by launch_date descending
    dates = [row["launch_date"] for row in launches]

    # launch_date should be a date object (psycopg + DATE column)
    for d in dates:
        assert isinstance(d, date)

    # Check that the list is sorted descending
    assert dates == sorted(dates, reverse=True)


def test_list_launches_respects_limit():
    # When a limit is passed, result length should be <= limit
    limit = 2
    rows = queries.list_launches(limit=limit)
    assert len(rows) <= limit
    assert len(rows) > 0  # we expect at least one seeded launch


@pytest.mark.parametrize("year", [2020, 2021, 2022])
def test_launches_by_year_filters_correctly(year: int):
    rows = queries.launches_by_year(year)

    # No error, rows is always a list
    assert isinstance(rows, list)

    for row in rows:
        # launch_date should be a date, and year must match
        launch_date = row["launch_date"]
        assert isinstance(launch_date, date)
        assert launch_date.year == year


def test_success_rate_by_agency_shape():
    rows = queries.success_rate_by_agency()

    assert isinstance(rows, list)
    assert len(rows) > 0

    for row in rows:
        # Ensure expected keys are present
        assert "agency" in row
        assert "total_launches" in row
        assert "successful_launches" in row
        assert "success_rate_pct" in row

        # Basic sanity checks on types/values
        assert isinstance(row["agency"], str)
        assert row["total_launches"] >= 0
        assert row["successful_launches"] >= 0
        assert 0.0 <= row["success_rate_pct"] <= 100.0


def test_success_rate_by_agency_sorted_desc():
    rows = queries.success_rate_by_agency()

    # Extract success rates and verify they are sorted descending
    rates = [row["success_rate_pct"] for row in rows]
    assert rates == sorted(rates, reverse=True)
