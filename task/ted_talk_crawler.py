import json
import requests
from bs4 import BeautifulSoup


class TedTalkCrawler:

    def __init__(self):
        pass

    def get_params(self, data):
        params = {}
        if "sort" in data and data["sort"]:
            params["sort"] = data["sort"]
        if "topic" in data and data["topic"]:
            params["topics[]"] = data["topic"]
        return params

    def get_headers(self, data):
        headers = {}
        headers["Content-Type"] = "application/json"
        return headers

    def main(self, data):
        url = "https://www.ted.com/talks"
        params = self.get_params(data)
        resp = requests.get(url, params)
        html = resp.text
        soup = BeautifulSoup(html, "html.parser")
        browse_res = soup.find(id="browse-results")
        tlk_lnks = browse_res.find_all("div", {"class": "talk-link"})
        final_res = [{"img": each.find("img")["src"], "speaker": each.find("h4").text,
                      "title": each.find_all("a", {"class": "ga-link"})[-1].text,
                      "link": each.find_all("a", {"class": "ga-link"})[-1]["href"],
                      "meta": each.find("div", {"class": "meta"}).text} for each in tlk_lnks]
        json.dump(final_res, open("crawl_res.json", "w"), indent=4)



if __name__=='__main__':
    data = {"topic": ["entertainment", "technology"], "sort": "newest"}
    OBJ = TedTalkCrawler()
    OBJ.main(data)