import pgq
import psycopg2

DSN = "host=localhost dbname=dms user=dms password=dms"


def main():
    with psycopg2.connect(DSN) as conn:
        with conn.cursor() as curs:
            for x in range(10):
                pgq.producer.insert_event(
                    curs,
                    "notifications",
                    "welcome",
                    f"aaa-{x}",
                )


if __name__ == "__main__":
    main()
