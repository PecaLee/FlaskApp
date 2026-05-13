# BLUEPRINT | DONT EDIT

from flask import Flask, render_template, request
import json

app = Flask("JobScraper")


def load_jobs():
    with open("jobs.json", "r") as f:
        return json.load(f)

# /BLUEPRINT


# 👇🏻 YOUR CODE 👇🏻:

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    if not keyword:
        return render_template("search.html", keyword="", jobs=[])
    
    keyword_lower = keyword.lower()
    jobs = load_jobs()
    matched_jobs = []
    
    for job in jobs:
        if (keyword_lower in job['title'].lower() or 
            keyword_lower in job['company_name'].lower() or 
            keyword_lower in job['description'].lower()):
            matched_jobs.append(job)
            
    return render_template("search.html", keyword=keyword, jobs=matched_jobs)

# /YOUR CODE


# BLUEPRINT | DONT EDIT

if __name__ == "__main__":
    app.run(port=5000)

# /BLUEPRINT