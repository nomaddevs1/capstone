import re

from pdf_generator import render_html, generate_pdf
from common_fixtures import mock_client, transcript_dict


def test_render_html(transcript_dict):
    transcript_data = {
        "settings": {
            # add settings here like color, font size, font type, bg color, etc.
        },
        "transcript": transcript_dict,
    }

    expected_html = """\
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    body {
      margin: 20px;
    }
  </style>
</head>
<body>
  <p><strong>2:7</strong> - Good morning, everyone.</p>
  <p><strong>10:16</strong> - Today, we'll discuss the new project.</p>
  <p><strong>20:26</strong> - First, let's go through the objectives.</p>
</body>
</html>\
"""
    result = render_html(transcript_data)

    assert expected_html == result

    transcript_data = {
        "settings": {
            "bg_color": "#ddffff",
            "font_size": "20px",
            "font_color": "black",
            "font": "Arial",
        },
        "transcript": [],
    }

    result = render_html(transcript_data)
    expect_styles = [
        re.compile(r"background-color:\s*#ddffff"),
        re.compile(r"font-size:\s*20px"),
        re.compile(r"color:\s*black"),
        re.compile(r"font-family:\s*Arial"),
    ]

    for style in expect_styles:
        assert style.search(result) != None


def test_render_html_missing_data():
    transcript_data = {
        "settings": {
            # add settings here like color, font size, font type, bg color, etc.
        },
        "transcript": [],
    }
    expected_html = """\
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    body {
      margin: 20px;
    }
  </style>
</head>
<body>
</body>
</html>\
"""
    result = render_html(transcript_data)

    assert expected_html == result


def test_generate_pdf():
    html_data = """\
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    body {
      margin: 20px;
    }
  </style>
</head>
<body>
</body>
</html>\
"""

    pdf_data = generate_pdf(html_data)

    assert len(pdf_data) > 0


def test_generate_pdf_route_valid_data(mock_client, transcript_dict):
    mock_html_text = "<h1>Title</h2>"

    response = mock_client.post("/generate-pdf/", json={"raw_html": mock_html_text})

    assert response.status_code == 200
    assert response.text

    response = mock_client.post("/generate-pdf/", json={"transcript": transcript_dict})

    assert response.status_code == 200
    assert response.text


def test_generate_pdf_route_invalid_data(mock_client, transcript_dict):
    mock_html_text = "<h1>Title</h2>"
    response = mock_client.post(
        "/generate-pdf/",
        json={"raw_html": mock_html_text, "transcript": transcript_dict},
    )

    assert response.status_code == 400
    assert response.text

    response = mock_client.post("/generate-pdf/", json={})

    assert response.status_code == 400
    assert response.text
