import basc_py4chan
import string
import re
from collections import Counter

# USAGE: 
#       1) in terminal, cd to folder that contains the files
#       2) type python 4chanbot.py

# VARIABLES:
boardName = 'biz'
counter = Counter()

# FUNCTIONS:
def addArrToCounter(aos):
	""" Adds the occurence of all strings in given array to counter

	ArrayOfStrings -> void

	Arguments:
		aos {ArrayOfStrings} -- contains all the words to be added to counter
	"""

	for word in aos:
		if word in counter:
			counter[word] += 1
		else:
			counter[word] = 1


def parsingHelper(strong):
	""" Splits strong into individual strings then adds them to the counter 

	Strong -> void
	
	"""
	allowedSymbols = string.letters + string.digits + ' ' + '\'' + '-'
	aos = re.sub('[^%s]' % allowedSymbols,'',strong)
	aos = aos.split()
	addArrToCounter(aos)


def parseThreadPosts(board, threadIDs):
	""" Parses all thread posts and adds them to counter
	
	Board ArrayOfthread_id -> void
	
	Arguments:
		board {Board} -- the board being parsed
		threadIDs {ArrayOfthread_id} -- the ids of all threads being parsed
	"""
	print "Parsing thread posts..."
	for threadID in threadIDs:
		thread = board.get_thread(threadID)
		posts = thread.all_posts
	
		for post in posts:
	 		strong = post.comment.encode('ascii', 'ignore').lower()
	 		parsingHelper(strong)
	print "Successfully parsed thread posts!"


def parseThreadTitles(board, threadIDs):
	""" Parses thread titles and adds them to counter

	Board ArrayOfthread_id -> void
	
	Arguments:
		board {Board} -- the board being parsed
		threadIDs {ArrayOfthread_id} -- the ids of all threads being parsed
	"""
	print "Parsing thread titles..."
	for threadID in threadIDs:
		thread = board.get_thread(threadID)
		topic = thread.topic
		subject = topic.subject
		# print type (subject)
		if type(subject) == unicode:
			strong = subject.encode('ascii', 'ignore').lower()
			parsingHelper(strong)
	print "Successfully parsed thread titles!"


def runBot(board, threadIDs):
	""" Runs the bot
	
	Parses both thread titles and thread posts
	
	Board thread_id -> void

	Arguments:
		board {Board} -- the board being parsed
		threadIDs {ArrayOfthread_id} -- the ids of all threads being parsed
	"""
	parseThreadTitles(board, threadIDs)
	parseThreadPosts (board, threadIDs)


def main():
	board = basc_py4chan.Board(boardName)
	threadIDs = board.get_all_thread_ids()
	
	runBot(board, threadIDs)
	print counter

if __name__ == '__main__':
	main()