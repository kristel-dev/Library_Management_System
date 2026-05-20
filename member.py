class Member:
    def __init__(self, member_id: str, name: str, email: str):
        self._member_id: str = member_id
        self._name: str = name
        self._email: str = email

    def get_member_id(self) -> str:
        return self._member_id

    def get_name(self) -> str:
        return self._name

    def get_email(self) -> str:
        return self._email

    def __str__(self):
        return f"[{self._member_id}] {self._name} ({self._email})”
