from scholarly import scholarly, ProxyGenerator
import json
import sys
from collections import Counter


with open("universityNames.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for index, uni in enumerate(data[100:]):
    ids = []
    emails = []
    name = uni['name']
    count = 0
    print(f'\n{name}({index})')
    query = scholarly.search_author(name)

    for result in query:
        if count >= 10:
            break
        emails.append(result.get('email_domain', None))
        basics = scholarly.fill(result, sections=["basics"])
        ids.append(basics.get('organization', None))
        count += 1
        print(count)

    uni['emails'] = Counter(emails)
    uni['ids'] = Counter(ids)

    print('emails', uni['emails'])
    print('ids', uni['ids'])

    with open('universityNames.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
