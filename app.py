from flask import Flask, render_template, url_for, request
from example import add2
from ml import add 

# from startertest import add

app= Flask(__name__)


@app.route('/')
def index():
    desc = request.args.get("desc")
    return render_template("index.html", desc= desc)


@app.route('/summary')
def summary():
    desc = request.args.get("desc")
    # ml_pipeline(head, name)
    # descrip=['python based project on image caption generator - learn to build a working model of image caption generator by implementing cnn &amp; a type of rnn (lstm) together."', 'a neural network to generate captions for an image using cnn and rnn with beam search. - dabasajay/image-caption-generator"', 'an overview of image caption generation methods" name="title"/>', 'explore and run machine learning code with kaggle notebooks | using data from flicker8k_dataset"', '/exchanges/models/all/max-image-caption-generator/--https://developer.ibm.com/technologies/artificial-intelligence" name="madeupmeta"/>', 'Image caption generator', 'Image caption generator', '/exchanges/models/all/max-image-caption-generator/--https://developer.ibm.com/technologies/artificial-intelligence" name="madeupmeta"/>', 'explore and run machine learning code with kaggle notebooks | using data from flicker8k_dataset"', 'python based project on image caption generator - learn to build a working model of image caption generator by implementing cnn &amp; a type of rnn (lstm) together."']

    return render_template("results.html", desc= desc, options=add(desc))

if __name__== "__main__":
    app.run(debug=True)