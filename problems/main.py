import requests
import json


def getUsernames(threshold):
    total_pages = 1
    i = 1
    res = []
    while i <= total_pages:
        resp = requests.get(f"https://jsonmock.hackerrank.com/api/article_users?page={i}")
        total_pages = resp.json()["total_pages"]
        for user in resp.json()["data"]:
            if user["submission_count"] > threshold:
                res.append(user["username"])
        i += 1
    return res


def get_lyrics():
    url = "https://www.google.com/search?q=oasis wonderwall lyrics"
    resp = requests.get(url)
    print(resp.content)


if __name__ == "__main__":
    print(get_lyrics())
