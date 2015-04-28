# coding=utf-8
from core.classifier.FileClassifier import FileClassifier
from  core.validator.FileValidators import FileValidators
import shutil

class ViewFileClassifier(FileClassifier):

    def __init__(self):
        FileClassifier.__init__(self)
        self.next = FileClassifier()

    def setNext(self,next):
        self.next = next


    def classifier(self,type,file):
        module = self._extractor.getModule(file)
        path = self._router.getPath("index",module)
        shutil.copy2(file, path)

        if type == FileValidators.VIEW_BI.value :
            path = self._router.getPath("bi",module)
            shutil.copy2(file, path)
        elif type == FileValidators.VIEW_DATA.value :
            path = self._router.getPath("datos",module)
            shutil.copy2(file, path)
        elif type == FileValidators.VIEW_JOIN.value :
            path = self._router.getPath("join",module)
            shutil.copy2(file, path)
        elif type == FileValidators.VIEW_LOV.value :
            path = self._router.getPath("lov",module)
            shutil.copy2(file, path)
        elif type == FileValidators.VIEW_REPORT.value :
            path = self._router.getPath("report",module)
            shutil.copy2(file, path)
        else :
            self.next.classifier(type,file)
