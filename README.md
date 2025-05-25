# dvoynik
Detect doppelganger websites by their appearance

## 0. Install the tool
```
pip install .
playwright install
```

## 1. (Optional) Find phishy domains
```
dvoynik-similar-domains --all-domains long-list-of-domains.txt --target-domains list-of-legitimate-domains.txt --output fishy-domains.txt
```

## 1. Crawl and screenshot
```
dvoynik-crawl --domains fishy-domains.txt --output results-directory/
```


## 2. Group sites by similarity
```
dvoynik-analyze --input results-directory/ --output report-directory/
```


## 3. Search the report
```
dvoynik-search --input report-directory/ --domains list-of-interesting-domains.txt
```
