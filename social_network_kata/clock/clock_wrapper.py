import datetime


class ClockWrapper:

    def clock(self) -> str:
        return datetime.date.today().strftime("%d/%m/%Y")
