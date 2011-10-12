import formencode

class QuestionForm(formencode.Schema):
    allow_extra_fields = True
    filter_extra_fields = True
    # TODO Add a puppet validator in here to validate the script's syntax.
    question = formencode.validators.UnicodeString(not_empty=True)

