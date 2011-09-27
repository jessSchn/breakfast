import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from breakfast.lib.base import BaseController, render

log = logging.getLogger(__name__)

class FrontendController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/frontend.mako')
        # or, return a string
        return 'Hello World'
