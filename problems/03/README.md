# l33t

A place for me to store my leetcode solutions and work.

## Scope

I'm working off a subset of problems from [leetcode](leetcode.com) as chosen by the author of [Grind 75](https://www.techinterviewhandbook.org/grind75).

My solutions will be done mostly in Python as that's the language I'd most likely choose to interview in. However, I'll occasionally solve problems in other languages when it suits the problem or if I'm curious to see how the solution would differ (ie. Go, Zig, C).

## Scrape

I've written a small Go program in the `scrape` folder. It performs the following steps:

1. Pull problem list from Grind 75 as a collection of `href`s
2. Use [chromedp](https://github.com/chromedp/chromedp) to collect the content of the problem
3. Create a directory with the problem number (`/problems/01-75`)
4. Convert the problem description to markdown
5. Write markdown inside newly created folder (from step 3)

> **NOTE:** leetcode contains asynchronous javascript code and has protections against scraping making the use of chromedp mandatory.

### To run it yourself
First install the dependencies:

```bash
go mod tidy
```

Then run the program:

```bash
go run scrape/main.go
```
