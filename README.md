# ☄️ 태양계 천체 역학적 분류 · Data Science Astronomy Lab

실제 태양계 천체의 **궤도요소와 카탈로그 데이터**를 이용해 행성·왜소행성·소행성·혜성의 역학적 특성과 분류 기준을 탐구하는 교육 콘텐츠입니다.

> **권장 실행:** Google Colab 원본 반영판  
> **설치:** 필요 없음  
> **핵심 흐름:** 데이터 수집 → 전체 탐색 → 데이터 처리 → 세부 탐색 → 그래프 분석 → 개별 천체 2D/3D 궤도 분석 → 분류 정답 확인

---

## ▶ 권장 실행: 원본 Jupyter 흐름을 유지한 Colab판

**[🚀 Google Colab 원본 반영판 바로 실행](https://colab.research.google.com/github/GodTANKS/Solar-System-Dynamical-Classification-Education/blob/main/colab/%ED%83%9C%EC%96%91%EA%B3%84%20%EC%B2%9C%EC%B2%B4%20%EC%97%AD%ED%95%99%EC%A0%81%20%EB%B6%84%EB%A5%98_Colab_%EC%9B%90%EB%B3%B8%EB%B0%98%EC%98%81%ED%8C%90.ipynb)**

이 버전은 논문용 Jupyter Notebook을 단순 요약한 것이 아니라, **원본 127개 셀의 분석 순서와 대부분의 코드 셀을 그대로 유지**한 Colab 변환판입니다.

Colab과 충돌하는 부분만 바꾸었습니다.

- Jupyter `nbextensions` 설치 셀 제거
- 로컬 `CSV`·`solarsystem_analysis13.py`를 GitHub에서 자동 준비
- 원본의 Dash 서버형 UI 6개 셀을 **Colab 입력폼 + Plotly**로 변환
- 정적 예시 스크린샷 대신 실행 결과를 직접 확대·회전하도록 정리
- 원본 `solarsystem_analysis13.py` 분석 함수는 그대로 사용

따라서 원본에 포함된 데이터 전체 탐색, 주요유형·세부유형 분리, 기술통계, 상자수염·막대·산점도, 목성 티세랑 경계선, 개별 천체 시간별 위치 계산, 2D/3D 궤도 분석, 분류 정답 확인 흐름을 그대로 따라갈 수 있습니다.

### 빠른 체험용 간편판

원본 전체 흐름보다 짧게 핵심 기능만 먼저 체험하려면 아래 버전을 사용할 수 있습니다.

**[⚡ Colab 간편판 실행](https://colab.research.google.com/github/GodTANKS/Solar-System-Dynamical-Classification-Education/blob/main/colab/%ED%83%9C%EC%96%91%EA%B3%84%20%EC%B2%9C%EC%B2%B4%20%EC%97%AD%ED%95%99%EC%A0%81%20%EB%B6%84%EB%A5%98_Colab_%EA%B0%84%ED%8E%B8%ED%8C%90.ipynb)**

> 홈페이지의 기본 **Colab에서 실행** 버튼은 원본 반영판으로 연결합니다.

---

## 📁 저장소 구성

| 경로 | 설명 |
|---|---|
| `colab/태양계 천체 역학적 분류_Colab_원본반영판.ipynb` | 원본 127셀 분석 흐름을 최대한 유지한 권장 Colab판 |
| `colab/태양계 천체 역학적 분류_Colab_간편판.ipynb` | 핵심 기능을 빠르게 체험하는 축약판 |
| `src/solarsystem_analysis13.py` | 논문용 원본 궤도 계산·데이터 처리 함수 |
| `data/catalog_b64/` | 전체 카탈로그 자동 복원용 압축 데이터 |
| `requirements.txt` | 로컬 Jupyter 실행용 패키지 목록 |

전체 카탈로그는 Colab 시작 셀에서 자동으로 복원되므로 사용자가 CSV를 따로 업로드할 필요가 없습니다.

---

## 🔭 주요 탐구 내용

- 장반경(semi-major axis)
- 이심률(eccentricity)
- 궤도경사각(inclination)
- 근일점·원일점 거리
- 지구와의 최소 궤도 교차거리(MOID)
- 목성 티세랑(Jupiter Tisserand)
- 행성·왜소행성·소행성·혜성의 유형별 분포
- 근지구천체(NEO)와 지구위협천체(PHA)
- 상자수염·막대·산점도 기반 데이터 탐색
- 개별 천체의 시간별 위치와 2D/3D 궤도
- 기존 분류와 탐구자가 찾은 분류 기준 비교

---

## 🧭 처음 사용하는 순서

1. **원본 반영판 Colab**을 엽니다.
2. 맨 위 환경 준비 셀부터 순서대로 실행합니다.
3. 전체 데이터와 기술통계를 먼저 확인합니다.
4. 주요유형·세부유형별 데이터 세트를 비교합니다.
5. 산점도·상자수염·막대 그래프에서 분류 기준을 찾습니다.
6. 개별 천체 식별번호(`pdes`)를 입력해 2D/3D 궤도를 분석합니다.
7. 마지막에 기존 분류를 확인하고 자신이 만든 분류 기준과 비교합니다.

> 3D 궤도 계산이 느릴 때는 궤도선 점 개수(`nps`)를 **101~201** 정도로 낮추면 됩니다.

---

## 📄 관련 연구

논문 PDF는 코드 저장소에 중복 보관하지 않고 **통합 논문 모음**에서 관리합니다.

**[📚 논문 보기](https://GodTANKS.github.io/astronomy-data-science/papers/#solar-system)**

---

## 🌐 통합 천문학 실습 홈페이지

**AI · 데이터 사이언스로 탐구하는 천문학**  
https://GodTANKS.github.io/astronomy-data-science/

기존 연구 아카이브:  
https://sites.google.com/view/astronomydatascience/

---

> 기존 `Solarsystem_object_orbit_3D` 저장소는 3차원 궤도 시각화를 중심으로 한 이전 프로젝트이며, 이 저장소의 최신 교육 콘텐츠와 구분합니다.

---

## 📘 교육·학습 목적 이용 조건

이 저장소에서 **공개된 코드·노트북·교육 자료**는 원저자·원본 저장소·관련 논문 출처를 명시하는 조건으로 **교육·학습 및 비상업적 연구 목적의 복제·수정·재배포가 가능합니다.**

**상업적 판매·유료 서비스·출처 삭제·타인의 독창적 연구 결과인 것처럼 사용하는 행위는 허용하지 않습니다.**

자세한 조건: [EDUCATIONAL_USE_NOTICE.md](EDUCATIONAL_USE_NOTICE.md)

