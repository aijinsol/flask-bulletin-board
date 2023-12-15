from datetime import datetime
from flask import Blueprint
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.utils import redirect

from .. import db
from ..models import Question
from ..forms import QuestionForm
from ..forms import AnswerForm


bp = Blueprint('question', __name__, url_prefix='/question')


@bp.route('/list/')
def _list():
    q_list = Question.query.order_by(Question.create_date.desc())
    return render_template('question/question_list.html', q_list=q_list)

@bp.route('/detail/<int:qid>/')
def detail(qid):
    form = AnswerForm()
    q = Question.query.get_or_404(qid)
    return render_template('question/question_detail.html', q=q, form=form)

@bp.route('/create/', methods=('GET', 'POST'))
def create():
    form = QuestionForm()
    if request.method == 'POST' and form.validate_on_submit():
        q = Question(subject=form.subject.data, content=form.content.data, create_date=datetime.now())
        db.session.add(q)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('question/question_form.html', form=form)
