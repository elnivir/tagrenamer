import sys
import os
from mutagen.mp3 import EasyMP3
from mutagen.flac import FLAC

from PyQt5.QtWidgets import (QWidget, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QCheckBox,
                             QLineEdit, QPushButton, QListWidget, QApplication, QTextEdit,
                             QFileDialog, QMessageBox, QAbstractItemView)

class Gui(QWidget):
    """Klasa zawierająca GUI projektu"""

    def __init__(self):

        super().__init__()

        self.AudFormat = '.mp3'
        '''self.ChangeFileName = False
        self.AddNumeration = False
        self.DirPath = None
        self.OrigArtist = None
        self.PerfArtist = None
        self.AlbumTitle = None
        self.Year = None
        self.Genre = None'''

        self.createUI()

    def createUI(self):

        self.MainVBox = QVBoxLayout()
        self.OptionsHBox = QHBoxLayout()
        self.DirHBox = QHBoxLayout()
        self.DataHBox = QHBoxLayout()
        self.MiscDataVBox = QVBoxLayout()
        self.TitleVBox = QVBoxLayout()
        self.FilesVBox = QVBoxLayout()
        self.ButtonsHBox = QHBoxLayout()

        self.DataHBox.addLayout(self.MiscDataVBox)
        self.DataHBox.addLayout(self.TitleVBox)
        self.DataHBox.addLayout(self.FilesVBox)

        self.MainVBox.addLayout(self.OptionsHBox)
        self.MainVBox.addLayout(self.DirHBox)
        self.MainVBox.addLayout(self.DataHBox)
        self.MainVBox.addLayout(self.ButtonsHBox)

        self.setLayout(self.MainVBox)

        self.Mp3ChoiceRdBtn = QRadioButton('Mp3')
        self.Mp3ChoiceRdBtn.clicked.connect(self.setMp3Format)
        self.Mp3ChoiceRdBtn.clicked.connect(self.readDir)
        self.FlacChoiceRdBtn = QRadioButton('Flac')
        self.FlacChoiceRdBtn.clicked.connect(self.setFlacFormat)
        self.FlacChoiceRdBtn.clicked.connect(self.readDir)
        self.ChangeFileNameChkBx = QCheckBox('Change filenames?')
        self.AddNumerationChkBx = QCheckBox('Add track numbers?')

        self.SelectDirBtn = QPushButton('Select Dir')
        self.SelectDirBtn.clicked.connect(self.selectDir)
        self.DirPathLnEd = QLineEdit()
        self.DirPathLnEd.setReadOnly(True)
        self.DirPathLnEd.textChanged.connect(self.readDir)

        self.OrigArtistLbl = QLabel('Original artist')
        self.OrigArtistLnEd = QLineEdit()
        self.PerfArtistLbl = QLabel('Performing artist')
        self.PerfArtistLnEd = QLineEdit()
        self.AlbumTitleLbl = QLabel('Album title')
        self.AlbumTitleLnEd = QLineEdit()
        self.YearLbl = QLabel('Year')
        self.YearLnEd = QLineEdit()
        self.GenreLbl = QLabel('Genre')
        self.GenreLnEd = QLineEdit()

        self.TrackTitleLbl = QLabel('Track titles')
        self.TrackTitleTxtEdt = QTextEdit()
        self.TrackTitleTxtEdt.setStyleSheet('font: 10.5pt;')
        self.TrackLstLbl = QLabel('Track list')
        self.TrackTitleLstBx = QListWidget()
        self.TrackTitleLstBx.setDragDropMode(QAbstractItemView.InternalMove)

        self.WorkBtn = QPushButton('Do your job')
        self.WorkBtn.clicked.connect(self.changeTags)
        self.ExitBtn = QPushButton('Exit')
        self.ExitBtn.clicked.connect(self.close)

        self.OptionsHBox.addWidget(self.Mp3ChoiceRdBtn)
        self.OptionsHBox.addWidget(self.FlacChoiceRdBtn)
        self.OptionsHBox.addWidget(self.ChangeFileNameChkBx)
        self.OptionsHBox.addWidget(self.AddNumerationChkBx)

        self.DirHBox.addWidget(self.SelectDirBtn)
        self.DirHBox.addWidget(self.DirPathLnEd)

        self.MiscDataVBox.addWidget(self.OrigArtistLbl)
        self.MiscDataVBox.addWidget(self.OrigArtistLnEd)
        self.MiscDataVBox.addWidget(self.PerfArtistLbl)
        self.MiscDataVBox.addWidget(self.PerfArtistLnEd)
        self.MiscDataVBox.addWidget(self.AlbumTitleLbl)
        self.MiscDataVBox.addWidget(self.AlbumTitleLnEd)
        self.MiscDataVBox.addWidget(self.YearLbl)
        self.MiscDataVBox.addWidget(self.YearLnEd)
        self.MiscDataVBox.addWidget(self.GenreLbl)
        self.MiscDataVBox.addWidget(self.GenreLnEd)

        self.TitleVBox.addWidget(self.TrackTitleLbl)
        self.TitleVBox.addWidget(self.TrackTitleTxtEdt)

        self.FilesVBox.addWidget(self.TrackLstLbl)
        self.FilesVBox.addWidget(self.TrackTitleLstBx)

        self.ButtonsHBox.addWidget(self.ExitBtn)
        self.ButtonsHBox.addWidget(self.WorkBtn)

        self.ErrorDialog = QMessageBox()
        self.ErrorDialog.setText('Number of titles must match number of files')

        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('Tag renamer')
        self.show()

    def selectDir(self):

        dialog = QFileDialog()
        folder_path = dialog.getExistingDirectory(None, "Select directory")
        self.DirPathLnEd.setText(folder_path)

    def readDir(self):

        self.TrackTitleLstBx.clear()
        if self.DirPathLnEd.text() == '':
            pass
        else:
            for file in os.listdir(self.DirPathLnEd.text()):
                if file.endswith(self.AudFormat):
                    self.TrackTitleLstBx.addItem(file)
        print(self.DirPathLnEd.text())
        print('==========================')

    def setMp3Format(self):

        self.AudFormat = '.mp3'
        print(self.AudFormat)

    def setFlacFormat(self):

        self.AudFormat = '.flac'
        print(self.AudFormat)

    def changeTags(self):

        tracks = self.TrackTitleTxtEdt.toPlainText()
        nbr_titles = (len(tracks.split('\n')))
        nbr_files = (self.TrackTitleLstBx.count())
        print(nbr_titles)
        print(nbr_files)
        
        with open(r'C:\Users\elnivir\Documents\Kod\tagrenamer\tagrenamer\test.txt', 'w') as tstplk:
            for i in range(self.TrackTitleLstBx.count()):
                abc = self.TrackTitleLstBx.item(i).text()
                print(abc)
                tstplk.write(abc)

        if nbr_titles == nbr_files:

            pass

        else:
            self.ErrorDialog.exec()

    def changeMp3Tags():

        pass

    def changeFlacTags():

        pass

def main():

    app = QApplication(sys.argv)
    ex = Gui()
    sys.exit(app.exec_())

if __name__ == '__main__':

    main()