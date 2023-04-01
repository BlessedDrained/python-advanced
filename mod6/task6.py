from flask import Flask, url_for

app = Flask(__name__)


@app.route('/hw')
def hello_world():
    return 'Hello World!'


@app.route('/bye')
def good_bye():
    return 'Good bye!'


def has_no_empty_params(rule):
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)


@app.errorhandler(404)
def list_routes(err):
    links = []
    for rule in app.url_map.iter_rules():
        if "GET" in rule.methods and has_no_empty_params(rule):
            url = url_for(rule.endpoint, **(rule.defaults or {}))
            links.append((url, rule.endpoint))
    text = 'Such address does not exist. Available endpoints are: '
    return text + "\n".join([x[0] for x in links])


if __name__ == '__main__':
    app.run()
