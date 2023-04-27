with open("universities.json", "r", encoding="utf-8") as f:
    data = json.load(f)


for index, uni in enumerate(data):

    if uni['id']:
        continue

    name = uni['name']
    print(f'\n{name}')

    query = scholarly.search_org(name)
    uni['ids'] = query

    with open('universities2.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
