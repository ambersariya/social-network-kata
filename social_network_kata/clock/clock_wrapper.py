import datetime


class ClockWrapper:

    def clock(self) -> str:
        raise NotImplementedError
        #return datetime.date.today().strftime("%d/%m/%Y")
