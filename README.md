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

## 2. Crawl and screenshot
```
dvoynik-crawl --domains fishy-domains.txt --workdir working-directory/
```


## 3. Group sites by similarity
```
dvoynik-analyze --workdir working-directory/
```


## 4. Browse clusters of similar sites
```
cd working-directory
python3 -m http-server 8000
```

vist http://127.0.0.1:8000 and click and search!

