import json
import sys

version_json = '''
{
 "dirty": false,
 "error": null,
 "full-revisionid": "unknown",
 "version": "VERSION"
}
'''  # END VERSION_JSON


def get_versions():
    return json.loads(version_json)
