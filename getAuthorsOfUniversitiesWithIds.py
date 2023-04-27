import json
from scholarly import scholarly

with open("universities.json", "r", encoding="utf-8") as f:
    data = json.load(f)

data = [uni for uni in data if uni['id']]

START = 50  # Dahil
END = 75  # Haric

uniCount = 1
for uni in data[START:END]:
    name = uni['name']
    id = uni['id']
    print(f'\n{name} ({uniCount}/{END-START})')

    count = 1
    results = []
    query = scholarly.search_author_by_organization(id)
    for result in query:
        results.append(result)
        count += 1

    print(f'found {count} authors')
    uniCount += 1

    with open(f'./scholar/{name}.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=4)
