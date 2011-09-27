from breakfast.tests import *

class TestFrontendController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='frontend', action='index'))
        # Test response...
