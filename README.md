# dvoynik
Detect doppelganger websites by their appearance.

Dvoynik crawls and screenshots websites from a list of domains, then uses a
perceptive hash and a clustering algorithm to identify sites which look alike.
This can help you find phishing sites, doppelgangers of legitimate sites, etc.

## 0. Install the tool
```
pip install .
playwright install
```

## 1. (Optional) Find phishy domains
If you happen to have a DNS zone file (or otherwise large listing of registered domain),
you can start by finding domains that are similar to the legitimate sites you're interested in.

This takes punycode domains into account, so `exampłe.com` is identified as similar to the legitimate `example.com`.
```
dvoynik-similar-domains --all-domains long-list-of-domains.txt --target-domains list-of-legitimate-domains.txt --output fishy-domains.txt
```

## 2. Crawl and screenshot
```
dvoynik-crawl --domains fishy-domains.txt --workdir working-directory/
```


## 3. Group sites by similarity
Calculates hashes for all the screenshots and tries to cluster them together by similarity.

```
dvoynik-analyze --workdir working-directory/
```


## 4. Browse clusters of similar sites
The analysis step also places a little HTML viewer in the working directory,
so you can interactively browse the identified clusters.

```
cd working-directory
python3 -m http-server 8000
```

vist http://127.0.0.1:8000 and click and search!

