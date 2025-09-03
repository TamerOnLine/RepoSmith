# 🛠️ RepoSmith

RepoSmith is a portable Python tool that helps you **bootstrap a new project quickly** with:
- Virtual environment (`venv`)
- Essential starter files (`app.py`, `requirements.txt`)
- VS Code configuration
- `.gitignore` presets
- `LICENSE` file
- GitHub Actions CI workflow

---

## ✨ Features

- ⚡ Instant project setup with one command.  
- 🐍 Python ≥ 3.12 support.  
- 📦 Automatic virtual environment creation and management.  
- 📝 Generates essential configuration files:  
  - `setup-config.json`  
  - `requirements.txt`  
  - `app.py` (with a welcome message)  
- 🛡️ Open-source license support (MIT by default).  
- 🤖 Preconfigured GitHub Actions workflow for running `main.py`.  
- 🧹 Ready-to-use `.gitignore` presets (Python, Node, Django).  

---

## 🚀 Installation & Usage

### 1️⃣ Clone the repository
```bash
git clone https://github.com/TamerOnLine/RepoSmith.git
cd RepoSmith
```

### 2️⃣ Run the setup
```bash
python main.py
```

By default, it will generate:
- Virtual environment in `.venv/`
- `requirements.txt`
- `app.py`
- `.vscode/` folder with settings

---

## ⚙️ CLI Options

You can customize the setup using command-line arguments:

```bash
python main.py --ci create --gitignore django --license MIT --author "Your Name"
```

### Supported options:
- `--ci [skip|create|force]` → Configure CI or skip it.  
- `--ci-python` → Python version for GitHub Actions (default: 3.12).  
- `--gitignore [python|node|django]` → Choose `.gitignore` preset.  
- `--license` → License type (MIT | Apache-2.0).  
- `--author` → Author name for LICENSE file.  
- `--year` → Year for LICENSE header (default: current year).  

---

## 📂 Generated Project Structure

After running the setup, your project will look like this:

```
my_project/
├── .venv/
├── .vscode/
│   ├── settings.json
│   ├── launch.json
├── app.py
├── main.py
├── requirements.txt
├── setup-config.json
├── .gitignore
└── LICENSE
```

---

## 🧪 GitHub Actions

A workflow is automatically generated under:

```
.github/workflows/test-main.yml
```

It runs `main.py` on every `push` and `pull_request`.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).
