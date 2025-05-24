# dvoynik
Detect doppelganger websites by their appearance

## 0. Install the tool
```
pip install .
```

## 1. Crawl and screenshot
```
dvoynik-crawl --domains list-of-domains.txt --output results-directory/
```


## 2. Find similar sites
```
dvoynik-analyze --input results-directory/ --output report-directory/
```


