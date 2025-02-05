# Installation Guide

## Prerequisites

- Python 3.13
- `pip` package manager

## Installation Steps

1. **Clone the repository**:
    ```bash
    git clone https://github.com/CSC510-Group13/hw3.git
    cd hw3
    ```

2. **Create a virtual environment** (optional but recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    python3 -m pip install --upgrade pip
    python3 -m pip install -r requirements.txt
    ```

4. **Run tests**:
    ```bash
    pytest
    ```

## Running Static Analysis Tools

To run the static analysis tools, use the following commands:
```bash
pylint hw2_debugging.py rand.py
pyflakes hw2_debugging.py rand.py
```