from urllib.parse import urlparse
import re
import os

import requests

def domains_from_zonefile(filename):
    ret = set()

    with open(filename, "r") as f:
        for line in f:
            line = line.strip()

            if len(line) == 0: continue
            if line[0] == ";": continue
            
            domain = line.split()[0]
            kind = line.split()[3]

            if kind in ["TXT", "RRSIG", "SOA", "DS"]: continue
            if ".ns." in domain: continue

            domain_without_root = domain[:-1]
            if "." not in domain_without_root: continue

            ret.add(domain_without_root)

    return list(sorted(ret))


def lines_from_textfile(filename):
    with open(filename, "r") as f:
        return [ l.strip() for l in f ]


def prefix_for_hostname(hostname):
    if hostname.startswith("www."):
        hostname = hostname[4:]

    parts = hostname.split(".")

    hostname = ".".join(parts[:-1])

    if len(hostname) < 2:
        return ""
    else:
        return hostname[0:2]

# Returns True if http://suspect_domain or https://suspect_domain
# redirect to the target_domain
def is_redirect_to(suspect_domain, target_domain):
    options = [
            f"http://{suspect_domain}",
            f"https://{suspect_domain}"
            ]

    for url in options:
        res = requests.get(url, allow_redirects=True)

        for redir in [ res ] + res.history:
            parsed = urlparse(redir.url)
            if parsed.hostname == target_domain:
                return True
            if parsed.hostname.endswith("." + target_domain):
                return True
    return False


def domain_from_filename(filename):
    base = os.path.basename(filename)
    return re.sub("\.http(s?)\.png$", "", base)

def filename_for_url(url):

    try:
        parsed = urlparse(url)
    except:
        # Not a valid URL, not much we can do with it
        return None

    prefix = prefix_for_hostname(parsed.hostname)

    filename = f"{prefix}/{parsed.hostname}.{parsed.scheme}.png"

    if filename[0] == "/": filename = filename[1:]

    return filename
