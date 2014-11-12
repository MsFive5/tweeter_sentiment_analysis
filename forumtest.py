fp = open('outputtest.txt')
for line in fp:
    x = line.split()
    if len(x) != 2:
        print 'WARNING: ', len(x), 'instead of 2 items per line:', line