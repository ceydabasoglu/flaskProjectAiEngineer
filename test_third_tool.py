
import unittest
from third_tool import load_chunk_persist_pdf, get_llm_response

class TestThirdTool(unittest.TestCase):
    def test_load_chunk_persist_pdf(self):
        vectordb = load_chunk_persist_pdf()
        self.assertIsNotNone(vectordb)
    def test_get_llm_response(self):
        query = "Which language and framework was this API developed using?"
        response = get_llm_response(query)
        self.assertIsNotNone(response)


if __name__ == '__main__':
    unittest.main()
