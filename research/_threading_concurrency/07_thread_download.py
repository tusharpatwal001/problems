import threading
import requests
import time


def download(url):
    print(f"Starting download from {url}")
    resp = requests.get(url)
    print(f"Finished downloading from {url}, size: {len(resp.content)}")


urls = [
    "https://httpbin.org/image/jpeg",
    "https://httpbin.org/image/png",
    "https://httpbin.org/image/svg",
]

start = time.perf_counter()

threads = []
for url in urls:
    t = threading.Thread(target=download, args=(url, ))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

end = time.perf_counter()

print("Total time taken", end - start)
