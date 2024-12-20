# l33t

![Build Status](https://github.com/hosackm/l33t/actions/workflows/test.yml/badge.svg) ![Activity](https://img.shields.io/github/commit-activity/m/hosackm/l33t.svg)

A monorepo for me to store my leetcode solutions and work.

## Scope

I'm working off a subset of problems from [leetcode](leetcode.com) as chosen by the author of [Grind 75](https://www.techinterviewhandbook.org/grind75).

My solutions will be done mostly in Python as that's the language I'd most likely choose to interview in. However, I'll occasionally solve problems in other languages when it suits the problem or if I'm curious to see how the solution would differ (ie. Go, Zig, C, etc.).

## Running tests

Each problem solution contains its own test suite which can be run in several ways depending on the implementation language.

### Running tests with Docker

The easiest way to run the tests is by using docker. A Dockerfile is provided to create a container in which the tests can be built and run. It can be built with the following:

```bash
docker build . -t l33t
```

The problems folder must be mounted into the container in order to run the tests. This way the files can be added or modified and updates will be present when running the tests.

Run the container like so:

```bash
docker run -it -v ./problems:/root/problems l33t
```

### Python

Make sure you have the Python dependencies installed:

```bash
python -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

A Python solution can be run directly with the following:

```bash
python problems/01/two_sum.py
```

**OR**

all available tests can be run using `pytest` from the root directory, like so:

```bash
pytest -xv
```

### Go

Go solutions can be run directly, using:

```bash
go test problems/01/*.go
```

Or all solutions in one go:

```bash
CGO_ENABLED=0 go test ./...
```

> **Note:** `CGO_ENABLED=0` must be present when there are Go solutions in the same folder as C solutions.

### C

Some solutions are provided in C. In order to run the test suites you'll need to ensure some dependencies are installed on your machine.

#### Dependencies

[CMake](https://cmake.org) is used as the meta-build (and test) system for C solutions. You'll need it and [criterion](https://github.com/Snaipe/Criterion) installed if you wish to build the C solutions. You can use your package manager of choice to do so.

For example, with [homebrew](https://brew.sh/), run:

```bash
brew install cmake criterion
```

#### Other dependencies

In cases where data structures are needed, I've chosen to use some well-known libraries. These libraries are fetched as a part of the `cmake` process when generating your build files so you don't have to do anything yourself. They are:

 * [stb_ds](https://github.com/nothings/stb)
 * [igraph](https://github.com/igraph/igraph)


#### Running C tests

You'll need to `make` the CMake project and then run `ctest`.

```bash
mkdir build
cd build
cmake ..

# or if you prefer ninja
cmake .. -G Ninja
```

You'll now have build files available and can build the project and run the test suite using the following:

```bash
make
ctest

# or with ninja
ninja
ctest
```

You should see something along the lines of the following:

```bash
Test project /Users/hosack/code/leet/build
    Start 1: 01_two_sum
1/4 Test #1: 01_two_sum .......................   Passed    0.24 sec
    Start 2: 02_valid_parentheses
2/4 Test #2: 02_valid_parentheses .............   Passed    0.16 sec
    Start 3: 03_merge_sorted_lists
3/4 Test #3: 03_merge_sorted_lists ............   Passed    0.18 sec
    Start 4: 07_valid_anagram
4/4 Test #4: 07_valid_anagram .................   Passed    0.15 sec

100% tests passed, 0 tests failed out of 4

Total Test time (real) =   0.72 sec
```

### Running zig tests

All tests are imported into `tests.zig` which is built and run with the following:

```bash
zig build test
```

If you'd like to execute a solution's tests directly you can run:

```bash
zig test problems/01/two_sum.zig
```
### Running elixir tests

Like zig tests, all [elixir]() tests from the problems subdirectories have been included in `tests.exs`. You can run them with:

```bash
$ elixir tests.exs

Running ExUnit with seed: 746382, max_cases: 22

.
Finished in 0.03 seconds (0.03s on load, 0.00s async, 0.00s sync)
1 test, 0 failures
```
