from PIL import Image

import pyocr
import pyocr.builders

tools = pyocr.get_available_tools()
if len(tools) == 0:
    sys.exit(1)
tool = tools[0]

langs = tool.get_available_languages()
lang = langs[0]

img_txt = tool.image_to_string(
    Image.open('test.png'),
    lang=lang,
    builder=pyocr.builders.TextBuilder()
)
