# Scrape

A small utility for populating the `problems` folder with content from leetcode.

Performs the following steps:

1. Pull problem list from Grind 75 as a collection of `href`s
2. Use [chromedp](https://github.com/chromedp/chromedp) to collect the content of the problem
3. Create a directory with the problem number (`/problems/01-75`)
4. Convert the problem description to markdown
5. Write markdown inside newly created folder (from step 3)

> **NOTE:** leetcode contains asynchronous javascript code and has protections against scraping making the use of chromedp mandatory.

## To run it yourself
First install the dependencies:

```bash
go mod tidy
```

Then run the program:

```bash
go run scrape/main.go
```
