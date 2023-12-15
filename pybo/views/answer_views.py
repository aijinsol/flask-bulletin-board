from datetime import datetime
from flask import Blueprint
from flask import url_for
from flask import request
from flask import render_template
from werkzeug.utils import redirect
from .. import db
from ..forms import AnswerForm
from ..models import Question
from ..models import Answer


bp = Blueprint('answer', __name__, url_prefix='/answer')

@bp.route('/create/<int:qid>', methods=('POST',))
def create(qid):
    form = AnswerForm()
    q = Question.query.get_or_404(qid)
    if form.validate_on_submit():
        c = request.form['content']
        a = Answer(question=q, content=c, create_date=datetime.now())
        db.session.add(a)
        db.session.commit()
        return redirect(url_for('question.detail', qid=qid))
    return render_template('question/question_detail.html', q=q, form=form)