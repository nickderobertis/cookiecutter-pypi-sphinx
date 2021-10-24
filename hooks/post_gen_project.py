from typing import Sequence
import shlex
import subprocess

PACKAGES = "{{ cookiecutter.install_packages }}".split(",")


def stream_process(process):
    go = process.poll() is None
    for line in process.stdout:
        print(line.decode("utf8"), end="")
    return go


def run_and_stream_output(command: str):
    process = subprocess.Popen(
        command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
    )
    while stream_process(process):
        pass


def run_and_get_output(command: str) -> str:
    output = subprocess.run(
        shlex.split(command),
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    return output.stdout.decode("utf8")


def is_existing_pipenv_project() -> bool:
    pipenv_py_output = run_and_get_output("pipenv --py")
    return not ("No virtualenv" in pipenv_py_output)


def pipenv_install(packages: Sequence[str]):
    package_str = " ".join(packages)
    command = f"pipenv install {package_str}"
    run_and_stream_output(command)


def main():
    if is_existing_pipenv_project():
        print("Project already exists, skipping pipenv install")
        return
    pipenv_install(PACKAGES)


if __name__ == "__main__":
    main()
