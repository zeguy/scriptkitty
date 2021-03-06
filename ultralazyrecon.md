***Enumerate subdomains and check for webservers with assetfinder & httprobe x @tomnonomnom***

*tee enables us to see the output in the terminal as it's written to a file, then we run a for loop on our .txt files and remove duplicate lines with sort -u*:

```bash
assetfinder --subs-only example.com | tee subs.txt; cat subs.txt | httprobe | tee http.txt; for f in *.txt; do sort -u "$f" -o "$f"; done
```
*further comb results with @tomnomnom's meg to search for robots.txt, for example, saving only 200 responses and looking for potentially interesting paths*

```bash
assetfinder --subs-only example.com | tee subs; cat subs | httprobe | tee hosts; for f in *; do sort -u "$f" -o "$f"; meg -s 200 /robots.txt; grep -ri 'disallow' out/ | tee nobots; done
```
---

***Search CNAME records across multiple domains listed in file and output relevant results only***

```bash
xargs -n1 -a FILENAME dig CNAME | grep CNAME
```

---

***Leveraging Shodan API to find hosts running specific service version***

>
```python
import shodan

#Enter your own API key
SHODAN_API_KEY = "xxx"

api = shodan.Shodan(SHODAN_API_KEY)

def customSearch():
    versions = ["0.8.12", "0.8.13" ,"0.8.14"]
    vulnHosts = {}
    count = 0
    for version in versions:
    # Wrap the request in a try/ except block to catch errors
        try:
                # Search Shodan
                results = api.search('nginx '+"version:"+version)
                # Show the results
                for result in results['matches']:
                        print 'IP: %s' % result['ip_str']
                        print result['product'] + " " + result['version']
                        print ''
                        vulnHosts[result['ip_str']] = result['data']
                        count+=1
        except shodan.APIError, e:
                print 'Error: %s' % e
    print str(count) + " potential vulnerable hosts found"

customSearch()
```

