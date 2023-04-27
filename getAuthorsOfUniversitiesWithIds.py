import json
import sys
from scholarly import scholarly

with open("universities.json", "r", encoding="utf-8") as f:
    data = json.load(f)

data = [uni for uni in data if uni['id']]

START = 50      # Dahil
END = 70        # Haric

uniCount = 1
for uni in data[START:END]:
    name = uni['name']
    id = uni['id']
    print(f'\n{name} ({uniCount}/{END-START})')

    count = 1
    page = 1
    print('page: ', end='')
    sys.stdout.flush()

    results = []
    query = scholarly.search_author_by_organization(id)

    for result in query:
        results.append(result)
        count += 1

        if (count // 10) + 1 > page:
            print('X', end='')
            sys.stdout.flush()

        page = (count // 10) + 1

    print(f'\nfound {count} authors')
    uniCount += 1

    with open(f'./scholar/{name}.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=4)
