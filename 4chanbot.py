import basc_py4chan
import string
import re
from collections import Counter
# board = basc_py4chan.Board('biz')
# thread = b.get_thread(423491034)
# print(thread)
boardName = 'biz'
#boardName = 'biz'
board = basc_py4chan.Board(boardName)
thread_ids = board.get_all_thread_ids()
str_thread_ids = [str(id) for id in thread_ids]  # need to do this so str.join below works
boardName = '/'+boardName+'/'
# print('There are', len(thread_ids), 'active threads on ',boardName,':', ', '.join(str_thread_ids))
dictionary = Counter()

for threadID in thread_ids:
	thread = board.get_thread(threadID)
	topic = thread.topic
	subject = topic.subject
	# print type (subject)
	if type(subject) == unicode:


		strong = subject.encode('ascii', 'ignore').lower()
		# strong = ''.join(subject).lower().encode('ascii','ignore')

		allow = string.letters + string.digits + ' ' + '\'' + '-'
		lol = re.sub('[^%s]' % allow,'',strong)

		lol = lol.split()

		# print('Subject:', lol)    #, 'Comment:', topic.text_comment)

		for word in lol:
			if word in dictionary:
				dictionary[word] += 1
			else:
				dictionary[word] = 1


for threadID in thread_ids:
	thread = board.get_thread(threadID)
	posts = thread.all_posts
	


	for post in posts:
		# print(post.text_comment)
		strong = post.comment.encode('ascii', 'ignore').lower()
		# strong = ''.join(subject).lower().encode('ascii','ignore')

		allow = string.letters + string.digits + ' ' + '\'' + '-'
		lol = re.sub('[^%s]' % allow,'',strong)
		lol = lol.split()
		for word in lol:
			if word in dictionary:
				dictionary[word] += 1
			else:
				dictionary[word] = 1

print dictionary

#for file in thread.files():
 #   print(file)

# In a while...
#print("I fetched", thread.update(), "new replies.")