import requests
from bs4 import BeautifulSoup  # beautiful soup is great for web scraping
import pprint

# grabbing info of a website from a server
response = requests.get('https://news.ycombinator.com')
response2 = requests.get('https://news.ycombinator.com/?p=2')
# .parser tells it to convert the text from a string into html, so we can use it
soup = BeautifulSoup(response.text, 'html.parser')
soup2 = BeautifulSoup(response.text, 'html.parser')
# titleline is the name for links in the hacker news coding
links = (soup.select('.titleline'))
# subtext is hat comes underneath the title
subtext = (soup.select('.subtext'))


links2 = (soup.select('.titleline'))
subtext2 = (soup.select('.subtext'))

mega_links = links + links2
mega_subtext = subtext +subtext2
# sorting by points
def sort_stories_by_votes(hnlist):
    # the key that we sort by is votes and reverse makes it descending
    return sorted(hnlist, key=lambda k:k['votes'], reverse=True)


# making custom hn website so only articles with 110+ votes appear
def create_custom_hn(links, subtext):
    hn = []
    # for each item on website:
    # enumerate
    for idx, item in enumerate(links):

        title = item.getText()
        # grabs the href of each link on page and if there is none then it becomes none
        href = item.get('hrf', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            # getting num of votes        here its saying if there is ' points' or 0 points replace with empty string
            points = int(vote[0].getText().replace(' points', ''))
            # if story has more than 100 points then we want to append it
            # displaying link and text and votes
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)


pprint.pprint(create_custom_hn(mega_links, mega_subtext))
# now we have just the body in the html file
# print(soup.body)

# finds all a tags: print(soup.find_all("a"))
# finds the thing with an id of that: print(soup.find(id="score_20514755"))
