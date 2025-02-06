import flask 

app = flask.Flask(__name__)


@app.route('/')
def index():
    return flask.render_template('concept.html')


@app.route('/page1')
def page1():
    return flask.render_template('page1.html')  






@app.route('/page2')
def page2():
    return flask.render_template('page2.html')




@app.route('/amazon_watches')
def amazon_watches():
    page_numbers = [1,2,3,4,5,6,7,8,9,10]
    all_watches = []
    for page in page_numbers:
        address = f'https://www.amazon.com.au/s?k=watches&page={page}&qid=1736409790&xpid=LkrxOpdcBsmDj&ref=sr_pg_2'
        all_watches.append(address)
    return flask.render_template('amazon_watches.html',watches_adresses = all_watches)



app.run(debug=True)