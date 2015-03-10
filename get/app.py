from flask import Flask, request


app = Flask(__name__)


@app.route('/api/')
def form_view():
    version = request.args.get('version')
    key = request.args.get('key')
    return "version: %s, key: %s" % (version, key)


if __name__ == '__main__':
    app.debug = True
    app.run()

