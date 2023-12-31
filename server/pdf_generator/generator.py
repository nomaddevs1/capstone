from jinja2 import Environment, PackageLoader, select_autoescape
from typing import List
import pdfkit

env = Environment(loader=PackageLoader("pdf_generator"), autoescape=select_autoescape())


def render_html(data: dict) -> str:
    template = env.get_template("transcript.html")
    html_str = template.render(**data)

    return html_str


def generate_pdf(html_data: str):
    return pdfkit.from_string(
        html_data,
        False,
        options={
            "margin-top": "0in",
            "margin-bottom": "0in",
            "margin-left": "0in",
            "margin-right": "0in",
        },
    )
