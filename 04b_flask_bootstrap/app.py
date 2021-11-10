from flask import Flask, render_template
import requests
import xmltodict


app = Flask(__name__)

@app.route("/")
def home():
    return "Hello world!"


# we can also get variables from the header
@app.route("/greet/<name>")
def greet(name):
    return f"Hello {name}"


# function that we call in one of the URLs
def get_last_arxiv_paper(query):
    # Fetch the data from the API (this API has not registration)
    base_url = "http://export.arxiv.org/api/query"
    params = {"search_query": query}
    r = requests.get(base_url, params)

    # This API supports a different format than json, we can convert this though
    # via the xmltodict package (first google result when googling the issue)
    json_response = xmltodict.parse(r.content)

    # get the first entry
    first_entry = json_response["feed"]["entry"][0]
    title = first_entry["title"]

    # Multiple authors are listed in different branches of the dictionary.
    # We want to get all of their names
    list_of_authors = []

    for author_entry in first_entry["author"]:
        list_of_authors += [author_entry["name"]]
    # we can join the list of author names together, separated by a comma
    authors = ", ".join(list_of_authors)

    return(title, authors)

# A more interesting version of using terms in the url
@app.route("/arxiv/<query_term>")
def arxiv(query_term):

    title, author = get_last_arxiv_paper(query_term)

    # these strings are called f-strings, they are available as of python 3.6
    result = f"'{title}' authored by {author}"

    # alternative formatting if you have an older version of python installed
    # result = "'{}' authored by {}".format(title, author)

    return result


@app.route("/html")
def nicer_html():
    return render_template("template1.html")


@app.route("/bootstrap")
def bootstrap():
    return render_template("bootstrap.html")




if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
