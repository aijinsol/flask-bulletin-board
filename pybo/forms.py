from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

class QuestionForm(FlaskForm):
    subject = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Questions', validators=[DataRequired()])

class AnswerForm(FlaskForm):
    content = TextAreaField('Answers', validators=[DataRequired()])