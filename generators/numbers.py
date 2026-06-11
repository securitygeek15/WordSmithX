class NumberGenerator:

    @staticmethod
    def generate(word):

        results = set()

        for i in range(0, 9999):
            results.add(f"{word}{i}")

        return results