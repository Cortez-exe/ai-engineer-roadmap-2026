def text_formatter(text):
    cleaned = clean_text(text)
    count = word_count(cleaned)

    return {  
        "text": cleaned,
        "count": count
    }

def clean_text(text):
    clean = text.strip().lower()
    return clean

def word_count(text):
    counter = len(text.split())
    return counter

    