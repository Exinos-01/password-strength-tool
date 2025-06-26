
#  Password Strength Analyzer with Custom Wordlist Generator

This is a simple Python-based cybersecurity tool built as part of an internship project. It includes:

- A **password strength analyzer** using `zxcvbn`, which evaluates passwords and provides feedback.
- A **custom wordlist generator** that creates realistic password variations based on user input (e.g., name, pet name, birth year, etc.).

## Features

###  Password Analyzer
- Uses `zxcvbn` to score password strength (0–4)
- Provides suggestions and warnings
- Saves analysis to `password_log.txt`

###  Wordlist Generator
- Takes personal inputs like name, pet name, year, etc.
- Generates combinations with leetspeak, appended numbers, and patterns
- Outputs to `custom_wordlist.txt`

###  Command-line Interface
Run everything using `argparse` from terminal:
```bash
# Analyze password strength
python main.py --analyze --password YourPassword123

# Generate wordlist
python main.py --wordlist --name Sharan --pet Max --year 2001 --fav Hacker
```

## 🛠 Tools Used

- Python 3
- zxcvbn
- argparse
- itertools

##  Folder Structure

```
password-strength-tool/
├── main.py
├── password_log.txt
├── custom_wordlist.txt
├── project_report.pdf
└── screenshots/ (optional)
```

##  Author

**Sharan Sreelal**  
Internship Project – June 2025
