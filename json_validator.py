import json
import jsonschema
import os


def log_message(event_filename, message):
    message = [
        "event: {}".format(event_filename),
        "{}".format(message)
    ]
    return "\n".join(message) + "\n"


print("Starting validation...")
errors = []
logs = []

events_paths = os.listdir("event")

events = []
for event_path in events_paths:
    with open("event/" + event_path, 'r') as file:
        try:
            events.append(json.load(file))
        except json.decoder.JSONDecodeError as error:
            logs.append(log_message(event_path, error))

for event in events:
    error_message = ''
    event_path = events_paths[events.index(event)]
    try:
        schema_path = event['event'] + ".schema"
        with open("schema/{}".format(schema_path), 'r') as file:
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
        error_message = "{}. Add this field".format(error.message)
    except jsonschema.exceptions.SchemaError as error:
        error_message = error.message
    finally:
        if error_message:
            logs.append(log_message(event_path, error_message))

with open('log.txt', 'w') as file:
    file.write("\n\n".join(logs))

print("Valid is complete.")
