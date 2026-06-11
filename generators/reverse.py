class ReverseGenerator:

    @staticmethod
    def generate(word):

        return {
            word[::-1],
            word[::-1].upper(),
            word[::-1].lower()
        }