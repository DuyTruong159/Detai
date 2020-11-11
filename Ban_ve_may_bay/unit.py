import json

def read_data(path= 'data/chuyen_bay.json'):
    with open(path, encoding='utf-8') as f:
        return json.load(f)

def get_chuyenbay_by_stt(stt):
    chuyen_bay = read_data()
    for cb in chuyen_bay:
        if cb['stt'] == stt:
            return cb