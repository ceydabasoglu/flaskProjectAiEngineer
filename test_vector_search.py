import unittest
from app import app
from PyPDF2 import PdfReader


class TestAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = app.test_client()
        cls.app.testing = True

    def read_qa_pairs_from_pdf(self, file_path):
        qa_pairs = []
        with open(file_path, "rb") as file:
            pdf_reader = PdfReader(file)
            num_pages = len(pdf_reader.pages)
            for page_num in range(num_pages):
                page = pdf_reader.pages[page_num]
                text = page.extract_text()
                qa_pairs.extend([{"question": q.strip(), "answer": a.strip()} for q, a in
                                 zip(text.split("\n")[::2], text.split("\n")[1::2])])
        return qa_pairs

    def test_question_responses(self):
        qa_pairs = self.read_qa_pairs_from_pdf("QA_testing.pdf")
        for qa_pair in qa_pairs:
            question = qa_pair["question"]
            response = self.app.post('/vector-search', json={"message": question})
            result = response.json["similar_vectors"] if response.status_code == 200 else None
            self.assertEqual(result, qa_pair["answer"])


if __name__ == '__main__':
    unittest.main()
