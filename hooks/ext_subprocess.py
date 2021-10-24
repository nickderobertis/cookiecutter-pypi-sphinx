import shlex
import subprocess


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
