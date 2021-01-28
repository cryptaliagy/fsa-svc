from typing import (
    List,
    Dict,
)


def csv_string_to_dicts(
    string: str
) -> List[Dict[str, str]]:
    '''
    Converts csv string separated by spaces to a
    list of dictionaries of trigger, source, target
    '''
    items = string.split()
    output = []
    for item in items:
        trigger, source, target = item.split(',')
        output.append({
            'trigger': trigger,
            'source': source,
            'target': target
        })

    return output
