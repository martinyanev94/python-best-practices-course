class ReportGenerator:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def generate_report(self):
        print(f"Report: {self.title}")
        print(self.content)

    def save_report(self, filename):
        with open(filename, 'w') as file:
            file.write(f"{self.title}\n{self.content}")
class Report:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def display(self):
        print(f"Report: {self.title}")
        print(self.content)

class ReportSaver:
    def __init__(self, report):
        self.report = report

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            file.write(f"{self.report.title}\n{self.report.content}")

    def save_to_pdf(self, filename):
        # Imagine this function saves the report in PDF format
        print(f"Saving {self.report.title} as a PDF.")
