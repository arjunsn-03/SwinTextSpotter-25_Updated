import json

N = 80  # how many images you want to keep

in_path = "datasets/totaltext/totaltext_test_full.json"
out_path = "datasets/totaltext/totaltext_test.json"

with open(in_path, "r") as f:
    data = json.load(f)

images = data["images"][:N]
keep_ids = {img["id"] for img in images}

annotations = [
    ann for ann in data["annotations"]
    if ann["image_id"] in keep_ids
]

subset = {
    "images": images,
    "annotations": annotations,
    "categories": data.get("categories", []),
}

with open(out_path, "w") as f:
    json.dump(subset, f)

print(f"Saved subset with {len(images)} images and {len(annotations)} annotations to {out_path}")
