from engine import Engine

from generators.case import CaseGenerator
from generators.prefix import PrefixGenerator
from generators.suffix import SuffixGenerator
from generators.numbers import NumberGenerator
from generators.separator import SeparatorGenerator
from generators.reverse import ReverseGenerator
from generators.combos import ComboGenerator

engine = Engine()

word = input("Enter text: ")

engine.add(CaseGenerator.generate(word))
engine.add(PrefixGenerator.generate(word))
engine.add(SuffixGenerator.generate(word))
engine.add(NumberGenerator.generate(word))
engine.add(SeparatorGenerator.generate(word))
engine.add(ReverseGenerator.generate(word))
engine.add(ComboGenerator.generate(word))



filename = input("Enter What should be the Filename (without .txt) : ")
with open(
    f"output/{filename}.txt",
    "w",
    encoding="utf-8"
) as file:

    for item in engine.export():
        file.write(item + "\n")


print(f"Generated: {len(engine.results)}")