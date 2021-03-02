# Scrapy demo

An example of how to use `scrapy` to scrape jokes from the website <http://www.laughfactory.com/jokes/science-jokes>. First, load up Git Bash and initialise the default `conda` environment with

```bash
conda activate
```

Navigate to the `scrapy` project directory, e.g., `scrapy_demos/joke_site_demo/`. You can then run the crawler with

```bash
scrapy crawl <name attribute of spider in class definition (in spiders/ subdirectory)> -O <output file>
```

e.g.,

```bash
scrapy crawl jokes -O data.csv
```

For the output file argument, use `-O` if you want the output file to overwrite an existing file. Instead use `-o` to append the new content to an existing file.
