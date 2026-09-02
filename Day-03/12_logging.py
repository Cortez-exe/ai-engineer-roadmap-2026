import logging

logging.basicConfig(level=logging.INFO)
 
def process_documents(documents):
    for document in documents:
        if document == "":
            logging.warning("Received an empty document!\n")
        else:
            logging.info(f"Processing document: {document}")
            yield f"Processed: {document}\n"

result = [
    "resume.pdf",
    "",
    "background.pdf",
    "certificates.pdf" 
    ]

for processed in process_documents(result):
    print(processed)


# ============================================================
# REVIEWER — DAY 3: LOGGING
# ============================================================
#
# KEY CONCEPTS:
# - Logging records events happening inside an application.
# - Logging is more useful for applications than relying only
#   on print().
#
# LOGGING LEVELS:
#
# DEBUG
#     Detailed information useful during development.
#
# INFO
#     Normal application activity.
#
# WARNING
#     Something unexpected happened, but the application can
#     continue.
#
# ERROR
#     Something failed.
#
# CRITICAL
#     A serious failure occurred.
#
# KEY SYNTAX:
#
# import logging
#
# logging.basicConfig(level=logging.INFO)
#
# logging.debug("Debug information")
# logging.info("Application started")
# logging.warning("Unexpected situation")
# logging.error("Something failed")
# logging.critical("Critical failure")
#
# IMPORTANT:
# logging.info() and similar logging functions normally return
# None. They are for recording events, not producing values.
#
# AI ENGINEERING RELEVANCE:
# Logging is essential for debugging AI APIs, RAG pipelines,
# automation workflows, model inference, document processing,
# and production services.
# ============================================================