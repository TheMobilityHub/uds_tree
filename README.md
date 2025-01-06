# **프로젝트 계획**

---

## **환경 구성**
- **OS**: Windows
- **IDE**: VS Code
- **Language**: Python (3.94)
- **Framework**: PySide6

---

## **코드 컨벤션**
- **스타일 가이드**:
  - PEP8
  - Google Python Style Guide
- **도구**:
  - Black: 코드 포맷팅
  - Flake8: 코드 품질 검사
  - isort: Import 정렬
  - mypy: 정적 타입 검사
- **통합 방법**:
  - VS Code에 Black, Flake8 플러그인 설치 및 설정.

---

## **빌드 및 배포**
- **빌드 도구**: PyInstaller
- **배포 방법**:
  1. **로컬 배포**:
     - 실행 파일 생성 후 회사 공유 폴더를 통해 배포.
  2. **온라인 배포**:
     - GitHub Releases를 사용하여 실행 파일 업로드.
  3. **설치 프로그램 생성**:
     - NSIS 

---

## **테스트**
- **테스트 도구**:
  - pytest: 유닛 테스트 및 통합 테스트.
  - pytest-qt: PySide6 GUI 테스트.

---

## **패키지 및 가상 환경 관리**
- **패키지 관리자**:
  - pip
- **가상 환경**:
  - venv: Python 기본 가상 환경 도구.

---

## **CI/CD**
- **도구**: GitHub Actions
- **설정**:
  - 테스트 자동화.
  - 빌드 및 배포 자동화.

---

## **로그 및 에러 관리**
- **도구**: Sentry
  - 실시간 에러 추적 및 로깅.

---

## **문서 관리**
- **도구**: Wiki
- **내용**:
  - 프로젝트 개요.
  - 설치 및 실행 방법.
  - 주요 코드 설명.

---

## **프로젝트 구조**
```plaintext
project_name/
├── main.py                     # 프로젝트 진입점
├── requirements.txt            # Python 패키지 의존성
├── README.md                   # 프로젝트 설명 문서
├── LICENSE                     # 라이선스 정보
├── .github/
│   └── workflows/              # GitHub Actions 설정
│       ├── build.yml           # 빌드 및 배포 자동화
│       └── test.yml            # 테스트 및 커버리지 리포트 자동화
├── src/                        # 애플리케이션 소스 코드
│   ├── __init__.py
│   ├── main_window.py          # PySide6 메인 윈도우 구성
│   ├── gui/                    # GUI 관련 모듈 (View)
│   │   ├── __init__.py
│   │   ├── uds_view.py         # UDS 통신 GUI 화면
│   │   └── settings_view.py    # 설정 화면
│   ├── controller/             # 컨트롤러 (Controller)
│   │   ├── __init__.py
│   │   ├── uds_controller.py   # UDS 통신 로직
│   │   └── settings_controller.py # 설정 로직
│   ├── model/                  # 데이터 처리 및 비즈니스 로직 (Model)
│   │   ├── __init__.py
│   │   ├── uds_model.py        # UDS 데이터 처리
│   │   └── settings_model.py   # 설정 데이터 처리
│   ├── utils/                  # 유틸리티 모듈
│   │   ├── __init__.py
│   │   ├── file_loader.py      # YML 파일 로드 및 파싱
│   │   └── logger.py           # 로그 관리
├── resources/                  # 리소스 파일 저장소
│   ├── images/                 # 이미지 및 아이콘 파일
│   │   ├── logo.png            # 로고 파일
│   │   ├── icon.ico            # 애플리케이션 아이콘
│   └── qrc/                    # Qt 리소스 파일
│       └── resources.qrc       # 리소스 정의 파일
├── ui/                         # .ui 파일 저장소
│   ├── main_window.ui          # 메인 윈도우 UI 파일
│   ├── uds_view.ui             # UDS 뷰 UI 파일
│   └── settings_view.ui        # 설정 화면 UI 파일
├── tests/                      # 테스트 코드
│   ├── __init__.py
│   ├── test_main.py            # 메인 테스트 코드
│   ├── test_gui.py             # GUI 테스트 (pytest-qt 사용)
│   ├── test_controller.py      # 컨트롤러 테스트
│   └── coverage/               # 테스트 커버리지 결과 저장
│       ├── index.html          # 커버리지 HTML 리포트
│       └── coverage.xml        # 커버리지 XML 리포트
├── dist/                       # PyInstaller 빌드 결과물
│   └── project_name.exe        # 빌드된 실행 파일
├── docs/                       # 문서화 관련 파일
│   ├── index.md                # 문서 메인 페이지
│   ├── usage.md                # 사용법
│   └── api_reference.md        # API 참조
└── builds/                     # 배포 관련 파일 저장소
    ├── releases/               # GitHub Releases에 올릴 파일
    │   ├── project_name_v1.0.exe # 실행 파일
    │   └── coverage_report_v1.0.zip # 테스트 커버리지 결과
    └── artifacts/              # 빌드 아티팩트 저장


