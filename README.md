# Terminal Typing Test

[![Python Version](https://img.shields.io/badge/Python-3.13.3-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](https://opensource.org/licenses/MIT)

**Terminal Typing Test** is a minimalist tool designed to measure typing speed directly in the terminal. Simply run the program, type the randomly generated text, and receive your typing speed and accuracy results.

---

## 📥 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/51B3/terminal_typing_test.git
   cd terminal_typing_test
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the program:
   ```bash
   python main.py
   ```

---

## 🎯 How It Works

1. The program selects a random text from a predefined list or an external file.
2. You start typing the displayed text in the terminal.
3. Upon completion, the program calculates:
   - Typing speed (characters per minute, words per minute).
   - Accuracy (percentage of correctly typed characters).
   - Total time taken.

---

## 🚀 Features

- 📝 Random text selection for typing tests.
- ⏱ Accurate speed and accuracy calculation.
- 🎨 Minimalist terminal-based interface.
- 🛠 Easy to extend and customize.

---

## 📂 Project Structure

```
terminal_typing_test/
├── keyboard.py        # Module containing predefined keyboard constants
├── main.py            # Main executable script
├── requirements.txt   # Dependencies file
└── words.json         # JSON file containing words for typing tests
```

---

## 🤝 Contributing

If you would like to contribute to this project, follow these steps:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m "Added new feature"
   ```
4. Push your changes to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Submit a Pull Request.

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

