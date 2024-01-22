import requests
import threading

url = 'your url'

def get_url():
    response = requests.get(url)
    print(response)

def start_thread():
    thr1 = threading.Thread(target=get_url)
    thr2 = threading.Thread(target=get_url)
    thr3 = threading.Thread(target=get_url)
    thr4 = threading.Thread(target=get_url)
    thr5 = threading.Thread(target=get_url)
    thr6 = threading.Thread(target=get_url)

    thr1.start()
    thr2.start()
    thr3.start()
    thr4.start()
    thr5.start()
    thr6.start()

def main():
    for i in range(10000):
        start_thread()


if __name__ == '__main__':
    main()