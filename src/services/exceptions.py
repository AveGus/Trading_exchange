class UserAlreadyExistsError(Exception):
    def __init__(self):
        self.message = "Пользователь с таким именем существует"
        super().__init__(self.message)
