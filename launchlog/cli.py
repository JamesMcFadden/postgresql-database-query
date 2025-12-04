import argparse

import launchlog.queries


def main():
    parser = argparse.ArgumentParser(description="Space Launch Log CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    p_list = subparsers.add_parser("list", help="List recent launches")
    p_list.add_argument("--limit", type=int, help="Max number of launches to show")

    p_year = subparsers.add_parser("year", help="Show launches in a given year")
    p_year.add_argument("year", type=int)

    subparsers.add_parser("success-rate", help="Show success rate by agency")

    p_dest = subparsers.add_parser("dest", help="Show launches to a destination")
    p_dest.add_argument("destination", type=str)

    args = parser.parse_args()

    if args.command == "list":
        rows = queries.list_launches(limit=args.limit)
        for row in rows:
            print(
                f"{row['launch_date']} | {row['mission_name']} "
                f"({row['agency']} / {row['rocket']}) "
                f"dest={row['destination']} outcome={row['outcome']}"
            )

    elif args.command == "year":
        rows = queries.launches_by_year(args.year)
        if not rows:
            print(f"No launches found in {args.year}")
        else:
            for row in rows:
                print(
                    f"{row['launch_date']} | {row['mission_name']} "
                    f"dest={row['destination']} outcome={row['outcome']}"
                )

    elif args.command == "success-rate":
        rows = queries.success_rate_by_agency()
        for row in rows:
            print(
                f"{row['agency']}: {row['successful_launches']}/"
                f"{row['total_launches']} = {row['success_rate_pct']}% success"
            )
