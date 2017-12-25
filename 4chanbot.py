import basc_py4chan
# board = basc_py4chan.Board('biz')
# thread = b.get_thread(423491034)
# print(thread)
boardName = 'biz'
#boardName = 'biz'
board = basc_py4chan.Board(boardName)
thread_ids = board.get_all_thread_ids()
str_thread_ids = [str(id) for id in thread_ids]  # need to do this so str.join below works
boardName = '/'+boardName+'/'
print('There are', len(thread_ids), 'active threads on ',boardName,':', ', '.join(str_thread_ids))

#for file in thread.files():
 #   print(file)

# In a while...
#print("I fetched", thread.update(), "new replies.")