import subprocess
from typing import Sequence

PACKAGES = "{{ cookiecutter.install_packages }}".split(",")


def stream_process(process):
    go = process.poll() is None
    for line in process.stdout:
        print(line.decode("utf8"), end="")
    return go


def run(command: str):
    process = subprocess.Popen(
        command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
    )
    while stream_process(process):
        pass


def pipenv_install(packages: Sequence[str]):
    package_str = " ".join(packages)
    command = f"pipenv install {package_str}"
    run(command)


pipenv_install(PACKAGES)
