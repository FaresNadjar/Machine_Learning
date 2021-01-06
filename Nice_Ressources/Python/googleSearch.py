import requests 
from parsel import Selector
import pprint


def get_digits_string(ch):
    # get only digits from a string
    digits = ""
    for i in range(0, len(ch)):
        if ch[i].isdigit():
            digits += ch[i]
    return int(digits)

def get_single_attribut(document, xpaths):

    # get the variables as an array and the one that exists
    for xpath in xpaths:
        attribut = extract_element(document, xpath)
        if attribut is not None:
            return attribut

def get_selector(document, xpath):

    # return the DOM from xpath
    return document.xpath(xpath)

def extract_element(document, element):
    # extract a xpath from the document given
    return document.xpath(element).extract_first()


def google(site,search):
    #xpath variables to extract data
    xpath_links = '//div[@class="rc"]'
    xpath_text = ['div[@class="r"]/a/h3/span/text()','div[@class="r"]/a/h3/text()']
    xpath_result_link = ['div[@class="r"]/a/@href']
    #header information for request
    headers_Get = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    }
    #prepare the search query to google
    query = site + " " + search
    s = requests.Session()
    query = '+'.join(query.split())
    #force google to get english results
    url = 'https://www.google.fr/search?q=' + query + '&ie=utf-8&oe=utf-8&gl=uk'
    r = s.get(url, headers=headers_Get)
    doc = Selector(text=r.text)
    Results_Query = get_selector(doc,xpath_links)
    #get all the result from the first page only
    for single_result in Results_Query : 
        url = get_single_attribut(single_result,xpath_result_link)
        text = get_single_attribut(single_result,xpath_text)
        result = {'text': text, 'url': url}
        pprint.pprint(result)
        choice = input('Enter Y to validate the choice or other key to the Next choice')
        #if the choise is Y then we get the ID of the team from URL 
        if (choice.upper()=='Y'):
            Id = get_digits_string(url)
            #TODO code

            print(Id)
            break

#Test the google function
site = "sofifa.com"
search = "Man City"
result = google("site:" + site ,search)







