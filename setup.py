from setuptools import setup, find_packages

setup(
    name="github-user-activity",
    version="1.0.0",
    description="A simple command line interface (CLI) to fetch the recent "
    "activity of a GitHub user and display it in the terminal",
    packages=find_packages(),
    install_requires=None,
    author="Pedro",
    author_email="manuelflores1795@gmail.com",
    url="https://github.com/flobell/github-user-activity.git",
    py_modules=["main"],
    entry_points={
        'console_scripts': [
            'github-activity=main:main',
        ],
    },
    tests_require=[
        "unittest",
    ],
    python_requires=">=3.9",
)
