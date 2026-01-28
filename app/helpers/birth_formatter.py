from datetime import datetime, date

class BirthFormatter:
    @staticmethod
    def format(birth: str) -> date:
        return datetime.strptime(birth.strip(), "%d/%m/%Y").date()
