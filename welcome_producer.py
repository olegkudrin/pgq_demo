import psycopg2
from pgq.producer import insert_event

DSN = "host=localhost dbname=dms user=dms password=dms"


def main():
    with psycopg2.connect(DSN) as conn:
        with conn.cursor() as curs:
            for x in range(10):
                insert_event(curs, "notifications", "welcome", f"aaa-{x}")


if __name__ == "__main__":
    main()
