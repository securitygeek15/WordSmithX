# 🚀 WordSmithX

**WordSmithX** is a modular Python-based text variation generator designed for creating large-scale keyword, username, branding, naming, and testing datasets.

Built with a plugin-like architecture, WordSmithX combines multiple generators such as prefixes, suffixes, separators, number patterns, abbreviations, and formatting transformations to produce thousands of unique text variations from a single input.

---

## ✨ Features

* 🔤 Case transformations
* 🎯 Prefix generation
* 🏷️ Suffix generation
* 🔢 Number pattern generation
* 🔀 Separator combinations
* 🔄 Reverse text generation
* 📋 Abbreviation generation
* 🧩 Combination engine
* 🚫 Automatic duplicate removal
* 📁 Export results to text files
* ⚡ Fast and lightweight

---

## 📂 Project Structure

```text
WordSmithX/

├── main.py
├── engine.py
│
├── generators/
│   ├── case.py
│   ├── prefix.py
│   ├── suffix.py
│   ├── numbers.py
│   ├── separator.py
│   ├── reverse.py
│   ├── abbreviations.py
│   └── combos.py
│
└── output/
```

---

## 🛠 Installation

Clone the repository:

```bash
git clone https://github.com/securitygeek15/WordSmithX.git
```

Navigate into the project:

```bash
cd WordSmithX
```

Run:

```bash
python main.py
```

---

## 📖 Example

Input:

```text
amaan
```

Example Output:

```text
AMAAN
amaan
Amaan
realamaan
officialamaan
amaanhub
amaantech
amaanworld
xamaanlabs
amaan_01
amaan-99
realamaan.tech
proamaanhub
```

Thousands of unique variations can be generated depending on the enabled generators and rules.

---

## ⚙️ How It Works

Each generator is responsible for a specific type of transformation.

Examples:

### Prefix Generator

```python
real + amaan
official + amaan
pro + amaan
```

### Suffix Generator

```python
amaan + hub
amaan + tech
amaan + world
```

### Combination Generator

```python
real + amaan + tech
official + amaan + world
pro + amaan + hub
```

The Engine collects all generated variations and removes duplicates using Python sets.

---

## 📈 Current Generators

| Generator             | Purpose                    |
| --------------------- | -------------------------- |
| CaseGenerator         | Text formatting variations |
| PrefixGenerator       | Prefix combinations        |
| SuffixGenerator       | Suffix combinations        |
| NumberGenerator       | Numeric patterns           |
| SeparatorGenerator    | Separator insertion        |
| ReverseGenerator      | Reversed text variants     |
| AbbreviationGenerator | Acronym generation         |
| ComboGenerator        | Multi-rule combinations    |

---

## 🎯 Use Cases

* Username brainstorming
* Brand name generation
* Domain name ideation
* SEO keyword variations
* Test dataset generation
* Content creation workflows
* Development and automation experiments

---

## 🔮 Planned Features

* GUI Version
* Plugin System
* Configuration Files
* Custom Rule Builder
* CSV Export
* JSON Export
* Batch Processing
* Category-Based Generators
* Statistics Dashboard
* PyQt6 Desktop Application

---

## 🤝 Contributing

Pull requests, ideas, and feature suggestions are welcome.

If you'd like to improve WordSmithX, feel free to fork the repository and submit a PR.

---

## 👨‍💻 Author

**Amaan (Security Geek)**

Building projects, learning, and exploring Python one step at a time.
