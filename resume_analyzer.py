import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton,
    QTextEdit, QFileDialog, QSplitter, QMessageBox
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from PyPDF2 import PdfReader

SOFT_SKILLS = [
    "communication", "teamwork", "leadership", "problem solving", "time management",
    "adaptability", "critical thinking", "creativity", "conflict resolution",
    "work ethic", "collaboration", "interpersonal skills", "decision making",
    "organization"
]

EDUCATION_TERMS = [
    "bachelor", "master", "phd", "degree", "diploma", "education", "university", "college"
]

LANGUAGES = [
    "english", "french", "spanish", "german", "chinese", "japanese", "korean",
    "arabic", "russian", "hindi", "portuguese", "italian"
]

class GeneralCVAnalyzer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("General CV Analyzer")
        self.setGeometry(200, 200, 1000, 700)

        layout = QVBoxLayout()

        header = QLabel("General CV Analyzer")
        header.setFont(QFont("Helvetica", 28, weight=QFont.Weight.Bold))
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        header.setStyleSheet("""
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                        stop:0 #4facfe, stop:1 #00f2fe);
            color: white;
            padding: 25px;
            border-radius: 15px;
        """)
        layout.addWidget(header)

        self.upload_btn = QPushButton("Upload CV (PDF or TXT)")
        self.upload_btn.setStyleSheet("""
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                            stop:0 #43e97b, stop:1 #38f9d7);
                color: black;
                padding: 16px;
                font-size: 20px;
                border-radius: 12px;
                font-weight: bold;
                margin-bottom: 15px;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                            stop:0 #38f9d7, stop:1 #43e97b);
            }
        """)
        self.upload_btn.clicked.connect(self.upload_cv)
        layout.addWidget(self.upload_btn)

        splitter = QSplitter(Qt.Orientation.Vertical)

        self.cv_text = QTextEdit()
        self.cv_text.setReadOnly(True)
        self.cv_text.setStyleSheet("""
            QTextEdit {
                background-color: #fefefe;
                color: black;
                border: 2px solid #cccccc;
                padding: 14px;
                font-size: 15px;
                font-family: Arial, sans-serif;
            }
        """)
        splitter.addWidget(self.cv_text)

        self.analysis_text = QTextEdit()
        self.analysis_text.setReadOnly(True)
        self.analysis_text.setStyleSheet("""
            QTextEdit {
                background-color: #ffffff;
                color: black;
                border: 3px solid #4facfe;
                padding: 14px;
                font-size: 15px;
                font-family: Arial, sans-serif;
            }
        """)
        splitter.addWidget(self.analysis_text)

        splitter.setSizes([450, 250])
        layout.addWidget(splitter)

        self.setLayout(layout)
        self.setStyleSheet("background-color: #e0eafc;")

    def upload_cv(self):
        path, _ = QFileDialog.getOpenFileName(self, "Select CV file", "", "PDF Files (*.pdf);;Text Files (*.txt)")
        if not path:
            return

        text = self.extract_text(path)
        if text.startswith("Error reading"):
            QMessageBox.warning(self, "Error", text)
            return

        self.cv_text.setPlainText(text)
        score, report = self.analyze_text(text)
        self.analysis_text.setPlainText(f"Score: {score}/100\n\n{report}")

    def extract_text(self, path):
        if path.lower().endswith(".pdf"):
            try:
                reader = PdfReader(path)
                text = ""
                for page in reader.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
                return text
            except Exception as e:
                return f"Error reading PDF: {e}"
        else:
            try:
                with open(path, "r", encoding="utf-8") as f:
                    return f.read()
            except Exception as e:
                return f"Error reading text file: {e}"

    def analyze_text(self, text):
        text_lower = text.lower()

        found_soft = [kw for kw in SOFT_SKILLS if kw in text_lower]
        found_edu = [kw for kw in EDUCATION_TERMS if kw in text_lower]
        found_lang = [kw for kw in LANGUAGES if kw in text_lower]

        score = 0
        reasons = []

        if len(found_soft) >= 2:
            score += 40
            reasons.append(f"Soft skills found ({len(found_soft)}): {', '.join(found_soft)}")
        else:
            reasons.append(f"Few soft skills found ({len(found_soft)}): {', '.join(found_soft) if found_soft else 'None'}")

        if found_edu:
            score += 30
            reasons.append(f"Education background detected: {', '.join(found_edu)}")
        else:
            reasons.append("No clear education background detected")

        if len(found_lang) >= 2:
            score += 30
            reasons.append(f"Multiple languages detected ({len(found_lang)}): {', '.join(found_lang)}")
        elif len(found_lang) == 1:
            score += 15
            reasons.append(f"One language detected: {found_lang[0]}")
        else:
            reasons.append("No language skills detected")

        return score, "\n".join(reasons)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GeneralCVAnalyzer()
    window.show()
    sys.exit(app.exec())
