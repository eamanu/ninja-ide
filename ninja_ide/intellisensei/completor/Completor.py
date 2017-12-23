from PyQt.QtWidgets import QCompleter


class CompletorNinjaApi(QCompleter):
    def __init__(self, list_key=None, parent=None):
        if list_key is None:
            # TODO: raise a exception
            print('completar')

        QCompleter.__init__(self, list_key, parent)
