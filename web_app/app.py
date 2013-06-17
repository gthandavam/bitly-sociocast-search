"""
This file is part of the flask+d3 Hello World project.
"""
import json
import requests
import flask
import numpy as np
from runner import get_links
from classify import get_categories

app = flask.Flask(__name__)

@app.route("/")
def index():
    """
    When you request the root path, you'll get the index.html template.

    """
    return flask.render_template("index.html")


@app.route("/flare")
def get_flare():
    with open("flare.json") as f:
        return json.dumps(json.loads(f.read()))

@app.route("/jack2", methods=['GET','POST'])
def more_data_jack():
    with open("jack2.json") as f:
        j = json.loads(f.read())
    return json.dumps(j)

@app.route("/jack", methods=['GET','POST'])
def data_jack():
    start = flask.request.args.get('start')
    w = get_links(start)
    j = get_categories(w)
    print j
    r = {}
    for u in j.keys():
        for c in j[u]['classification']:
            r.setdefault(c, []).append(u)
    with open('jack2.json', 'wb') as f:
        f.write( json.dumps(r) )
    print
    print 'done'
    return flask.render_template("index.html")

'''
@app.route("/")
def index():
    """
    When you request the root path, you'll get the index.html template.

    """
    return flask.render_template("index.html")


@app.route("/data")
@app.route("/data/<int:ndata>")
def data(ndata=100):
    """
    On request, this returns a list of ``ndata`` randomly made data points.

    :param ndata: (optional)
        The number of data points to return.

    :returns data:
        A JSON string of ``ndata`` data points.

    """
    print 'ndata = ' + str(ndata)
    x = 10 * np.random.rand(ndata) - 5
    y = 0.5 * x + 0.5 * np.random.randn(ndata)
    A = 10. ** np.random.rand(ndata)
    c = np.random.rand(ndata)
    return json.dumps([{"_id": i, "x": x[i], "y": y[i], "area": A[i],
        "color": c[i]}
        for i in range(ndata)])

@app.route("/data2")
@app.route("/data2/<int:ndata>")
def data(ndata=100):
    """
    On request, this returns a list of ``ndata`` randomly made data points.

    :param ndata: (optional)
        The number of data points to return.

    :returns data:
        A JSON string of ``ndata`` data points.

    """
    print 'ndata2 = ' + str(ndata)
    x = 10 * np.random.rand(ndata) - 5
    y = 0.5 * x + 0.5 * np.random.randn(ndata)
    A = 10. ** np.random.rand(ndata)
    c = np.random.rand(ndata)
    return json.dumps([{"_id": i, "x": x[i], "y": y[i], "area": A[i],
        "color": c[i]}
        for i in range(ndata)])
'''


if __name__ == "__main__":
    import os

    port = 9000

    # Open a web browser pointing at the app.
    os.system("open http://localhost:{0}".format(port))

    # Set up the development server on port 8000.
    app.debug = True
    app.run(port=port)
