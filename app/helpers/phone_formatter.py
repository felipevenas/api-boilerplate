class PhoneFormatter:
    @staticmethod
    def format(phone: str) -> str:
        """ Formata um número de telefone para (XX) XXXXX-XXXX """
        phone = "".join(filter(str.isdigit, phone))
        if len(phone) == 11:
            return f"({phone[:2]}) {phone[2:7]}-{phone[7:]}"
        return phone