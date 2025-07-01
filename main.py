from flask import Flask, jsonify
from bs4 import BeautifulSoup
import requests
from datetime import datetime

app = Flask(__name__)

@app.route('/recent-meetings')
def get_todays_meetings():
    url = "https://www.racingpost.com/racecards/"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    today = datetime.now().strftime("%d %b").lstrip("0")

    meetings = []
    for link in soup.select("a.rc-meeting-item__link"):
        date_element = link.select_one(".rc-meeting-item__header-date")
        course_element = link.select_one(".rc-meeting-item__course-name")
        if date_element and course_element and today in date_element.text:
            meetings.append(course_element.text.strip())

    return jsonify({"date": today, "meetings": meetings})

@app.route('/')
def index():
    return "WINA Race Scraper is running."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)