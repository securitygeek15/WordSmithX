class PrefixGenerator:
    PREFIXES = [
    "the",
    "real",
    "official",
    "its",
    "my",
    "our",
    "weare",
    "team",
    "join",
    "get",
    "go",
    "try",
    "use",
    "best",
    "top",
    "elite",
    "prime",
    "ultra",
    "super",
    "mega",
    "hyper",
    "next",
    "future",
    "smart",
    "quick",
    "fast",
    "easy",
    "pro",
    "dev",
    "code",
    "build",
    "launch",
    "digital",
    "online",
    "global",
    "urban",
    "modern",
    "alpha",
    "beta",
    "nova",
    "neo",
    "x",
    "mr",
    "mrs",
    "dr",
    "captain",
    "hey",
    "hello",
    "hi",
    "officially"
]

    @classmethod
    def generate(cls, word):

        results = set()

        for prefix in cls.PREFIXES:
            results.add(prefix + word)

        return results