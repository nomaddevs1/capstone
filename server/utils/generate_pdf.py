import logging
import pdfkit

from .render_template import render_template


def render_html(data: dict) -> str:
    logging.info("rendering html document to convert to pdf file...")
    html_str = render_template("transcript.html", **data)

    return html_str


def generate_pdf(html_data: str):
    logging.info("generating pdf file...")
    return pdfkit.from_string(
        html_data,
        False,
        options={
            "margin-top": "1in",
            "margin-bottom": "1in",
            "margin-left": "1in",
            "margin-right": "1in",
            "enable-javascript": True,
            "javascript-delay": 1000,  # may need to adjust the delay
            "no-stop-slow-scripts": True,
            "encoding": "UTF-8",
        },
    )
