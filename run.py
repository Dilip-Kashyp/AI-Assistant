import multiprocessing
from main import start


def startai():
        print("Running...............")
        start()
        
if __name__ == '__main__':
        p1 = multiprocessing.Process(target=startai)
        p1.start()
        p1.join()
        print("system stop")   
        