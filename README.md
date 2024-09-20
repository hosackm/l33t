# l33t

A place for me to store my leetcode solutions and work.

## Scope

I'm working off a subset of problems from [leetcode](leetcode.com) as chosen by the author of [Grind 75](https://www.techinterviewhandbook.org/grind75).

My solutions will be done mostly in Python as that's the language I'd most likely choose to interview in. However, I'll occasionally solve problems in other languages when it suits the problem or if I'm curious to see how the solution would differ (ie. Go, Zig, C).

## Running tests

Each problem solution contains its own test suite which can be run in several ways depending on the implementation language.

### Python

When a solution is a available in Python it can be run with the following:

```bash
python problems/01/two_sum.py
```

Also, all available tests can be run using `pytest` from the root directory, like so:

```bash
pytest -xv
```

### Go

Go solutions can be run directly:

```bash
go test problems/01/*.go
```

Or all solutions in one go:

```bash
CGO_ENABLED=0 go test ./...
```

> **Note:** `CGO_ENABLED=0` must be present when there are Go solutions in the same folder as C solutions.

### C

Some solutions are provided in C. In order to run the test suites you'll need to ensure some dependencies are available on your machine.

#### Dependencies

[CMake](https://cmake.org) is used as the build (and test) system for C solutions. You'll need it and [glib](https://github.com/GNOME/glib) installed if you wish to build the C solutions. You can use your package manager of choice to do so.

With [homebrew](https://brew.sh/) installed, run:

```bash
brew install cmake glib
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

# or if you use ninja
cmake .. -G Ninja
```

You'll now have build files available and can build the project and run the test suite using the following:

```bash
make  # or ninja
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

### Zig

> **TODO**
