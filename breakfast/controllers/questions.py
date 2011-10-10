import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from breakfast.lib.base import BaseController, render, Session
from breakfast.model import Question

log = logging.getLogger(__name__)

class QuestionsController(BaseController):

    def __before__(self):
        self.question_q = Session.query(Question)

    def index(self):
        c.questions = self.question_q.all()
        return render('/questions/index.genshi')

    def show(self, id):
        question = self.question_q.filter_by(id = id).first()
        if question:
            c.question = question
            return render('/questions/show.genshi')
        abort(404)

    def create(self):
        question = Question()
        Session.add(question)
        Session.commit()
        redirect_to('show_page', id = question.id)

    def save(self, id):
        question = self.question_q.filter_by(id = id).first()
        question.question = escape(request.POST.getone("question"))
        Session.commit()
        redirect_to('show_page', id = question.id)

    def delete(self, id):
        question = self.question_q.filter_by(id = id).first()
        Session.delete(question)
        Session.commit()
        redirect_to('questions')

