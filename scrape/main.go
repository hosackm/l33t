package main

import (
	"context"
	"fmt"
	"log"
	"net/http"
	"os"
	"path/filepath"
	"strings"
	"time"

	md "github.com/JohannesKaufmann/html-to-markdown"
	"github.com/antchfx/htmlquery"
	"github.com/chromedp/chromedp"
)

const (
	GrindURL                 = "https://www.techinterviewhandbook.org/grind75"
	LeetcodeURL              = "https://leetcode.com/problems/"
	DescriptionClassSelector = ".elfjS"
	TitleClassSelector       = ".text-title-large a"
)

var (
	converter = md.NewConverter("leetcode.com", true, nil)
)

type Problem struct {
	Slug        string
	Title       string
	Description string
	Link        string
}

func (p *Problem) ToMarkdown() string {
	// convert <sup> to caret because the conversion to markdown loses
	// the representation and presents a different number altogether
	description := strings.ReplaceAll(p.Description, "<sup>", "^")
	description = strings.ReplaceAll(description, "</sup>", "")
	markdown, err := converter.ConvertString(description)
	if err != nil {
		log.Fatal(err)
	}

	return fmt.Sprintf("# [%s](%s)\n\n", p.Title, p.Link) + markdown
}

func GetProblems(ch chan Problem) error {
	client := http.Client{Timeout: time.Second * 10}
	req, err := http.NewRequest("GET", GrindURL, nil)
	if err != nil {
		return err
	}

	resp, err := client.Do(req)
	if err != nil {
		return err
	}
	if resp.StatusCode != http.StatusOK {
		return fmt.Errorf("returned status != 200")
	}

	root, err := htmlquery.Parse(resp.Body)
	if err != nil {
		return err
	}

	go func() {
		ctx, cancel := NewContext()
		defer cancel()

		i := 1
		for _, element := range htmlquery.Find(root, `//a[@href]`) {
			href := htmlquery.SelectAttr(element, "href")
			if !strings.HasPrefix(href, LeetcodeURL) {
				continue
			}

			link := strings.TrimRight(href, "/")
			log.Printf("[%d] scraping '%s'\n", i, link)

			var problem Problem
			problem.Slug = strings.TrimPrefix(link, LeetcodeURL)
			problem.Link = link

			actions := []chromedp.Action{
				chromedp.Navigate(link),
				chromedp.WaitReady(DescriptionClassSelector, chromedp.ByQuery),
				chromedp.Text(TitleClassSelector, &problem.Title),
				chromedp.InnerHTML(DescriptionClassSelector, &problem.Description),
			}
			if err = chromedp.Run(ctx, actions...); err != nil {
				panic(err)
			}

			ch <- problem
			i++
		}

		close(ch)
	}()

	return nil
}

// NewContext returns a multi purpose context with custom logging
// and timeout as a single context and cancel function.
func NewContext() (context.Context, context.CancelFunc) {
	cancels := []context.CancelFunc{}
	opts := append(chromedp.DefaultExecAllocatorOptions[:],
		chromedp.DisableGPU,
		chromedp.NoDefaultBrowserCheck,
		chromedp.NoFirstRun,
		chromedp.UserAgent("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3830.0 Safari/537.36"),
		chromedp.Flag("ignore-certificate-errors", true),
		chromedp.Flag("window-size", "50,400"),
	)

	// create context
	ctx, cancel := chromedp.NewExecAllocator(context.Background(), opts...)
	cancels = append(cancels, cancel)

	// also set up a custom logger
	ctx, cancel = chromedp.NewContext(ctx, chromedp.WithLogf(log.Printf))
	cancels = append(cancels, cancel)

	f := func() {
		for _, cancel := range cancels {
			cancel()
		}
	}

	return ctx, f
}

func main() {
	i := 1
	ch := make(chan Problem)

	err := GetProblems(ch)
	if err != nil {
		log.Fatal(err)
	}

	for p := range ch {
		folder := fmt.Sprintf("problems/%02d", i)
		err = os.MkdirAll(folder, 0o777)
		if err != nil {
			log.Fatal(err)
		}

		data := []byte(p.ToMarkdown())
		basename := fmt.Sprintf("%s.md", p.Slug)
		name := filepath.Join(folder, basename)

		log.Printf("[%d] writing '%s'\n", i, basename)
		if err = os.WriteFile(name, data, 0o777); err != nil {
			log.Fatal(err)
		}
		i++
	}
}
