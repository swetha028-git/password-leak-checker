# Password Leak Checker (HIBP k-anonymity)

Small CLI tool to check whether a password has appeared in known breaches using Have I Been Pwned's Pwned Passwords k-anonymity API.

## Usage

1. Create virtual environment and install:
```bash
python -m venv venv
# mac/linux
source venv/bin/activate
# windows (PowerShell)
venv\Scripts\Activate.ps1
pip install -r requirements.txt
