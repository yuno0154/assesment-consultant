import pandas as pd
import re
import os
import glob

# 설정
TARGET_DIR = r'd:/OneDrive - 사곡고등학교/2026학년도/프로그램 개발/엑셀 관련'
INPUT_FILES = glob.glob(os.path.join(TARGET_DIR, "*.xlsx"))

def get_first_category(val):
    if pd.isna(val):
        return None
    # 숫자(1~6) 추출
    digits = re.findall(r'[1-6]', str(val))
    if digits:
        return int(digits[0])
    return None

def process():
    if not INPUT_FILES:
        print("엑셀 파일을 찾을 수 없습니다.")
        return

    # 가장 최근 파일 선택 (또는 특정 파일 지정)
    input_file = INPUT_FILES[0]
    print(f"파일 처리 중: {input_file}")

    try:
        # 엑셀 파일 읽기
        df = pd.read_excel(input_file)
        
        # '대상*' 컬럼 또는 유사한 컬럼 찾기
        target_col = None
        for col in df.columns:
            if '대상' in str(col):
                target_col = col
                break
        
        if not target_col:
            print("'대상*' 관련 컬럼을 찾을 수 없습니다. 기본 '대상*' 사용 시도...")
            target_col = '대상*'

        # 분류 적용 (1~6)
        df['Classification'] = df[target_col].apply(get_first_category)

        # 1~6번까지 각각 파일로 저장
        for i in range(1, 7):
            category_df = df[df['Classification'] == i].drop(columns=['Classification'])
            if not category_df.empty:
                output_path = os.path.join(TARGET_DIR, f'category_{i}.csv')
                category_df.to_csv(output_path, index=False, encoding='utf-8-sig')
                print(f"생성 완료: {output_path} ({len(category_df)}명)")

        print("\n모든 작업이 완료되었습니다.")
        print("이제 생성된 CSV 파일들을 index.html에서 불러와서 확인할 수 있습니다.")

    except Exception as e:
        print(f"오류 발생: {e}")

if __name__ == "__main__":
    process()
