from urllib import *
import sys

class WebGrab():

    count = 0
    
    def download(self, url):
        filename = 'capture' + str(self.count) + '.txt'
        f= open(filename, 'a')
        urlretrieve(url, filename)
        f.close()
        
        self.count += 1

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print 'useage: MyWeb url'
    else:    
        mine = WebGrab(argv[1])

        mine.download(url)
