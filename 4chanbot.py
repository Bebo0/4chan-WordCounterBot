import basc_py4chan
import string
import re
from collections import Counter

# USAGE: 
#       1) in terminal, cd to folder that contains the files
#       2) type python 4chanbot.py

# VARIABLES:
boardName = 'biz'
dictionary = Counter()





def runBot(board, threadIDs):
	parseThreadTitles(board, threadIDs)
	parseThreadPosts (board, threadIDs)



def parseThreadTitles(board, threadIDs):
	""" Parses thread titles and adds them to dictionary

	Board ArrayOfthread_id -> void
	
	Arguments:
		board {Board} -- the board being parsed
		threadIDs {ArrayOfthread_id} -- the ids of all threads being parsed
	"""
	
	
	

	for threadID in threadIDs:
		thread = board.get_thread(threadID)
		topic = thread.topic
		subject = topic.subject
		# print type (subject)
		if type(subject) == unicode:
			strong = subject.encode('ascii', 'ignore').lower()
			parsingHelper(strong)

def parsingHelper(strong):
	"""
	Splits strong into individual strings then adds them to the dictionary 
	
	"""
	allowedSymbols = string.letters + string.digits + ' ' + '\'' + '-'
	aos = re.sub('[^%s]' % allowedSymbols,'',strong)
	aos = aos.split()
	addArrToDictionary(aos)


def addArrToDictionary(aos):
	"""
	ArrayOfStrings -> void

	Adds all strings in given array to dictionary

	Arguments:
		aos {ArrayOfStrings} -- contains all the words to be added to dictionary
	"""

	for word in aos:
		if word in dictionary:
			dictionary[word] += 1
		else:
			dictionary[word] = 1


def parseThreadPosts(board, threadIDs):
	""" Parses all thread posts and adds them to dictionary
	
	Board ArrayOfthread_id -> void
	
	Arguments:
		board {Board} -- the board being parsed
		threadIDs {ArrayOfthread_id} -- the ids of all threads being parsed
	"""

	for threadID in threadIDs:
		thread = board.get_thread(threadID)
		posts = thread.all_posts
	


		for post in posts:
			# print(post.text_comment)
	 		strong = post.comment.encode('ascii', 'ignore').lower()
	 		parsingHelper(strong)
# 		# strong = ''.join(subject).lower().encode('ascii','ignore')

# 		allow = string.letters + string.digits + ' ' + '\'' + '-'
# 		lol = re.sub('[^%s]' % allow,'',strong)
# 		lol = lol.split()
# 		for word in lol:
# 			if word in dictionary:
# 				dictionary[word] += 1
# 			else:
# 				dictionary[word] = 1

#boardName = 'biz'


#str_thread_ids = [str(id) for id in thread_ids]  # need to do this so str.join below works
#boardName = '/'+boardName+'/'
# print('There are', len(thread_ids), 'active threads on ',boardName,':', ', '.join(str_thread_ids))

# for threadID in thread_ids:
# 	thread = board.get_thread(threadID)
# 	topic = thread.topic
# 	subject = topic.subject
# 	# print type (subject)
# 	if type(subject) == unicode:


# 		strong = subject.encode('ascii', 'ignore').lower()
# 		# strong = ''.join(subject).lower().encode('ascii','ignore')

# 		allow = string.letters + string.digits + ' ' + '\'' + '-'
# 		lol = re.sub('[^%s]' % allow,'',strong)

# 		lol = lol.split()

# 		# print('Subject:', lol)    #, 'Comment:', topic.text_comment)

# 		for word in lol:
# 			if word in dictionary:
# 				dictionary[word] += 1
# 			else:
# 				dictionary[word] = 1


# for threadID in thread_ids:
# 	thread = board.get_thread(threadID)
# 	posts = thread.all_posts
	


# 	for post in posts:
# 		# print(post.text_comment)
# 		strong = post.comment.encode('ascii', 'ignore').lower()
# 		# strong = ''.join(subject).lower().encode('ascii','ignore')

# 		allow = string.letters + string.digits + ' ' + '\'' + '-'
# 		lol = re.sub('[^%s]' % allow,'',strong)
# 		lol = lol.split()
# 		for word in lol:
# 			if word in dictionary:
# 				dictionary[word] += 1
# 			else:
# 				dictionary[word] = 1

#print dictionary

#for file in thread.files():
 #   print(file)

# In a while...
#print("I fetched", thread.update(), "new replies.")
#
#
def main():
	board = basc_py4chan.Board(boardName)
	threadIDs = board.get_all_thread_ids()
	
	runBot(board, threadIDs)
	print dictionary

if __name__ == '__main__':
	main()