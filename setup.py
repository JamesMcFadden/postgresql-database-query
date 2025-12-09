# setup.py
from setuptools import setup, find_packages
from pathlib import Path

BASE_DIR = Path(__file__).parent
README = (BASE_DIR / "README.md").read_text(encoding="utf-8") if (BASE_DIR / "README.md").exists() else ""

setup(
    name="launchlog",
    version="0.1.0",
    description="Space launch log demo app with PostgreSQL backend",
    long_description=README,
    long_description_content_type="text/markdown",
    author="James McFadden",
    packages=find_packages(exclude=("tests", "tests.*")),
    python_requires=">=3.13",
    install_requires=[
        "psycopg[binary]>=3.1.0",
        "python-dotenv>=1.0.0",
    ],
    entry_points={
        "console_scripts": [
            # lets you run `launchlog-cli ...` from the shell
            "launchlog-cli=launchlog.cli:main",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)
