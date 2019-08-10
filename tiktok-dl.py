
DEBUG = True
VERBOSE = False
 
import sys
VERSION = sys.version_info[0]

def dowload_data(uri):
    UA_CHROME = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
    r1 = None
    class Junk:
        def __init__(self):
            self.data = None

    if VERSION==2:
        import urllib2
        req = urllib2.Request(uri, headers={ 'User-Agent': UA_CHROME })
        # faked to return a similar setup as Python3
        r1 = Junk()
        print("getting url data...")
        r1.data = urllib2.urlopen(req).read()
        return r1
    else:
        http = urllib3.PoolManager(10, headers=user_agent)
        print("getting url data...")
        r1 = http.urlopen('GET', uri)
        return r1

def mainline():
    import argparse
    
    parser = argparse.ArgumentParser()
    parser.add_argument("uri", help="uri to load")
    parser.add_argument("-v", "--verbose", help="verbose",action="store_true")
    parser.add_argument("-d", "--debug", help="debug this program",action="store_true")
    parser.add_argument("-o", "--output", help="output filename", default="out.mp4")

    args = parser.parse_args()
    
    # print(args)
    # import sys
    # sys.exit(0)

    if VERSION==2:
        pass
    else:
        import urllib3

    # this is chrome76
    UA_CHROME = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
    user_agent = {'user-agent': UA_CHROME }
    if VERSION==2:
        import urllib2
        req = urllib2.Request(args.uri, headers={ 'User-Agent': UA_CHROME })
        class Junk:
            def __init__(self):
                self.data = None
        r1 = Junk()
        r1.data = urllib2.urlopen(req).read()
    else:
        # 3
        http = urllib3.PoolManager(10, headers=user_agent)

        print("getting url data...")
        r1 = http.urlopen('GET', args.uri)
    
    if args.debug and args.verbose:
        print(r1.data)

    if args.debug:
        print("saving debug output to disk...")
        outf = open("out.html","w")
        outf.write(str(r1.data))
        outf.close()

    print("parsing for video url...")
    import re
    P = re.compile("contentUrl\":\"(.*?/\?rc=.*?%3D)")
    
    data = str(r1.data)

    links = P.findall(data)
    if args.debug:
        for link in links:
            print(link)
    
    if len(links)==1:
        print("found good video link...", links[0])
    else:
        print("did not find a video link :(", len(links))

        
    if VERSION==2:

        req = urllib2.Request(links[0], headers={ 'User-Agent': UA_CHROME })
        r2 = Junk()
        r2.data = urllib2.urlopen(req).read()


    else:
        r2 = http.urlopen('GET', links[0])

    outf = open(args.output,"wb")
    outf.write(r2.data)
    outf.close()


if __name__ == "__main__":
    mainline()