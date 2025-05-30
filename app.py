from fetch_data import fetch_and_save_data
from merge_data import merge_data

def main():
  DOMAIN = {
    'currency': 'https://poe.ninja/api/data/currencyoverview',
    'item': 'https://poe.ninja/api/data/itemoverview',
  }

  LEAGUES = {
    'standard': 'Standard',
    'settler': 'Settlers',
  }

  CATEGORIES = {
    'scarab': 'Scarab',
  }

  save_folder = "datas"  # 저장 폴더 이름
  fetch_and_save_data(DOMAIN['item'], LEAGUES, CATEGORIES, save_folder)

  # 파일 경로 설정
  api_data_path = "datas/settler/scarab.json"
  translation_path = "translations/scarab.json"
  output_path = "datas/settler/scarab_merged.json"
  
  # 데이터 병합
  merge_data(api_data_path, translation_path, output_path)

if __name__ == "__main__":
    main()