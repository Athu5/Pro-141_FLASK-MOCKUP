from flask import Flask, jsonify, request
from storage import all_articles, liked_articles, not_liked_articles
import csv

app = Flask(__name__)


@app.route("/get-articles")
def get_article():
    articles_data = {
        "title": all_articles[0][10],
        "url": all_articles[0][9],
        "lang": all_articles[0][12],
        "contentId": all_articles[0][2],
        "eventType": all_articles[0][1]
    }
    return jsonify({
        "data": articles_data,
        "status": "success"
    })


@app.route("/liked-articles", methods=["POST"])
def liked_article():
    with open('shared_articles.csv', encoding = "utf8") as f:
        reader = csv.reader(f)
        data = list(reader)
        all_articles = data[1:]
        
    articles = all_articles[0]
    all_articles = all_articles[1:]
    liked_articles.append(articles)
    return jsonify({
        "status": "success"
    }), 201


@app.route("/not-liked-articles", methods=["POST"])
def unliked_articles():
    articles = all_articles[0]
    all_articles = all_articles[1:]
    not_liked_articles.append(articles)
    return jsonify({
        "status": "success"
    }), 201


if __name__ == "__main__":
    app.run()
# done
