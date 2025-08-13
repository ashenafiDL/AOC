# Advent of Code (AOC) Solutions

This repository contains my solutions for **[Advent of Code](https://adventofcode.com/)** challenges.
Each year’s challenges are stored in their own folder, with a separate folder for each day.

## 📂 Project Structure

```
AOC/
│
├── 2024/
│ ├── day-01/
| | |-- day-01-input.txt
│ │ └── day-01.py
│ ├── day-02/
| | |-- day-02-input.txt
│ │ └── day-02.py
│ └── ...
│
├── file/
│ └── utils.py # Shared helper functions (e.g., read_file_lines)
│
└── README.md
```

- `file/utils.py` — Contains utility functions like `read_file_lines` to read input files.
- Each `day-XX` folder contains one Python file for that day’s solution and one text file for that day's puzzle input.

## 🔧 Installation

1. **Clone the repository**

```bash
git clone https://github.com/ashenafidl/AOC.git
cd AOC
```

2. Set up a virtual environment (optional but recommended)

```base
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Running a Solution

From the repository root, run:

```
python -m 2024.day-10.day-10
```

## 🏆 About Advent of Code

Advent of Code is an annual set of programming puzzles released daily from December 1st to 25th.
It’s a fun way to improve problem-solving and coding skills.

## 📜 License

MIT License — free to use, modify, and share.
