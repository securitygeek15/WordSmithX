class SeparatorGenerator:

    SEPARATORS = [
        "_",
        "-",
        ".",
        "~",
    ]

    @classmethod
    def generate(cls, word):

        results = set()

        for sep in cls.SEPARATORS:

            results.add(word + sep)
            results.add(sep + word)

        return results