import os
import pytest
import sys
from contextlib import contextmanager
from pathlib import Path
from subprocess import run, PIPE

REPO_ROOT = Path(__file__).parent.resolve()
CMAKE_BUILD_DIR = REPO_ROOT / "build"


class NonZeroExitCode(Exception):
    pass


@contextmanager
def working_dir(dir):
    cwd = os.getcwd()
    try:
        os.chdir(dir)
        yield
    finally:
        os.chdir(cwd)


def must_exec(cmd, env=None):
    if env is None:
        env = os.environ

    result = run(cmd, env=env, stdout=PIPE, stderr=PIPE)
    print(result.stdout.decode())
    print(result.stderr.decode())

    if result.returncode != 0:
        raise NonZeroExitCode

    return result


def run_python():
    print("Running python tests...")
    return_code = pytest.main(["problems", "-xv"])
    if return_code != 0:
        raise NonZeroExitCode


def run_go():
    print("Running go tests...")
    env = {"CGO_ENABLED": "0"} | os.environ
    cmd = ["go", "test", "./..."]
    must_exec(cmd, env)


def run_zig():
    print("Running zig tests...")
    cmd = ["zig", "test", "tests.zig"]
    must_exec(cmd)


def run_c():
    print("Running C tests...")
    cmd = ["ctest"]
    os.chdir(CMAKE_BUILD_DIR)
    must_exec(cmd)


def build():
    run(["mkdir", "-p", "build"])
    with working_dir(CMAKE_BUILD_DIR):
        commands = [
            "cmake .. -G Ninja -USE_LOCAL_IGRAPH=ON",
            "ninja",
        ]
        for cmd in commands:
            must_exec(cmd.split())


if __name__ == "__main__":
    if "problems" not in os.listdir():
        print("Make sure the problems directory is mounted into container")
        sys.exit(1)

    build()

    test_suites = [
        run_python,
        run_go,
        run_zig,
        run_c,
    ]
    for suite in test_suites:
        suite()
