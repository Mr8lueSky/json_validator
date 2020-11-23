import json
import jsonschema
import os


EVENT_FOLDER = 'event'
SCHEMA_FOLDER = 'schema'


def log_message(event_filename, message, path=''):
    message = [
        "event: {}".format(event_filename),
        "error path: {}".format(path),
        "{}".format(message)
    ]
    return "\n".join(message)


print("Starting validation...")
errors = []
logs = []

events_paths = os.listdir("event")

events = []

for event_path in events_paths:
    error_message = ''
    error_path = ''
    with open("{}/{}".format(EVENT_FOLDER, event_path), 'r') as file:
        try:
            event = json.load(file)
        except json.decoder.JSONDecodeError as error:
            logs.append(log_message(event_path, error))
            continue
    try:
        schema_path = event['event'] + ".schema"
        with open("{}/{}".format(SCHEMA_FOLDER, schema_path), 'r') as file:
            schema = json.load(file)
        jsonschema.validate(event, schema)
    except TypeError as error:
        error_message = "'event' field is not a string. Edit this field"
    except KeyError as error:
        error_message = "There is no 'event' field. Add this field"
    except FileNotFoundError as error:
        error_message = "There is no such schema to validate this event. " \
                        + "Change 'event' field to schema that exist or create new schema"
    except jsonschema.exceptions.ValidationError as error:
        error_path = "/".join(error.absolute_schema_path)
        error_message = error
    except jsonschema.exceptions.SchemaError as error:
        error_message = error
    finally:
        if error_message:
            logs.append(log_message(event_path, error_message, error_path))

with open('log.txt', 'w') as file:
    file.write("\n\n\n".join(logs))

print("Valid is complete.")
