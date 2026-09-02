from dataclasses import dataclass
import logging

logging.basicConfig(level=logging.INFO)


class InvalidDocument(Exception):
    pass


@dataclass
class Document:
    title: str
    content: str
    pages: int


def validate_documents(document: Document) -> None:
    if document.title.strip() == "":
        raise InvalidDocument("Title of the document cannot be empty")

    if document.content.strip() == "":
        raise InvalidDocument("Content cannot be empty")

    if document.pages <= 0:
        raise InvalidDocument("Page number is invalid")


def process_document(documents: list[Document]):
    for document in documents:
        try:
            validate_documents(document)

            logging.info(f"Processing document: {document.title}")

            yield f"Processed: {document.title}"

        except InvalidDocument as error:
            logging.error(error)


def main():
    documents = [
        Document(
            "resume.pdf",
            "Andrei Cortez",
            5
        ),
        Document(
            "thesis.pdf",
            "Drownaid ng lahat",
            5
        ),
        Document(
            "certificates.pdf",
            "ai certssss",
            5
        ),
        Document(
            "damn.pdf",
            "",
            5
        ),
        Document(
            "",
            "Andrei Cortez",
            5
        ),
        Document(
            "random.pdf",
            "Andrei Cortez",
            0
        ),
    ]

    for results in process_document(documents):
        print(results)


if __name__ == "__main__":
    main()





#checklist
#create a custom invaliderror for documents
#create  a dataclass for document creation
#create a function that will validate the content of the documents like name and content
#create a function that will process the documents after validating them
#create the main function that will create the documents and print the results