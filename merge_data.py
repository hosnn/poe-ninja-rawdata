import json
import os

def load_json_file(file_path):
    """JSON 파일을 로드하는 함수"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except json.JSONDecodeError:
        print(f"Invalid JSON in file: {file_path}")
        return None

def save_json_file(data, file_path):
    """JSON 파일을 저장하는 함수"""
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"File saved: {file_path}")
    except Exception as e:
        print(f"Error saving file: {e}")

def merge_data(api_data_path, translation_path, output_path):
    """API 데이터와 번역 데이터를 병합하는 함수"""
    # API 데이터 로드
    api_data = load_json_file(api_data_path)
    if api_data is None:
        return

    # 번역 데이터 로드
    translation_data = load_json_file(translation_path)
    if translation_data is None:
        return

    translations = translation_data['translations']

    # API 데이터의 각 아이템에 번역 데이터 추가
    for item in api_data.get('lines', []):
        name = item.get('name')
        if name in translations:
            item.update(translations[name])
        else:
            item.update({
                'name_ko': '',
                'regex': ''
            })

    # 병합된 데이터 저장
    save_json_file(api_data, output_path)