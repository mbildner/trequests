from time import time
import requests



languages_list = [
	"English", 
	"French",
	"German",
	"Swahili",
	"Tagalog", 
	"Hebrew", 
	"Spanish",
	"Arabic",
	"Hindi",
	"Persian"
	]

languages_responses = dict()



def keep_running_check(languages_list, languages_responses):
	if len(languages_list) == len(languages_responses):
		kill_reactor()
		print "Kill reactor"
	else:
		print "Keep reactor alive"
		pass

def non_blocking_language_scraper(language, languages_responses):
	url = 'http://en.wikipedia.org/wiki/%s' % language
	r = requests.get(url)
	languages_responses[language] = r
	keep_running_check(languages_list, languages_responses)


def kill_reactor():
	from twisted.internet import reactor
	reactor.stop()

from twisted.internet import reactor


for language in languages_list:
	reactor.callWhenRunning(non_blocking_language_scraper, language, languages_responses)

reactor.run()

print languages_responses





