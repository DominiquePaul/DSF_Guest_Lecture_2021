"""
Things to consider when using file uploads

    1. Use FileField, imported from flask_wtf (not wtforms)

    2. Ideally, specify a folder where you want files uploaded to

    3. In your formtag in your html file, set enctype="multipart/form-data".
        This format is required when at least one of the fields in the form is
        a file field.

Further reading for working with file uploads
https://blog.miguelgrinberg.com/post/handling-file-uploads-with-flask
"""

from flask import Flask, render_template, url_for

from wtforms import SubmitField
from wtforms.validators import DataRequired

from flask_wtf import FlaskForm
from flask_wtf.file import FileField

# we call these functions from our own code
from call_automl import classify_image_with_automl

app = Flask(__name__)
app.config["SECRET_KEY"] = "enter-a-hard-to-guess-string"


class FileUpload(FlaskForm):
    user_file = FileField("Your Data", validators=[DataRequired()])
    submit = SubmitField("Submit")


@app.route('/', methods=['GET', 'POST'])
def index():

    prediction, score = (None, None)

    form = FileUpload()

    if form.validate_on_submit():

        file_as_bytes = form.user_file.data.read()

        prediction, score = classify_image_with_automl(file_as_bytes)

        score = round(score,3)*100

    return render_template("index.html", form=form, prediction=prediction, score=score)


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=80)
