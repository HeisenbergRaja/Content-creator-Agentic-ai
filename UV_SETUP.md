# Setup Guide - Using UV Package Manager

This project uses **uv** - a fast, modern Python package manager written in Rust.

## Why UV?

- **⚡ Fast**: 5-10x faster than pip
- **🔒 Reliable**: Deterministic dependency resolution
- **📦 Minimal**: Single binary, no external dependencies
- **🐍 Compatible**: Drop-in replacement for pip/venv

## Installation

### Step 1: Install UV

#### Option A: Using pip (if Python is already installed)
```bash
pip install uv
```

#### Option B: Download standalone binary
Visit: https://github.com/astral-sh/uv/releases

### Step 2: Create Virtual Environment with UV

```bash
cd c:\Users\Heisenberg Raja\OneDrive\Desktop\agentic

# Create venv
uv venv

# Activate venv
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

### Step 3: Install Dependencies with UV

```bash
# Using requirements.txt
uv pip install -r requirements.txt

# Or using pyproject.toml (recommended)
uv pip install -e .

# Install with dev dependencies
uv pip install -e ".[dev]"
```

## Common UV Commands

### Install Dependencies
```bash
uv pip install <package>
uv pip install -r requirements.txt
```

### Update Packages
```bash
uv pip install --upgrade <package>
uv pip install --upgrade -r requirements.txt
```

### Uninstall Packages
```bash
uv pip uninstall <package>
```

### List Installed Packages
```bash
uv pip list
```

### Freeze Requirements
```bash
uv pip freeze > requirements.txt
```

### Sync Exact Dependencies
```bash
uv pip sync requirements.txt
```

## Quick Start

### 1. Setup Environment
```bash
# Navigate to project
cd c:\Users\Heisenberg Raja\OneDrive\Desktop\agentic

# Create and activate venv
uv venv
.venv\Scripts\activate

# Install dependencies
uv pip install -r requirements.txt
```

### 2. Configure Environment Variables
```bash
# Create .env file with your OpenAI API key
copy .env.example .env

# Edit .env and add your key:
# OPENAI_API_KEY=sk-...
```

### 3. Run the Application
```bash
python main.py
```

## Troubleshooting

### "uv: command not found"
Solution: Ensure uv is in your PATH or use `python -m uv`

### Activate venv manually
```bash
# Windows PowerShell
.\.venv\Scripts\Activate.ps1

# Windows CMD
.venv\Scripts\activate.bat

# macOS/Linux
source .venv/bin/activate
```

### Clear UV cache
```bash
uv cache clean
```

### Reinstall all dependencies
```bash
uv pip uninstall -r requirements.txt
uv pip install -r requirements.txt
```

## Project Structure with UV

```
agentic/
├── .venv/                    # Virtual environment (created by uv)
├── pyproject.toml           # Project config (uv compatible)
├── requirements.txt         # Pinned dependencies
├── .env.example            # Environment template
├── main.py                 # Main application
├── README.md               # Project documentation
└── article_output.txt      # Generated output
```

## CI/CD with UV

For GitHub Actions or other CI systems:

```yaml
- name: Install dependencies with UV
  run: |
    python -m pip install uv
    uv pip install -r requirements.txt
```

## Documentation

- UV Official Docs: https://docs.astral.sh/uv/
- GitHub: https://github.com/astral-sh/uv

---

**Version**: 1.0.0 | **Last Updated**: November 2025
