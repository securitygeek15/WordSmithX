class SuffixGenerator:

    SUFFIXES = [
    "hub",
    "world",
    "zone",
    "verse",
    "labs",
    "studio",
    "works",
    "tech",
    "dev",
    "pro",
    "plus",
    "media",
    "network",
    "group",
    "team",
    "club",
    "community",
    "central",
    "space",
    "base",
    "point",
    "spot",
    "online",
    "digital",
    "solutions",
    "systems",
    "services",
    "academy",
    "school",
    "learn",
    "guide",
    "master",
    "expert",
    "guru",
    "creator",
    "design",
    "creative",
    "project",
    "factory",
    "garage",
    "house",
    "store",
    "market",
    "express",
    "connect",
    "link",
    "now",
    "today",
    "live",
    "hq"
]

    @classmethod
    def generate(cls, word):

        results = set()

        for suffix in cls.SUFFIXES:
            results.add(word + suffix)

        return results