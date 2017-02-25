from flask import Flask, redirect, render_template, request, url_for

import helpers
import os
import sys
import nltk
from analyzer import Analyzer

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():

    # validate screen_name
    screen_name = request.args.get("screen_name", "").lstrip("@")
    if not screen_name:
        return redirect(url_for("index"))

    # get screen_name's tweets
    tweets = helpers.get_user_timeline(screen_name, 100)

    # TODO
    # Absolute paths to positive/negative words lists
    positives = os.path.join(sys.path[0], "positive-words.txt")
    negatives = os.path.join(sys.path[0], "negative-words.txt")
    
    # Instantiate analyzer
    analyzer = Analyzer(positives, negatives)
    
    # Separate comma-separated-values list into a list of strings (each is separated by a "', ")
    newTweetList = list()
    
    # Make sure twitter handle isn't private/non-existent, catch any other errors.
    if(tweets == None):
        return redirect(url_for("index"))
        print("User is protected, non-existent, Invalid API_KEY/SECRET, or you've hit a rate limit.")
    
    # Put the tweets into separate indices for the new list
    for i in range (len(tweets)):
        newTweetList.append(tweets[i].strip("', "))
    
    # Initialize values for the pie chart
    positive, negative, neutral = 0.0, 0.0, len(newTweetList)
    
    # Change the "sentiment value" while analyzing
    for i in range (len(newTweetList)):
        score = analyzer.analyze(newTweetList[i])
        if score > 0.0:
            positive += 1
            neutral -= 1
        elif score < 0.0:
            negative += 1
            neutral -= 1
    
    # generate chart (Making sure adds up to 100%)
    chart = helpers.chart( (positive / (positive+negative+neutral)), 
                           (negative / (positive+negative+neutral)), 
                           (neutral / (positive+negative+neutral)) )

    # render results
    return render_template("search.html", chart=chart, screen_name=screen_name)