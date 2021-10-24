from typing import Sequence

from hooks.ext_subprocess import run_and_stream_output, run_and_get_output

PACKAGES = "{{ cookiecutter.install_packages }}".split(",")


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
