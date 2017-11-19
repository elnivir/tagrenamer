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

        self.OrigArtistChkBx = QCheckBox('Original artist')
        self.OrigArtistChkBx.clicked.connect(lambda: self.OrigArtistLnEd.setEnabled(self.OrigArtistChkBx.isChecked()))
        self.OrigArtistLnEd = QLineEdit()
        self.OrigArtistLnEd.setEnabled(False)
        self.PerfArtistChkBx = QCheckBox('Performing artist')
        self.PerfArtistChkBx.clicked.connect(lambda: self.PerfArtistLnEd.setEnabled(self.PerfArtistChkBx.isChecked()))
        self.PerfArtistLnEd = QLineEdit()
        self.PerfArtistLnEd.setEnabled(False)
        self.AlbumTitleChkBx = QCheckBox('Album title')
        self.AlbumTitleChkBx.clicked.connect(lambda: self.AlbumTitleLnEd.setEnabled(self.AlbumTitleChkBx.isChecked()))
        self.AlbumTitleLnEd = QLineEdit()
        self.AlbumTitleLnEd.setEnabled(False)
        self.YearChkBx = QCheckBox('Year')
        self.YearChkBx.clicked.connect(lambda: self.YearLnEd.setEnabled(self.YearChkBx.isChecked()))
        self.YearLnEd = QLineEdit()
        self.YearLnEd.setEnabled(False)
        self.GenreChkBx = QCheckBox('Genre')
        self.GenreChkBx.clicked.connect(lambda: self.GenreLnEd.setEnabled(self.GenreChkBx.isChecked()))
        self.GenreLnEd = QLineEdit()
        self.GenreLnEd.setEnabled(False)

        self.TrackTitleChkBx = QCheckBox('Track titles')
        self.TrackTitleChkBx.clicked.connect(lambda: self.TrackTitleTxtEdt.setEnabled(self.TrackTitleChkBx.isChecked()))
        self.TrackTitleTxtEdt = QTextEdit()
        self.TrackTitleTxtEdt.setEnabled(False)
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

        self.MiscDataVBox.addWidget(self.OrigArtistChkBx)
        self.MiscDataVBox.addWidget(self.OrigArtistLnEd)
        self.MiscDataVBox.addWidget(self.PerfArtistChkBx)
        self.MiscDataVBox.addWidget(self.PerfArtistLnEd)
        self.MiscDataVBox.addWidget(self.AlbumTitleChkBx)
        self.MiscDataVBox.addWidget(self.AlbumTitleLnEd)
        self.MiscDataVBox.addWidget(self.YearChkBx)
        self.MiscDataVBox.addWidget(self.YearLnEd)
        self.MiscDataVBox.addWidget(self.GenreChkBx)
        self.MiscDataVBox.addWidget(self.GenreLnEd)

        self.TitleVBox.addWidget(self.TrackTitleChkBx)
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
        
        if (nbr_titles == nbr_files) or TrackTitleChkBx.isEnabled():

            for i in range(self.TrackTitleLstBx.count()):
                TrkTtl = self.TrackTitleLstBx.item(i).text()
                file = os.path.abspath(os.path.join(self.DirPathLnEd.text(), TrkTtl))
                print(file)

        else:
            self.ErrorDialog.exec()

    def changeMp3Tags(self):

        pass

    def changeFlacTags(self):

        pass

        
def main():

    app = QApplication(sys.argv)
    ex = Gui()
    sys.exit(app.exec_())

if __name__ == '__main__':

    main()