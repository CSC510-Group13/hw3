[![Language: Python](https://img.shields.io/badge/Language-Python-blue.svg)](https://www.python.org/)
[![License: Apache-2-License](https://img.shields.io/badge/Licence-Apache--2--Licence-green.svg)](https://www.apache.org/licenses/LICENSE-2.0)
[![Platform: Linux](https://img.shields.io/badge/Platform-Linux-yellow.svg)](https://www.linux.org/)
[![Merge Sort Test](https://github.com/CSC510-Group13/hw3/actions/workflows/test.yml/badge.svg)](https://github.com/CSC510-Group13/hw3/actions/workflows/test.yml)


https://github.com/CSC510-Group13/hw3
[![Coverage Status](https://coveralls.io/repos/github.com/CSC510-Group13/hw3/badge.svg?branch=main)](https://coveralls.io/github/CSC510-Group13/hw3/?branch=main)
[![pylint](https://img.shields.io/badge/PyLint-10.00-brightgreen?logo=python&logoColor=white)](https://SC510-Group13/hw3/actions/runs/)

# Homework 3 - Debugging

## Project Overview
This project focuses on debugging a faulty `mergeSort` implementation in `hw2_debugging.py` and ensuring the code quality through automated tools. 
The following are the tasks that were performed:
- We did Pylint Analysis to check for programming errors, enforce a coding standard, finds code smells, which are indications of deeper problems in a system.
- Fixed issues based on the analysis tools' recommendations.
- Fix the bug in the mergeSort Implementation.  
- Writing test cases for `mergeSort` to verify its correctness.
- Configuring continuous integration (CI) to automatically run the analysis tools and test cases on every commit.


## Getting Started

### Prerequisites

- Python 3.13
- `pytest` for running the test cases

#

### Execute Three (3) Static Analysis Tools
- Use the following tools to analyze the code:
  1. **Pylint**: A static analysis tool to identify errors, style issues, and other potential problems in Python code.
  2. **pyflakes**: A simple program which checks Python source files for errors.
  3. **bandit**: A tool which checks Python files for security concerns.

  
To run these tools, use the following commands:
```bash
pylint hw2_debugging.py rand.py
pyflakes hw2_debugging.py rand.py
bandit hw2_debugging.py rand.py
```
### License
This project is licensed under the Apache License 2.0 See the LICENSE file for more details.
