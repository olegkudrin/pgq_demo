import sys
from typing import Sequence

import pgq

from skytools.basetypes import Connection

from pgq.event import Event


class WelcomeConsumer(pgq.Consumer):
    def __init__(self, args: Sequence[str]):
        pgq.Consumer.__init__(self, "welcome_app", "src_db", args)

    def process_event(self, db: Connection, ev: Event) -> None:
        if ev.ev_type == "welcome":
            self.log.info("Welcome %s!" % ev.ev_data)
        ev.tag_done()


if __name__ == "__main__":
    script = WelcomeConsumer(sys.argv[1:])
    script.start()
