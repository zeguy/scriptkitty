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
