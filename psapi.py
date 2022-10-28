from psaw import PushshiftAPI
import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
import requests


base_url = 'https://api.pushshift.io/reddit/search/submission'
params = {'subreddit': 'asoiaf'}
res = requests.get(base_url, params)
data = res.json()
posts = data['data']

def get_posts():
	pass


def main():
	pass


if __name__ == '__main__':
	main()
