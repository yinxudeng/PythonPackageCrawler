from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

html = urlopen("https://www.lfd.uci.edu/~gohlke/pythonlibs/?q=cp33")
bs = BeautifulSoup(html, "html.parser")
packages = bs.find_all("a", {"href": "javascript:;"})
baseDownloadLink = "https://download.lfd.uci.edu/pythonlibs/n5jyqt7p/"

for package in packages:
	packageName = package.get_text()
	packageName = packageName.replace("‑", "-")
	downloadLink = "".join([baseDownloadLink, packageName])
	urlretrieve(downloadLink, packageName)
	print("".join([packageName, " has been downloaded"]))