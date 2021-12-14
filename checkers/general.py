import jsonschema

from schemas.general import schemas


class Checker:

    @staticmethod
    def validate_json(json, schema):
        schema = schemas[schema]
        jsonschema.validate(json, schema)
