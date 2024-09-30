import os
import pytest
import sys
from pathlib import Path
from subprocess import run

WORKING_DIR = Path(__file__).parent.resolve()
CMAKE_BUILD_DIR = WORKING_DIR / "build"


class NonZeroExitCode(Exception):
    pass


def must_exec(cmd, env=None):
    if env is None:
        env = os.environ

    result = run(cmd, env=env)
    if result.returncode != 0:
        raise NonZeroExitCode


def run_python():
    return_code = pytest.main(["problems", "-xv"])
    if return_code != 0:
        raise NonZeroExitCode


def run_go():
    env = {"CGO_ENABLED": "0"} | os.environ
    cmd = ["go", "test", "./..."]
    must_exec(cmd, env)


def run_zig():
    cmd = ["zig", "build", "test"]
    must_exec(cmd)


def run_c():
    cmd = ["ctest"]
    os.chdir(CMAKE_BUILD_DIR)
    must_exec(cmd)


def find_mount():
    if "problems" not in os.listdir():
        print("Make sure the problems directory is mounted into container")
        sys.exit(1)


def build():
    run(["mkdir", "-p", "build"])
    os.chdir(CMAKE_BUILD_DIR)

    commands = [
        "cmake .. -G Ninja -USE_LOCAL_IGRAPH=ON".split(),
        ["ninja"],
    ]
    for cmd in commands:
        must_exec(cmd)

    os.chdir(WORKING_DIR)


if __name__ == "__main__":
    find_mount()
    build()

    test_suites = [
        run_python,
        run_go,
        run_zig,
        run_c,
    ]
    for suite in test_suites:
        suite()
