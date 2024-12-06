class FibonacciGenerator:
    def generate_sequence(self, n):
        """
        Gera os primeiros n números da sequência de Fibonacci.
        :param n: Número de elementos na sequência.
        :return: Lista contendo a sequência de Fibonacci.
        """
        if n <= 0:
            return []
        
        sequence = [0, 1]
        for _ in range(2, n):  # Corrigido o loop para iniciar a partir do terceiro número.
            next_number = sequence[-1] + sequence[-2]
            sequence.append(next_number)
        return sequence[:n]

    def get_nth_number(self, n):
        """
        Retorna o enésimo número da sequência de Fibonacci (baseado em índice 1).
        :param n: Posição do número na sequência (1-indexed).
        :return: Número correspondente na sequência.
        """
        if n <= 0:
            return None
        elif n == 1:
            return 0
        elif n == 2:
            return 1
        
        a, b = 0, 1
        for _ in range(n - 2):  # Corrigido o loop para percorrer n-2 iterações.
            a, b = b, a + b
        return b
