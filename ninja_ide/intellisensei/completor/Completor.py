from PyQt5.QtWidgets import QListWidget
from PyQt5.QtCore import pyqtSignal


class CompletorNinjaApi(QListWidget):
    
    
    def __init__(self, parent=None):
        # QListWidget.__init__(parent)
        super(CompletorNinjaApi, self).__init__(parent)
        self.___text_script_complete = ''
        self.___line_editor = 0
        self.___column_editor = 0
        self.___list_pred_position = None
        self.___language = None
        self.hide()

    @property
    def text_script_complete(self):
        return self.___text_script_complete

    @text_script_complete.setter
    def text_script_complete(self, script):
        self.___text_script_complete = script

    @property
    def line_editor(self):
        return self.___line_editor

    @line_editor.setter
    def line_editor(self, line):
        self.___line_editor = line

    @property
    def column_editor(self):
        return self.___column_editor

    @column_editor.setter
    def column_editor(self, column):
        self.___column_editor = column

    @property
    def language(self):
        return self.___language

    @language.setter
    def language(self, lang):
        self.___language = lang

    @property
    def list_pred_position(self):
        return self.___list_pred_position

    @list_pred_position.setter
    def list_pred_position(self, qpoint):
        self.___list_pred_position = qpoint

    def __fill_list(self, list_predictions):
        self.clear()
        self.addItems(list_predictions)

    def put_predictions(self, list_pred=None):
        if not isinstance(list_pred, list):
            raise('list_pred shall be a list class')
        if len(list_pred) == 0:
            raise('list_pred shall be have some element')

        self.__fill_list(list_pred)

    def show_list_predictions(self):
        if self.___list_pred_position is None:
            raise Exception('Error with the text position cursor')
        self.hide()
        self.move(self.___list_pred_position)
        self.show()

    def hide_list_predictions(self):
        self.hide()

    def clear_list_predictiones(self):
        self.clear()
