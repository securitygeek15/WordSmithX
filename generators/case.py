class CaseGenerator:

    @staticmethod
    def generate(word):

        return {
            word.lower(),
            word.upper(),
            word.title(),
            word.capitalize(),
            word.swapcase(),
        }