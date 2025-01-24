# Github User Activty
A simple command line interface (CLI) to fetch the recent activity of a GitHub user and display it in the terminal

---

## Installation End-User Usage

### 1. Easy install with Pip
```bash
pip install git+https://github.com/flobell/github-user-activity.git
```

## Installation Dev

### 1. Clone the Repository
```bash
git clone https://github.com/flobell/github-user-activity.git
cd task-tracker
```

### 2. Create virtual environment
```bash
python -m venv venv
```

### 3. Activate virtual environment

- On Windows
```bash
.\venv\scripts\activate
```
- On macOS/Linux
```bash
source venv/bin/activate
```

### 4. Install project package

```bash
pip install -e .
```

## Unit Testing

### Execute unit tests

```
python -m unittest discover -s tests
```

## How to Use

### Fetch recent 10 most recent events
```bash
github-activity <username>
```

## Project URL
- https://roadmap.sh/projects/github-user-activity