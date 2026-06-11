# AI 활용 자유 주제 파이썬 미니 프로젝트
# 이름 또는 학번: 20924 황다인
# 프로젝트 주제: 수술 후 환자 통증(NRS) 기록 및 무통주사(PCA) 부작용 모니터링기

# [1] 데이터: 환자 현황 (2차원 리스트)
# 열 구조: [0]번호, [1]수술명, [2]통증점수, [3]부작용
patients = [
    ["P001", "복강경수술", 6, "오심"],
    ["P002", "충수절제술", 2, "없음"],
    ["P003", "제왕절개술", 3, "어지러움"]
]

# [2] 기능 1: 환자의 상태를 진단하는 함수 (첫 번째 함수)
def analyze_patient(patient):
    # 복합 조건 판정 (부작용 확인 -> 통증 확인)
    if patient[3] != "없음":
        return f"🚨 [주입 중단 및 부작용 완화 약물 투여 후 재주입] 부작용({patient[3]}) 발생! PCA 잠금 및 보고"
    elif patient[2] >= 4:
        return f"⚠️ [추가 주입] 통증({patient[2]}점) 높음! 추가 주입 고려"
    else:
        return "✅ [유지] 통증 및 부작용 안정적임"

# [3] 기능 2: 현재 병동 환자들을 모두 모니터링하여 출력하는 함수 (두 번째 함수)
def monitor_all_patients():
    print("\n[현재 병동 환자 실시간 상태 분석]")
    # 반복문으로 2차원 리스트의 행을 하나씩 뽑아 분석 결과 출력
    for p in patients:
        print(f"▶ 환자 {p[0]} ({p[1]}) -> {analyze_patient(p)}")

# [4] 기능 3: 신규 환자의 정보를 입력받아 등록하는 함수 (세 번째 함수)
def register_new_patient():
    print("\n[신규 환자 정보 등록]")
    num = input("환자 번호: ")
    op = input("수술명: ")
    pain = int(input("통증 점수(0~10): ")) # 숫자로 형변환
    side = input("부작용 증상(없음/오심/어지러움 등): ")
    
    # 입력된 데이터를 리스트로 묶어 기존 2차원 리스트에 추가
    new_patient = [num, op, pain, side]
    patients.append(new_patient)
    
    print(f"\n[등록 완료] {num}번 환자가 병동 데이터에 추가되었습니다.")
    print(f"새 환자 실시간 분석: {analyze_patient(new_patient)}")


# [5] 프로그램 실제 실행 부분 (흐름 제어)
print("=== 🏥 환자 통증 및 부작용 모니터링 시스템 ===")

# 분리한 함수들을 순서대로 호출합니다.
monitor_all_patients()  # 1. 전체 환자 모니터링 기능 실행
print("\n" + "="*40)
register_new_patient()  # 2. 신규 환자 등록 기능 실행