
DEBUG = True
VERBOSE = False
 
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

    # import urllib3
    import urllib2
    opener = urllib2.build_opener()
    opener.addheaders = [("User-Agent", "")]

    # this is chrome76
    UA_CHROME = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
    # user_agent = {'user-agent': UA_CHROME }
    # http = urllib3.PoolManager(10, headers=user_agent)
    
    opener = urllib2.build_opener()
    opener.addheaders = [("User-Agent", "")]

    print("getting url data...")
    # r1 = http.urlopen('GET', args.uri)
    r1 = opener.open(args.uri)

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
    
    # inf = open("out.html","r")
    # data = inf.read()
    # inf.close()
    data = str(r1.data)

    links = P.findall(data)
    if args.debug:
        for link in links:
            print(link)
    
    if len(links)==1:
        print("found good video link...", links[0])
    
    # r2 = http.urlopen('GET', links[0])
    r2 = opener.open(links[0])

    outf = open(args.output,"wb")
    outf.write(r2.data)
    outf.close()


if __name__ == "__main__":
    mainline()
