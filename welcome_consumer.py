import sys
from typing import Sequence

from pgq import Consumer

from skytools.basetypes import Connection

from pgq.event import Event


class WelcomeConsumer(Consumer):
    def __init__(self, args: Sequence[str]):
        super().__init__("welcome_app", "src_db", args)

    def process_event(self, db: Connection, event: Event) -> None:
        if event.ev_type == "welcome":
            self.log.info("Welcome %s!" % event.ev_data)
        event.tag_done()


if __name__ == "__main__":
    script = WelcomeConsumer(sys.argv[1:])
    script.start()
