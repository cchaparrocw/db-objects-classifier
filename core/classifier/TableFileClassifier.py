# coding=utf-8
from core.classifier.FileClassifier import FileClassifier
from  core.validator.FileValidators import FileValidators
import shutil

class TableFileClassifier(FileClassifier):

    def __init__(self):
        FileClassifier.__init__(self)
        self.next = FileClassifier()

    def setNext(self,next):
        self.next = next

    def classifier(self,type,file):
        if type == FileValidators.TABLE.value :
            module = self._extractor.getModule(file)
            path = self._router.getPath("table",module)
            shutil.copy2(file, path)
        else:
            self.next.classifier(type,file)
