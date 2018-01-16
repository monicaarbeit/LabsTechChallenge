from flask import Flask, render_template

app = Flask(__name__)


@app.route('/mna2126', methods=['GET'])
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
