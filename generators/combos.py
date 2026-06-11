from generators.prefix import PrefixGenerator
from generators.suffix import SuffixGenerator


class ComboGenerator:

    @staticmethod
    def generate(word):

        results = set()

        for prefix in PrefixGenerator.PREFIXES:
            for suffix in SuffixGenerator.SUFFIXES:

                results.add(
                    f"{prefix}{word}{suffix}"
                )

        return results