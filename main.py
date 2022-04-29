from flask import Flask, request, render_template
import run

app = Flask(__name__,  template_folder='./flask/templates/')


@app.route('/')
def start():
    page = '<form method="post" enctype="multipart/form-data" action="/background-separation"><input type="file" name="image"><button type="submit">Send</button></form>'
    return page


@app.route('/background-separation', methods=['POST'])
def main():
    file = request.files['image']
    file.save('./flask/static/input.jpeg')
    run.run('./flask/static/input.jpeg')
    return render_template('out.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0')
