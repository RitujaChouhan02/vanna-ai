import requests
import html2text
from vanna_setup import vn
from vanna_schema import schema


def fetch_google_doc_text(doc_id):
    export_url = f"https://docs.google.com/document/d/{doc_id}/export?format=html"
    response = requests.get(export_url)
    html = response.text
    text_maker = html2text.HTML2Text()
    text_maker.ignore_links = True
    return text_maker.handle(html)

# Your Google Doc ID (grab from the link)
doc_id = "1Z2vseeWcZ24Ru9isd0zHwFWVQ5qg_fDZbevEl1SIrTI"
domain_knowledge = fetch_google_doc_text(doc_id)

# Train Vanna using this live content
vn.train([schema, domain_knowledge])
