with open(r"research\rud_test_case\jsons\report_scope.json", encoding='utf-8')as f:
    import json
    data = json.load(f)

all_keys = [key for key in list(data.keys())]

cleaned_dict = dict()

for item in [{i: data[i]} for i in all_keys]:
    for key, value in item.items():
        for v in list(value.keys()):
            if v != "By Region":
                first_half = ", ".join(value[v][:-1]).strip()
                second_half = value[v][-1].replace(" and", ",")

                new_str = first_half + ", " + second_half
                new_value = new_str.split(", ")
                if "" in new_value:
                    new_value.remove("")
                value[v] = new_value
        cleaned_dict[key] = value

with open(r"research\rud_test_case\jsons\cleaned_report_scope.json", "w", encoding='utf-8') as f:
    json.dump(cleaned_dict, f, ensure_ascii=False)
