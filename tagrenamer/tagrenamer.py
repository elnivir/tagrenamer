import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QCheckBox,
                             QLineEdit, QPushButton, QListWidget, QApplication, QTextEdit,
                             QFileDialog)

class Gui(QWidget):
    """Klasa zawierająca GUI projektu"""

    def __init__(self):

        super().__init__()

        '''self.AudFormat = None
        self.ChangeFileName = False
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
        self.FlacChoiceRdBtn = QRadioButton('Flac')
        self.ChangeFileNameChkBx = QCheckBox('Change files names?')
        self.AddNumerationChkBx = QCheckBox('Add track numbers?')

        self.SelectDirBtn = QPushButton('Select Dir')
        self.SelectDirBtn.clicked.connect(self.selectDir)
        self.DirPathLnEd = QLineEdit()
        self.DirPathLnEd.setReadOnly(True)

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

        self.TrackTitleLbl = QLabel('Track title')
        self.TrackTitleTxtEdt = QTextEdit()
        self.TrackLstLbl = QLabel('Track list')
        self.TrackTitleLstBx = QListWidget()

        self.WorkBtn = QPushButton('Do your job')
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

        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('Tag renamer')
        self.show()


    def selectDir(self):

        dialog = QFileDialog()
        folder_path = dialog.getExistingDirectory(None, "Select directory")
        self.DirPathLnEd.setText(folder_path)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Gui()
    sys.exit(app.exec_())
