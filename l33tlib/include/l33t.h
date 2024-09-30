#pragma once

/**
 * @file l33t.h
 * @brief Contains API functions for frequently used leetcode types.
 * @author Matt Hosack
 * @version 1.0
 * @date September 2024
 *
 * @mainpage Documentation for l33tlib
 *
 * @section intro_sec Introduction
 *
 * TODO: This is the main page of the documentation for the project. It provides
 * an overview of the API and the project goals.
 *
 * @section install_sec Installation
 *
 * TODO: Installation instructions for the project.
 *
 * @section usage_sec Usage
 *
 * TODO: Example usage and key components of the API:
 *
 * @code
 * int result = my_function(42);
 * @endcode
 */

#include "error.h"
#include "list.h"
#include "stack.h"
#include "tree.h"

#define MAX(a, b) ((a > b) ? a : b)
#define ARRAY_SIZE(arr, t) (sizeof(arr) / sizeof(t))
