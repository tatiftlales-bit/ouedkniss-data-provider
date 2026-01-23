import json

# معلومات تجريبية سيتم استبدالها لاحقاً بسحب حقيقي من واد كنيس
data = {
    "status": "success",
    "last_update": "2026-01-23",
    "cars": [
        {"model": "Symbol", "price": "2200000"},
        {"model": "Golf 7", "price": "4500000"}
    ]
}

# حفظ البيانات في ملف JSON
with open('market_data.json', 'w') as f:
    json.dump(data, f, indent=4)

print("تم إنشاء ملف البيانات بنجاح!")
