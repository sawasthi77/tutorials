import sys, time
try:
    def backward():
        for n in range (4, 0, -1):
            print(' '*n, end = '')
            print('********')
    def forward():
        for i in range (4):
            print(' '*i, end = '')
            print('********')
    while True:
        backward()
        time.sleep(0.1)
        forward()
   
except KeyboardInterrupt:
    sys.exit()

