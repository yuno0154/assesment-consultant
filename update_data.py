import json

# 1. Update groups_result.json
with open('groups_result.json', 'r', encoding='utf-8') as f:
    groups = json.load(f)

for g in groups:
    if g['group_num'] == 8:
        # Find Choi Yeon-ho and remove
        g['members'] = [m for m in g['members'] if m['name'] != '최연호']
        # Add Park Yang-hui as leader
        new_member = {
            "num": 159,
            "school": "선주고등학교",
            "school_type": "수석교사",
            "name": "박양희",
            "subject": "생명과학",
            "phone": "",
            "group": "1",
            "remarks": "수석교사",
            "is_high": True,
            "is_middle": False,
            "is_leader": True
        }
        g['members'].insert(0, new_member)

with open('groups_result.json', 'w', encoding='utf-8') as f:
    json.dump(groups, f, ensure_ascii=False, indent=2)

# 2. Update groups_new.json (if exists)
try:
    with open('groups_new.json', 'r', encoding='utf-8') as f:
        groups_new = json.load(f)
    for g in groups_new:
        if g['group_num'] == 8:
            g['members'] = [m for m in g['members'] if m['name'] != '최연호']
            new_member = {
                "name": "박양희",
                "school": "선주고등학교",
                "school_type": "수석교사",
                "subject": "생명과학",
                "is_leader": True,
                "remarks": "수석교사",
                "main_grp": 1
            }
            g['members'].insert(0, new_member)
    with open('groups_new.json', 'w', encoding='utf-8') as f:
        json.dump(groups_new, f, ensure_ascii=False, indent=2)
except FileNotFoundError:
    pass

# 3. Update all_data_js.txt
with open('all_data_js.txt', 'r', encoding='utf-8') as f:
    all_data = json.load(f)

# Remove Choi Yeon-ho
all_data = [d for d in all_data if d['name'] != '최연호']
# Add Park Yang-hui
new_person = {
    "id": 159,
    "name": "박양희",
    "org": "선주고등학교",
    "pos": "수석교사",
    "subject": "생명과학",
    "class": 1,
    "is_leader": True,
    "remarks": "수석교사"
}
all_data.append(new_person)

with open('all_data_js.txt', 'w', encoding='utf-8') as f:
    json.dump(all_data, f, ensure_ascii=False, separators=(',', ':'))

# 4. Update groups_js2.txt (it contains the minified JS string)
groups_js = json.dumps(groups, ensure_ascii=False, separators=(',', ':'))
with open('groups_js2.txt', 'w', encoding='utf-8') as f:
    f.write(groups_js)

print("Update completed successfully.")
