# 2024

## 📂 Project Structure

```
2024/
 ├── day-01/
 | |-- day-01-input.txt
 │ └── day-01.py
 ├── day-02/
 | |-- day-02-input.txt
 │ └── day-02.py
 └── ...
 ├── utils/
 │ └── file.py # Shared helper functions (e.g., read_file_lines)
 └── README.md
```

- `utils/file.py` — Contains utility functions like `read_file_lines` to read input files.
- Each `day-XX` folder contains one Python file for that day’s solution and one text file for that day's puzzle input.

## 🔧 Installation

1. **Clone the repository**

```bash
git clone https://github.com/ashenafidl/AOC.git
cd AOC/2024
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
python -m day-10.day-10
```