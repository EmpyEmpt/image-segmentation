import model as md
import tensorflow as tf
import cv2
import config as cfg
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def start():
    page = '<form method="post" enctype="multipart/form-data" action="/background-separation"><input type="file" name="image"><button type="submit">Send</button></form>'
    return page


@app.route('/background-separation', methods=['POST'])
def main():
    file = request.files['image']
    file.save('./static/input.jpeg')
    run('./static/input.jpeg',
        './static/output.png', './static/mask.jpeg')
    return render_template('out.html')


# I fought of moving it to a different file or breaking it into functions
#   but it's small anyways...
def run(im, save_path, mask_path):
    image = cv2.imread(im)

    image = tf.image.resize(
        image, (cfg.IMAGE_SIZE, cfg.IMAGE_SIZE), method="nearest")
    image /= 255
    image = tf.expand_dims(image, axis=0)
    res = model(image)[0].numpy()

    cv2.imwrite(mask_path, res * 255)

    res[res > 0.5] = 2
    res[res <= 0.5] = 1
    res[res == 2] = 0

    image = image[0].numpy()
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    r, g, b = cv2.split(image)
    image = cv2.merge([b, g, r, res], 4)

    image = image * 255
    cv2.imwrite(save_path, image)


if __name__ == "__main__":
    model = md.load_model()
    app.run(host='0.0.0.0')
