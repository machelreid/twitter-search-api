from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
from threading import Timer
class Twitter:
    """
    Parameters: Twitter(outputfilename, scrollnumber, tweet_number)
    """
    def __init__(self, filename = 'output', scroll_number = 1000, tweet_number = 100):
        self = self
        self.filename = filename
        self.scroll_number = scroll_number
        self.tweet_number = tweet_number

    # def __str__(self):
    #     print('I am a tweet scraper')

    def find_tweets(self, all_words = [], required_phrase = [], either_or = [], none_of_these = [], hashtag = [], dates = []):
        """
        Finds tweets with key search phrases (shown above)
        """
        query = u''
        number = []
        for i in all_words:
            query+= (i+'%20')
        for i in required_phrase:
            query+= ('"'+i+'"%20')
        if len(either_or) != 0:
            query+='('
            for i in either_or:
                query+= (i+'%20OR%20')
            query = query [:-8] + ')%20'
        for i in none_of_these:
            query += '-'+i+'%20'
        if len(hashtag) != 0:
            query += '('
            for i in hashtag:
                query += '%23' + i + '%20OR%20'
            query = query [:-8] + ')'
        if len(dates) != 0:
            query+= '%20since%3A'+dates[0]+'%20until%3A'+dates[1]
        query += '&src=typed_query'
    
  
        browser = webdriver.Chrome(executable_path='./chromedriver.exe')
        browser.get(u'https://twitter.com/search?q='+query)
        time.sleep(1)
    
        body = browser.find_element_by_tag_name('body')

        def len_tweets():
           return len(browser.find_elements_by_class_name('tweet-text')) 
    
        for _ in range(self.scroll_number):
            body.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.00000000001)
            if _%5 == 1: 
                if len_tweets() >= self.tweet_number:
                    print(len(browser.find_element_by_class_name('tweet-text')))
                    break
                else:
                    number.append(len_tweets())
                    try:
                        if number[-1] == number[-7]:
                            print(number)
                            print(len_tweets())
                            break
                    except IndexError:
                        pass

    
        tweets = browser.find_elements_by_class_name('tweet-text')
    
        # tweets = soup.find_all("div", class_="css-901oao r-hkyrab r-gwet1z r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0")
        for tweet in tweets:
            print(tweet.text)
    
        with open(self.filename+'.txt','w', encoding='utf8') as f:
            if tweets == []:
                f.write("THERE WAS NOTHING HERE!!!!!!!")
            for tweet in range(self.tweet_number - 1):
                try:
                    f.write(tweets[tweet].text+'\n\n\n')
                except IndexError:
                    pass
    
Twitter(tweet_number=100, filename = 'ライフライン').find_tweets(all_words = ['地震'],required_phrase = ['どうなっていますか'],either_or=[], none_of_these=[], dates = ['2006-03-10','2019-12-31'])

