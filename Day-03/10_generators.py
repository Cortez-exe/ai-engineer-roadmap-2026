def count_up_to(number):
    for i in range(1, number + 1):
        yield i


for count in count_up_to(5):
    print(f"Launching in {count}")



def process_documents(documents):
    for document in documents:
        yield f"Processing: {document}"

documents = [
    "resume.pdf",
    "invoice.pdf",
    "thesis.pdf",
    "dataset.csv"
]

for result in process_documents(documents):
    print(result)




# ============================================================
# REVIEWER — DAY 3: GENERATORS
# ============================================================
#
# KEY CONCEPTS:
# - `yield` creates a generator.
# - `yield` produces one value and pauses the function.
# - The function continues from where it paused when the next
#   value is requested.
# - `return` ends a function and returns its result.
# - Generators are useful for processing large amounts of data
#   without keeping the entire result in memory.
#
# KEY SYNTAX:
#
# def count_up_to(number):
#     for i in range(1, number + 1):
#         yield i
#
# for number in count_up_to(5):
#     print(number)
#
# COMMON MISTAKES:
# - Writing `yield[i]` instead of `yield i`
# - Forgetting that `range(number)` starts at 0
# - Writing `for x in count_up_to` instead of
#   `for x in count_up_to(5)`
# - Assuming calling a generator function immediately produces
#   all of its values
#
# AI ENGINEERING RELEVANCE:
# Generators are useful when processing large datasets, files,
# database records, document pipelines, and other data streams
# where loading everything into memory at once is inefficient.
#
# ============================================================