
# pyrefly: ignore [missing-import]
from langchain_community.document_loaders import TextLoader
# pyrefly: ignore [missing-import]
from langchain_core.documents import Document

from backend.vector_store import create_vector_database

from utils.config import DATA_PATH



def load_sections(file_path):
    """
    Split the dataset by '====' separators so each chunk
    stays within ONE service section and always includes
    the service name. This prevents cross-service confusion.
    """
    with open(file_path, encoding="utf-8") as f:
        raw_text = f.read()

    # Split on the section divider
    sections = raw_text.split("=" * 50)

    docs = []
    for section in sections:
        section = section.strip()
        if not section:
            continue

        # Only keep sections that describe a service
        if "Service:" in section:
            docs.append(Document(page_content=section))

    return docs



def get_retriever():

    documents = load_sections(DATA_PATH)

    vector_db = create_vector_database(documents)

    retriever = vector_db.as_retriever(
        search_kwargs={
            "k": 3   # 3 full service sections is plenty now
        }
    )

    return retriever