import re
from langchain.text_splitter import MarkdownTextSplitter
from langchain.docstore.document import Document


# Data Cleaning functions

def merge_hyphenated_words(text):
    return re.sub(r"(\w)-\n(\w)", r"\1\2", text)


def fix_newlines(text):
    return re.sub(r"(?<!\n)\n(?!\n)", " ", text)


def remove_multiple_newlines(text):
    return re.sub(r"\n{2,}", "\n", text)


def clean_text(text):
    """
    Cleans the text by passing it through a list of cleaning functions.

    Args:
        text (str): Text to be cleaned

    Returns:
        str: Cleaned text
    """
    cleaning_functions = [merge_hyphenated_words, fix_newlines, remove_multiple_newlines]
    for cleaning_function in cleaning_functions:
        text = cleaning_function(text)
    return text


def text_to_docs(text, metadata):
    """
    Converts input text to a list of Documents with metadata.

    Args:
        text (str): A string of text.
        metadata (dict): A dictionary containing the metadata.

    Returns:
        List[Document]: List of documents.
    """
    doc_chunks = []
    text_splitter = MarkdownTextSplitter(chunk_size=2048, chunk_overlap=128)
    chunks = text_splitter.split_text(text)
    for i, chunk in enumerate(chunks):
        doc = Document(page_content=chunk, metadata=metadata)
        doc_chunks.append(doc)
    return doc_chunks


def get_doc_chunks(text, metadata):
    """
    Processes the input text and metadata to generate document chunks.

    This function takes the raw text content and associated metadata, cleans the text,
    and divides it into document chunks.

    Args:
        text (str): The raw text content to be processed.
        metadata (dict): Metadata associated with the text content.

    Returns:
        List[Document]: List of documents.
    """
    text = clean_text(text)
    doc_chunks = text_to_docs(text, metadata)
    return doc_chunks
