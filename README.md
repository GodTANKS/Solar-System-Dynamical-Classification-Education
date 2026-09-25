# ☄️ 태양계 천체 역학적 분류 · Data Science Astronomy Lab

태양계 천체의 궤도요소와 실제 카탈로그 데이터를 이용해 행성·왜소행성·소행성·혜성의 **역학적 분류 기준**을 탐구하는 Jupyter Notebook 기반 교육 콘텐츠입니다.

> **권장 대상:** 고등학생, 예비교사, 교사, 데이터 기반 천문학 입문자  
> **권장 환경:** Python 3 + Jupyter Notebook  
> **핵심 흐름:** 문제 정의 → 데이터 수집 → 탐색 → 처리 → 분석·표현 → 일반화

---

## 🚀 처음 사용하는 분을 위한 실행 순서

이 프로젝트는 최종적으로 아래 파일을 같은 작업 폴더에 두고 실행하도록 구성합니다.

```text
태양계 천체 역학적 분류_분석 코드.ipynb
dwarfplanet_asteroid_comet_analysis.csv
solarsystem_analysis13.py
requirements.txt
```

### 1. Python 준비
Python이 설치되어 있지 않다면 먼저 Python 3을 설치합니다.

### 2. 필요한 패키지 설치

터미널 또는 명령 프롬프트에서:

```bash
pip install -r requirements.txt
```

### 3. Jupyter 실행

```bash
jupyter notebook
```

### 4. Notebook 열기

`태양계 천체 역학적 분류_분석 코드.ipynb`를 열고 **맨 위 셀부터 순서대로 실행**합니다.

### 5. 처음에는 코드를 바꾸지 않고 한 번 끝까지 실행

전체 결과가 정상적으로 나오는지 확인한 뒤, 궤도요소 범위나 시각화 조건을 조금씩 바꾸면서 탐구하는 것을 권장합니다.

---

## 📌 현재 GitHub 공개 상태

이 저장소는 **최신 역학적 분류 교육 콘텐츠용 공식 저장소**입니다.  
README와 실행환경 파일을 먼저 정리했으며, Notebook·CSV·보조 Python 파일 등 실행 핵심 자료는 최종본 기준으로 순차 정리하여 공개하는 구조입니다.

저장소에서 위의 핵심 파일이 모두 보일 때는 아래 실행 순서를 그대로 따르면 됩니다.  
파일이 아직 보이지 않는다면 업로드가 완료되기 전 상태입니다.

> 기존 `Solarsystem_object_orbit_3D` 저장소는 3차원 궤도 시각화를 중심으로 한 **이전 프로젝트**이며, 이 저장소와 구분합니다.

---

## 🔭 무엇을 탐구하나요?

- 장반경(semi-major axis)
- 이심률(eccentricity)
- 궤도경사각(inclination)
- 근일점 거리 및 기타 궤도 관련 요소
- 행성·왜소행성·소행성·혜성의 분포 차이
- 카탈로그 데이터를 이용한 역학적 분류
- 2D/3D 궤도 및 통계 시각화

단순한 천체 이름 분류가 아니라 **“궤도 특성이 왜 서로 다른가?”**를 데이터로 탐구합니다.

---

## 📁 주요 파일

| 파일 | 설명 |
|---|---|
| `태양계 천체 역학적 분류_분석 코드.ipynb` | 메인 Jupyter Notebook |
| `dwarfplanet_asteroid_comet_analysis.csv` | 분석용 태양계 천체 카탈로그 |
| `solarsystem_analysis13.py` | 궤도 분석·시각화 보조 함수 |
| `requirements.txt` | 필요한 Python 패키지 목록 |
| 활동지 PDF/HWP | 수업 및 탐구 기록용 자료 |
| 궤도 관련 이미지 | 궤도요소 개념 이해용 참고 자료 |

---

## 🧭 추천 실습 방법

1. **결과 먼저 보기** — 코드를 수정하지 않고 전체 실행
2. **그래프 읽기** — 천체 유형별 분포 차이를 말로 설명
3. **변수 바꾸기** — 궤도요소나 시각화 범위를 변경
4. **분류 기준 만들기** — 어떤 궤도 특성이 분류에 유용한지 정리
5. **결과 일반화** — 다른 태양계 소천체에도 적용 가능한지 토의

---

## 📦 주요 Python 패키지

- numpy
- pandas
- scikit-learn
- plotly
- astropy
- dash
- jupyter

설치가 잘 되지 않으면 먼저 다음을 실행한 뒤 다시 시도하세요.

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

---

## ❓ 자주 발생하는 문제

**Q. CSV 파일을 찾지 못합니다.**  
A. Notebook과 `dwarfplanet_asteroid_comet_analysis.csv`를 같은 작업 폴더에 두는 것을 권장합니다.

**Q. `solarsystem_analysis13` 관련 오류가 납니다.**  
A. `solarsystem_analysis13.py`가 Notebook과 같은 작업 폴더에 있는지 확인하세요.

**Q. Plotly 그래프가 안 보입니다.**  
A. Jupyter Notebook에서 모든 셀을 위에서부터 다시 실행한 뒤 브라우저를 새로고침해 보세요.

---

## 📄 관련 연구

논문 PDF는 코드 저장소에 중복 보관하지 않고 **통합 논문 모음**에서 관리합니다.

**[📚 통합 논문 모음에서 보기](https://GodTANKS.github.io/astronomy-data-science/papers/)**


---

## 🌐 통합 연구·교육 플랫폼

**AI · 데이터 사이언스로 탐구하는 천문학**  
https://GodTANKS.github.io/astronomy-data-science/

기존 연구 아카이브:  
https://sites.google.com/view/astronomydatascience/
