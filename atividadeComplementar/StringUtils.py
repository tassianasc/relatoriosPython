class StringUtils:
    def reverse_string(self, s):
        """
        Reverte a string.
        :param s: String de entrada.
        :return: String invertida.
        """
        return s[::-1]

    def is_palindrome(self, s):
        """
        Verifica se a string é um palíndromo.
        :param s: String de entrada.
        :return: True se for palíndromo, False caso contrário.
        """
        return s == s[::-1]
