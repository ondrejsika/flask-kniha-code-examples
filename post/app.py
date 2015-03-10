from flask import Flask, request


app = Flask(__name__)


@app.route('/form/', methods=['POST'])
def form_view():
    name = request.form.get('name')
    email = request.form.get('email')
    return "name: %s, email: %s" % (name, email)


if __name__ == '__main__':
    app.debug = True
    app.run()

