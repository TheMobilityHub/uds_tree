# **프로젝트 계획**

---

## **환경 구성**
- **OS**: Windows
- **IDE**: VS Code
- **Language**: Python (3.11)
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
     - NSIS 또는 Inno Setup으로 설치 프로그램 생성.

---

## **테스트**
- **테스트 도구**:
  - pytest: 유닛 테스트 및 통합 테스트.
  - unittest: 표준 유닛 테스트 프레임워크.
  - pytest-qt: PySide6 GUI 테스트.

---

## **패키지 및 가상 환경 관리**
- **패키지 관리자**:
  - pip
  - Poetry
- **가상 환경**:
  - venv: Python 기본 가상 환경 도구.
  - Conda: 데이터 과학 프로젝트용 가상 환경.

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
├── main.py
├── requirements.txt
├── README.md
├── src/
│   ├── __init__.py
│   ├── gui.py
│   └── utils.py
├── tests/
│   ├── __init__.py
│   └── test_main.py
└── docs/
    └── index.md
