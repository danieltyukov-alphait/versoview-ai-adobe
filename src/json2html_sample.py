import os
import os.path
import json
from json2html import *

base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(base_path + "\\versoview-ai-adobe\\output\\structuredData.json", "r") as f:
    data = json.load(f)
    html = json2html.convert(json=data)
    with open(base_path + "\\versoview-ai-adobe\\output\\ExtractTextInfoFromPDF.html", "w") as f:
        f.write(html)