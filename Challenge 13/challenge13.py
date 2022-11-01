import urllib.request
import html

def read_web(url):
    mybytes = fp.read()
    mystr = mybytes.decode("utf-8") 
    mystr = html.unescape(mystr) 
    return mystr

def get_singles(mystr):
    position1 = mystr.find('<div class="title">') 
    position2 = mystr.find('<div class="artist">')
    count = 1
    while position1 != -1 and count <= 10 and position2 != -1: 
        start = mystr.find(">",position1+len('<div class="title">'))+1 
        stop = mystr.find("<",start)                                  
 
        a = mystr.find(">",position2+len('<div class="artist">'))+1
        b = mystr.find("<",a)
        
        print(f"{count} - {mystr[start:stop]}")
        print(f"{mystr[a:b]}", "\n")
        position1 = mystr.find('<div class="title">',stop)
        position2 = mystr.find('<div class="artist">',b)
        
        count += 1
        



if __name__ == "__main__":
    fp = urllib.request.urlopen("https://www.officialcharts.com/charts/singles-chart/")
    web_str = read_web(fp)
    get_singles(web_str)
