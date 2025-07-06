# 🚀 Deploy Celery Worker on Windows using NSSM and GitHub Actions

This guide explains how to deploy a **Celery** worker as a **Windows Service** using **NSSM**, and how to trigger it via **GitHub Actions**.

---

## 📦 Prerequisites

- A Windows machine (preferably Server edition)
- Administrator access
- GitHub repository with a functioning Python/Celery project
- Internet access to download dependencies

---

## 🧰 Tools Required

| Tool             | Purpose                         | Download Link / Install Command                                       |
|------------------|----------------------------------|------------------------------------------------------------------------|
| Python           | Runtime for Celery              | [Download Python](https://www.python.org/downloads/)                  |
| NSSM             | Manage non-service apps         | [Download NSSM](https://nssm.cc/download)                             |
| PowerShell (v7+) | Scripting and service setup     | `winget install --id Microsoft.PowerShell --source winget`           |
| GitHub Runner    | GitHub Actions self-hosted runner | [GitHub Runner Setup](https://github.com/actions/runner)             |

---

## 🪜 Step-by-Step Instructions

### 1️⃣ Install Python

1. Download and install Python from [python.org](https://www.python.org/downloads/).
2. During installation:
   - ✅ Check **Add Python to PATH**
   - ✅ Enable `pip`


### 2️⃣ Install NSSM

1. Download NSSM from the official site: [https://nssm.cc/download](https://nssm.cc/download)
2. Extract and place the `nssm.exe` (usually found under `win64`) somewhere in your system PATH (e.g., `C:\Tools\nssm\nssm.exe`).
3. Verify installation:

```
nssm --version
```

### 3️⃣ Install PowerShell 7+ (if not already)
To install PowerShell using winget:

```
winget search Microsoft.PowerShell
winget install --id Microsoft.PowerShell --source winget
```

### 4️⃣ Install GitHub Runner
Navigate to your GitHub repo: Settings > Actions > Runners

Click "New self-hosted runner" and follow the instructions.


