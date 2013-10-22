from time import time
import requests


		


class Trequest(object):
	def __init__(self, url, callback_function):
		self.url = url
		self.callback_function = callback_function

	def __start__(self):
		r = requests.get(self.url)
		self.callback_function(r)
		

		

class TrequestManager(object):
	def __init__(self):
		self.holder = []
		self.responses = []

	def trequest(url, callback_function):
		t = Trequest(url, callback_function)
		self.holder.append(t)

	def __continue__(self):
		if len(self.holder) == len(self.responses):
			return False
		else:
			return True

	def start(self):
		from twisted.internet import reactor
		for t in self.holder:
			reactor.callWhenRunning(t.__start__)






def report(response):
	content = response.content
	print content




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

tlist = [Trequest("http://en.wikipedia.org/wiki/%s" % l, report) for l in languages_list]


from twisted.internet import reactor

for t in tlist:
	reactor.callWhenRunning(t.start)


reactor.run()




# languages_responses = dict()



# def keep_running_check(languages_list, languages_responses):
# 	if len(languages_list) == len(languages_responses):
# 		return True
# 	else:
# 		return False

# def non_blocking_language_scraper(language, languages_responses):
# 	url = 'http://en.wikipedia.org/wiki/%s' % language
# 	r = requests.get(url)
# 	languages_responses[language] = r

# 	if keep_running_check(languages_list, languages_responses):
# 		pass
# 	else:
# 		kill_reactor()		


# def kill_reactor():
# 	from twisted.internet import reactor
# 	reactor.stop()

# from twisted.internet import reactor


# for language in languages_list:
# 	reactor.callWhenRunning(non_blocking_language_scraper, language, languages_responses)


# start = time()
# reactor.run()
# print "took: ", time() - start

# print languages_responses





