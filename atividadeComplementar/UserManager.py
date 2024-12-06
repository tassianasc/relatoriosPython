class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        if user not in self.users:
            self.users.append(user)
        else:
            return "User already exists"

    def remove_user(self, user):
        """
        Remove um usuário da lista.
        :param user: Nome do usuário.
        :return: Mensagem de erro se o usuário não existir.
        """
        if user in self.users:
            self.users.remove(user)
        else:
            return "User not found"
