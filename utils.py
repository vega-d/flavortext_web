from FlavorTexts import FlavorTexts
from flask import jsonify
from flask_restful import Resource


def generate_phrase(patreon=False, constructive=None, lowercase=False):
    generator = FlavorTexts(patreon=patreon)

    if constructive is None:
        constructive = bool(generator._random(1))

    generated_text = generator.generateText(constructive=constructive)

    if lowercase:
        generated_text = str(generated_text).lower()

    return "".join(generated_text)


class API_point(Resource):
    def get(self):
        ret = {"text": generate_phrase()}
        return jsonify(ret)
