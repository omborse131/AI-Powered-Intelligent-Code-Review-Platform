import subprocess
import tempfile
import json
import os


def run_bandit(code: str):
    """
    Run Bandit security analysis on Python code.
    """

    temp_file = None

    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            suffix=".py",
            delete=False,
            encoding="utf-8"
        ) as file:

            file.write(code)
            temp_file = file.name

        result = subprocess.run(
            [
                "bandit",
                "-f",
                "json",
                "-q",
                temp_file
            ],
            capture_output=True,
            text=True
        )

        if not result.stdout:
            return []

        data = json.loads(result.stdout)

        issues = []

        for item in data.get("results", []):

            issues.append({
                "tool": "bandit",
                "test_id": item.get("test_id"),
                "severity": item.get("issue_severity"),
                "confidence": item.get("issue_confidence"),
                "message": item.get("issue_text"),
                "line": item.get("line_number"),
                "code": item.get("code")
            })

        return issues

    except Exception as e:
        return [
            {
                "tool": "bandit",
                "severity": "ERROR",
                "message": str(e)
            }
        ]

    finally:
        if temp_file and os.path.exists(temp_file):
            os.remove(temp_file)


def run_ruff(code: str):
    """
    Run Ruff code-quality analysis on Python code.
    """

    temp_file = None

    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            suffix=".py",
            delete=False,
            encoding="utf-8"
        ) as file:

            file.write(code)
            temp_file = file.name

        result = subprocess.run(
            [
                "ruff",
                "check",
                "--output-format",
                "json",
                temp_file
            ],
            capture_output=True,
            text=True
        )

        if not result.stdout:
            return []

        data = json.loads(result.stdout)

        issues = []

        for item in data:

            issues.append({
                "tool": "ruff",
                "code": item.get("code"),
                "message": item.get("message"),
                "line": item.get("location", {}).get("row"),
                "column": item.get("location", {}).get("column"),
                "end_line": item.get("end_location", {}).get("row"),
                "end_column": item.get("end_location", {}).get("column")
            })

        return issues

    except Exception as e:
        return [
            {
                "tool": "ruff",
                "severity": "ERROR",
                "message": str(e)
            }
        ]

    finally:
        if temp_file and os.path.exists(temp_file):
            os.remove(temp_file)


def analyze_python_code(code: str):

    bandit_issues = run_bandit(code) or []
    ruff_issues = run_ruff(code) or []

    return {
        "language": "python",
        "issues": bandit_issues + ruff_issues,
        "total_issues": len(bandit_issues) + len(ruff_issues)
    }