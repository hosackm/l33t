import os
import pytest
from pathlib import Path
from subprocess import run

WORKING_DIR = Path(__file__).parent.resolve()
CMAKE_BUILD_DIR = WORKING_DIR / "build"


class NonZeroExitCode(Exception):
    pass


def must_exec(cmd, env=None):
    if env is None:
        env = {}

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
    result = run(cmd, env=env)
    if result.returncode != 0:
        raise NonZeroExitCode


def run_zig():
    cmd = ["zig", "build", "test"]
    result = run(cmd)
    if result.returncode != 0:
        raise NonZeroExitCode


def run_c():
    cmd = ["ctest"]
    os.chdir(CMAKE_BUILD_DIR)
    result = run(cmd)
    if result.returncode != 0:
        raise NonZeroExitCode


if __name__ == "__main__":
    test_suites = [
        run_python,
        run_go,
        run_zig,
        run_c,
    ]
    for suite in test_suites:
        suite()
