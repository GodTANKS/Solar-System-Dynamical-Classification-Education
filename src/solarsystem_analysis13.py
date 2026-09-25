# -*- coding: utf-8 -*-
"""테양계 천체 역학적 분류 함수 모음

# **태양계 천체 역학적 분류 함수 모음**
"""

from sklearn.preprocessing import LabelEncoder # 문자형 데이터를 숫자형으로 바꿔주는 패키지
from astropy.time import Time # 율리우스력과 그레고리력 변환 패키지
import numpy as np # 데이터 수학 계산 패키지
import pandas as pd # 데이터 처리 패키지
from plotly.subplots import make_subplots # 그래프 분할 패키지
import plotly.graph_objs as go # 데이터 시각화(그래프 표현) 패키지
import plotly # 데이터 시각화(그래프 표현) 패키지
import plotly.express as px  # 데이터 시각화(그래프 표현) 패키지

"""## 1 음수 각도를 양수 각도로 변환 함수"""

def degree_to_plus(element_degree): # 함수 입력값(변환할 각도(단위:도))
  initial_degree = element_degree
  while initial_degree < 0: # 음수 각도면 양수가 될때까지 +360 시행
    initial_degree = initial_degree + 360
    if initial_degree >= 0: # 음수 각도가 0이상이 되면 최종 수정 데이터로 취급
      initial_degree = initial_degree
  return initial_degree # 함수 출력값

"""## 2 입력된 율리우스력 시간의 태양계 행성 궤도 요소를 구하는 함수"""

# 입력된 율리우스력 시간의 태양계 행성 궤도 요소를 구하는 함수
def planet_orbit_element(julian_date): # 함수 입력값(율리우스력 일)
  au_m = 149597870700 # 천문 단위 m
  au_km = au_m*(10**-3) # 천문 단위 km
  day_s = 60*60*24 # 1일을 초로 환산
  GM_sun = 1.32712440041279419*(10**20)*(day_s**2)/(au_m**3) # 태양 중력상수
  GM_mercury = 22031.868551*(day_s**2)/(au_km**3) # 수성 중력상수
  GM_venus = 324858.592000*(day_s**2)/(au_km**3) # 금성 중력상수
  GM_earth = 398600.435507*(day_s**2)/(au_km**3) # 지구 중력상수
  GM_mars = 42828.375816*(day_s**2)/(au_km**3) # 화성 중력상수
  GM_jupiter = 126712764.100000*(day_s**2)/(au_km**3) # 목성 중력상수
  GM_saturn = 37940584.841800*(day_s**2)/(au_km**3) # 토성 중력상수
  GM_uranus = 5794556.400000*(day_s**2)/(au_km**3) # 천왕성 중력상수
  GM_neptune = 6836527.100580*(day_s**2)/(au_km**3) # 해왕성 중력상수

  j_d = julian_date # 율리우스력 일
  t = j_d - 2451545 # 수정된 율리우스력 일
  T = t / 36525 # 율리우스력 세기

  # 지구
  p3_a = 1.00000011 - 0.00000005*T # 시간별 장반경
  p3_e = 0.01671022 - 0.00003804*T # 시간별 이심률
  p3_q = p3_a*(1-p3_e) # 시간별 근일점
  p3_ad = p3_a*(1+p3_e) # 시간별 원일점
  p3_i = 0.00005 - 46.94/(60*60)*T # 시간별 경사각
  p3_om = -11.26064-18228.25/(60*60)*T # 시간별 승교점 경도
  p3_w1 = 102.94719 + 1198.28/(60*60)*T # 시간별 근일점 경도
  p3_l = 100.46435 + 0.98560910*t # 시간결 평균 경도
  p3_l1 = p3_l -360*(p3_l//360) # 시간별 평균 경도가 360도를 넘어가면 0~360도 내로 변환
  p3_w = p3_w1 - p3_om #degree_to_plus(p3_w1 - p3_om) # 시간별 근일점 이각
  p3_ma = np.deg2rad( p3_l1 - p3_w1 ) # np.deg2rad( degree_to_plus(p3_l - p3_w1) ) # 시간별 평균 이각
  p3_p = 2*np.pi*np.sqrt(p3_a**3/(GM_sun + GM_earth)) # 공전주기(일)
  p3_p_y = p3_p/p3_p # 공전주기(년)
  p3_tp = j_d - p3_ma*p3_p/(2*np.pi) # 근일점 통과 시각(율리우스력)
  p3_tp_cal = Time(p3_tp, format='jd').iso # 근일점 통과 시각(그레고리력)

  earth_sidereal_year = p3_p # 지구 공전주기(항성일)

  # 수성
  p1_a = 0.38709893 + 0.00000066*T
  p1_e = 0.20563069 + 0.00002527*T
  p1_q = p1_a*(1-p1_e)
  p1_ad = p1_a*(1+p1_e)
  p1_i = 7.00487 - 23.51/(60*60)*T
  p1_om = 48.33167 - 446.30/(60*60)*T
  p1_w1 = 77.45645 + 573.57/(60*60)*T
  p1_l = 252.25084 + 4.092333880*t
  p1_l1 = p1_l -360*(p1_l//360)
  p1_w =  degree_to_plus(p1_w1 - p1_om)
  p1_ma = np.deg2rad( degree_to_plus(p1_l1 - p1_w1) ) #np.deg2rad(168.6562 + 4.0923344368*t)
  p1_p = 2*np.pi*np.sqrt(p1_a**3/(GM_sun + GM_mercury))
  p1_p_y = p1_p/earth_sidereal_year
  p1_tp = j_d - p1_ma*p1_p/(2*np.pi)
  p1_tp_cal = Time(p1_tp, format='jd').iso
  # 금성
  p2_a = 0.72333199 + 0.00000092*T
  p2_e = 0.00677323 - 0.00004938*T
  p2_q = p2_a*(1-p2_e)
  p2_ad = p2_a*(1+p2_e)
  p2_i = 3.39471 - 2.86/(60*60)*T
  p2_om = 76.68069 - 996.89/(60*60)*T
  p2_w1 = 131.53298 - 108.80/(60*60)*T
  p2_l = 181.97973 + 1.60213047*t
  p2_l1 = p2_l -360*(p2_l//360)
  p2_w = degree_to_plus(p2_w1 - p2_om)
  p2_ma = np.deg2rad( degree_to_plus(p2_l1 - p2_w1) ) # np.deg2rad(48.0052 + 1.6021302244*t)
  p2_p = 2*np.pi*np.sqrt(p2_a**3/(GM_sun + GM_venus))
  p2_p_y = p2_p/earth_sidereal_year
  p2_tp = j_d - p2_ma*p2_p/(2*np.pi)
  p2_tp_cal = Time(p2_tp, format='jd').iso
  # 화성
  p4_a = 1.52366231 - 0.00007221*T
  p4_e = 0.09341233 + 0.00011902*T
  p4_q = p4_a*(1-p4_e)
  p4_ad = p4_a*(1+p4_e)
  p4_i = 1.85061 - 25.47/(60*60)*T
  p4_om = 49.57854 - 1020.19/(60*60)*T
  p4_w1 = 336.04084 + 1560.78/(60*60)*T
  p4_l = 355.45332 + 0.52403304*t
  p4_l1 = p4_l -360*(p4_l//360)
  p4_w = degree_to_plus(p4_w1 - p4_om)
  p4_ma = np.deg2rad( degree_to_plus(p4_l1 - p4_w1) ) #np.deg2rad(18.6021 + 0.5240207766*t)
  p4_p = 2*np.pi*np.sqrt(p4_a**3/(GM_sun + GM_mars))
  p4_p_y = p4_p/earth_sidereal_year
  p4_tp = j_d - p4_ma*p4_p/(2*np.pi)
  p4_tp_cal = Time(p4_tp, format='jd').iso
  # 목성
  p5_a = 5.20336301 + 0.00060737*T
  p5_e = 0.04839266 - 0.00012880*T
  p5_q = p5_a*(1-p5_e)
  p5_ad = p5_a*(1+p5_e)
  p5_i = 1.30530 - 4.15/(60*60)*T
  p5_om = 100.55615 + 1217.17/(60*60)*T
  p5_w1 = 14.75385 + 839.93/(60*60)*T
  p5_l = 34.40438 + 0.08308676*t
  p5_l1 = p5_l -360*(p5_l//360)
  p5_w = degree_to_plus(p5_w1 - p5_om)
  p5_ma = np.deg2rad( degree_to_plus(p5_l1 - p5_w1) ) # np.deg2rad(19.8950 + 0.0830853001*t)
  p5_p = 2*np.pi*np.sqrt(p5_a**3/(GM_sun + GM_jupiter))
  p5_p_y = p5_p/earth_sidereal_year
  p5_tp = j_d - p5_ma*p5_p/(2*np.pi)
  p5_tp_cal = Time(p5_tp, format='jd').iso
  # 토성
  p6_a = 9.53707032 - 0.00301530*T
  p6_e = 0.05415060 - 0.00036762*T
  p6_q = p6_a*(1-p6_e)
  p6_ad = p6_a*(1+p6_e)
  p6_i = 2.48446 + 6.11/(60*60)*T
  p6_om = 113.71504 - 1591.05/(60*60)*T
  p6_w1 = 92.43194 - 1948.89/(60*60)*T
  p6_l = 49.94432 + 0.03346063*t
  p6_l1 = p6_l -360*(p6_l//360)
  p6_w = degree_to_plus(p6_w1 - p6_om)
  # p6_m1 = 316.9670 + 0.0334442282*t - 360
  p6_ma =  np.deg2rad( degree_to_plus(p6_l1 - p6_w1) )# np.deg2rad(p6_m1) # np.deg2rad(p6_l - p6_w1)
  p6_p = 2*np.pi*np.sqrt(p6_a**3/(GM_sun + GM_saturn))
  p6_p_y = p6_p/earth_sidereal_year
  p6_tp = j_d - p6_ma*p6_p/(2*np.pi)
  p6_tp_cal = Time(p6_tp, format='jd').iso
  # 천왕성
  p7_a = 19.19126393 + 0.00152025*T
  p7_e = 0.04716771 - 0.00019150*T
  p7_q = p7_a*(1-p7_e)
  p7_ad = p7_a*(1+p7_e)
  p7_i = 0.76986 - 2.09/(60*60)*T
  p7_om = 74.22988 + 1681.40/(60*60)*T
  p7_w1 = 170.96424 + 1312.56/(60*60)*T
  p7_l = 313.23218 + 0.01173129*t
  p7_l1 = p7_l -360*(p7_l//360)  
  p7_w = degree_to_plus(p7_w1 - p7_om)
  p7_ma = np.deg2rad( degree_to_plus(p7_l1 - p7_w1) ) # np.deg2rad(142.5905 + 0.011725806*t)
  p7_p = 2*np.pi*np.sqrt(p7_a**3/(GM_sun + GM_uranus))
  p7_p_y = p7_p/earth_sidereal_year
  p7_tp = j_d - p7_ma*p7_p/(2*np.pi)
  p7_tp_cal = Time(p7_tp, format='jd').iso
  # 해왕성
  p8_a = 30.06896348 - 0.00125196*T
  p8_e = 0.00858587 + 0.00002514*T
  p8_q = p8_a*(1-p8_e)
  p8_ad = p8_a*(1+p8_e)
  p8_i = 1.76917 - 3.64/(60*60)*T
  p8_om = 131.72169 - 151.25/(60*60)*T
  p8_w1 = 44.97135 - 844.43/(60*60)*T
  p8_l = 304.88003 + 0.00598106*t
  p8_l1 = p8_l -360*(p8_l//360)
  p8_w = degree_to_plus(p8_w1 - p8_om)
  p8_ma = np.deg2rad( degree_to_plus(p8_l1 - p8_w1) ) # np.deg2rad(260.2471 + 0.005995147*t)
  p8_p = 2*np.pi*np.sqrt(p8_a**3/(GM_sun + GM_neptune))
  p8_p_y = p8_p/earth_sidereal_year
  p8_tp = j_d - p8_ma*p8_p/(2*np.pi)
  p8_tp_cal = Time(p8_tp, format='jd').iso
  # 행성 궤도 요소를 데이터 프레임으로 생성
  df_p = pd.DataFrame({'full_name':['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'], # 천체명
                      'pdes':['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'], # 식별번호
                      'q':[p1_q, p2_q, p3_q, p4_q, p5_q, p6_q, p7_q, p8_q], # 근일점(au)
                      'ad':[p1_ad, p2_ad, p3_ad, p4_ad, p5_ad, p6_ad, p7_ad, p8_ad], # 원일점(au)
                      'a':[p1_a, p2_a, p3_a, p4_a, p5_a, p6_a, p7_a, p8_a], # 장반경(au)
                      'e':[p1_e, p2_e, p3_e, p4_e, p5_e, p6_e, p7_e, p8_e], # 이심률
                      'i':[p1_i, p2_i, p3_i, p4_i, p5_i, p6_i, p7_i, p8_i], # 경사각(degree)
                      'om':[p1_om, p2_om, p3_om, p4_om, p5_om, p6_om, p7_om, p8_om], # 승일점 경도(degree)
                      'w':[p1_w, p2_w, p3_w, p4_w, p5_w, p6_w, p7_w, p8_w], # 근일점 이각(degree)
                      #'m':[np.rad2deg(p1_ma), np.rad2deg(p2_ma), np.rad2deg(p3_ma), np.rad2deg(p4_ma),
                      #     np.rad2deg(p4_ma), np.rad2deg(p6_ma), np.rad2deg(p7_ma), np.rad2deg(p8_ma)],
                      'tp':[p1_tp, p2_tp, p3_tp, p4_tp, p5_tp, p6_tp, p7_tp, p8_tp], # 근일점 통과 시각(율리우스력 일)
                      #'tp_cal':[p1_tp_cal, p2_tp_cal,p3_tp_cal, p4_tp_cal, p5_tp_cal, p6_tp_cal, p7_tp_cal, p8_tp_cal], # 근일점 통과
                      'moid':[-9, -9, -9, -9, -9, -9, -9, -9], # 지구와의 최소 궤도 교차거리                     
                      'per':[p1_p, p2_p, p3_p, p4_p, p5_p, p6_p, p7_p, p8_p], # 공전주기(일)
                      'per_y':[p1_p_y, p2_p_y, p3_p_y, p4_p_y, p5_p_y, p6_p_y, p7_p_y, p8_p_y], # 공전주기(년)
                      't_jup':[-99, -99, -99, -99, -99, -99, -99, -99], # 목성 티세랑 (행성은 목성 티세랑을 구할 수 없으니 목성 티세랑 값이 태양계 천체에서는 나올 수 없는 값을 임의로 작성
                      'pr_class':['Planet', 'Planet', 'Planet', 'Planet', 'Planet', 'Planet', 'Planet', 'Planet'], # 주요유형
                      'dt_class':['TP', 'TP', 'TP', 'TP', 'JP', 'JP', 'JP', 'JP'], # 세부유형
                      'neo':['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N'], # 근지구형 천체 유무
                      'pha':['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N'] # 지구위협형 천체 유무
  })
  return df_p # 함수 출력값
  
"""## 3 입력된 율리우스력 시간의 천체 위치를 산출하는 함수"""

# 입력된 율리우스력 시간의 천체 위치를 산출하는 함수
def orbit_point(a, e, i, om, w, tp, per, julian_date):
  # 함수 입력값(a(장반경, 단위:au), e(이심률), i(경사각, 단위:도), om(승교점 경도, 단위:도), w(근일점 이각, 단위:도),
  # tp(근일점 통과시각, 단위:율리우스력 일), per(공전주기, 단위: 율리우스력 일), julian_date(율리우스력 시간, 단위: 일))
  # 각도를 라디안으로 변환
  i_rad = np.deg2rad(i) # 도->라디안
  o_rad = np.deg2rad(om) # 도->라디안
  w_rad = np.deg2rad(w) # 도->라디안

  # 평균근일점 이각(mean anomaly)
  j_d = julian_date # 입력된 율리우스력 일
  m = (j_d - tp)*2*np.pi/per # (입력된 율리우스력 일 - 알고자하는 행성의 근일점 통과시각(UTC)에 대한 율리우스력 일)*2π/공전주기(일)
  if m < 0:
    M = m + 2*np.pi
  else:
    M = m

  # 반복 접근법을 이용한 수치해석적(완력적 접근법) 이심 이각(eccentric anomaly)
  E = M.copy()
  n = 0 # n에 대입되는 초기값
  while True: # if문의 En+1 - En < 10^-10 조건이 만족할 때까지 반복 시행
    globals()['E{}'.format(0)] = M # 초기값은 평균근일점 이각
    globals()['E{}'.format(n+1)] = M + e*np.sin(globals()['E{}'.format(n)]) # 반복과정
    if abs(globals()['E{}'.format(n+1)] - globals()['E{}'.format(n)]) < 10**-10:
      E = globals()['E{}'.format(n+1)]
      break # En+1 - En < 10^-10 일때 반복문 멈추고 그 En+1이 최종 이심 이각이 됨
    n += 1 # n에 대입되는 값이 +1만큼 증가하며 순환함

  # 진 근일점 이각(true anomaly)
  f = 2*np.arctan2(np.sqrt(1+e)*np.sin(E/2), np.sqrt(1-e)*np.cos(E/2))

  # 태양으로부터 천체까지의 거리(단위, au)
  r = a*(1-e**2)/(1+e*np.cos(f))

  # 직교좌표로 변환(x, y, z 좌표, 단위 au)
  x = r*(np.cos(o_rad)*np.cos(w_rad+f) - np.sin(o_rad)*np.sin(w_rad+f)*np.cos(i_rad))
  y = r*(np.sin(o_rad)*np.cos(w_rad+f) + np.cos(o_rad)*np.sin(w_rad+f)*np.cos(i_rad))
  z = r*np.sin(w_rad+f)*np.sin(i_rad)
  return r, x, y, z # 함수 출력값

"""## 4 천체의 궤도 선을 산출하는 함수"""

# 천체의 궤도 선을 산출하는 함수
def orbit_line(a, e, i, om, w, nps):
  # 함수 입력값(a(장반경, 단위:au), e(이심률), i(경사각, 단위:도), om(승교점 경도, 단위:도), w(근일점 이각, 단위:도),
  # points_num(평균근일점 이각의 점 개수))
  # 각도를 라디안으로 변환
  i_rad = np.deg2rad(i) # 도->라디안
  o_rad = np.deg2rad(om) # 도->라디안
  w_rad = np.deg2rad(w) # 도->라디안

  # 원 궤도를 나타내는 각도 범위 = 평균근일점 이각(mean anomaly)
  M = np.linspace(start=0, stop=2*np.pi, num=int(nps)) # 2**5
  # num에서 지정한 점 개수만큼 0이상 2π이하 숫자 생성(이때 숫자 사이 간격은 균등)
  # 점 개수를 줄일수록 컴퓨터 메모리 부하가 감소되지만, 그만큼 궤도 모양이 찌그러짐짐

  # 반복 접근법을 이용한 수치해석적(완력적 접근법) 이심 이각(eccentric anomaly)
  E = M.copy()
  for i in range(len(M)): # 점 개수만큼 반복 시
    n = 0 # n에 대입되는 초기값
    while True: # if문의 En+1 - En < 10^-10 조건이 만족할 때까지 반복 시행
      globals()['E{}'.format(0)] = M[i] # 초기값은 평균근일점 이각
      globals()['E{}'.format(n+1)] = M[i] + e*np.sin(globals()['E{}'.format(n)]) # 반복과정
      if abs(globals()['E{}'.format(n+1)] - globals()['E{}'.format(n)]) < 10**-10:
        E[i] = globals()['E{}'.format(n+1)]
        break # En+1 - En < 10^-10 일때 반복문 멈추고 그 En+1이 최종 이심 이각이 됨
      n += 1 # n에 대입되는 값이 +1만큼 증가하며 순환함

  # 진근일점 이각(true anomaly)
  f = 2*np.arctan2(np.sqrt(1+e)*np.sin(E/2), np.sqrt(1-e)*np.cos(E/2))

  # 태양으로부터 천체까지의 거리(단위, au)
  r = a*(1-e**2)/(1+e*np.cos(f))

  # 직교좌표로 변환(x, y, z 좌표, 단위 au)
  x = r*(np.cos(o_rad)*np.cos(w_rad+f) - np.sin(o_rad)*np.sin(w_rad+f)*np.cos(i_rad))
  y = r*(np.sin(o_rad)*np.cos(w_rad+f) + np.cos(o_rad)*np.sin(w_rad+f)*np.cos(i_rad))
  z = r*np.sin(w_rad+f)*np.sin(i_rad)
  return r, x, y, z # 함수 출력값

"""## 5 천체 궤도선 정보 출력 함수 (시간별 위치 정보 없음)"""

# 천체 궤도선 정보 출력 함수 (시간별 위치 정보 없음)
def df_orbit_line_xyz(object_dataframe, nps):
  # 함수 입력값(천체 데이터 세트, 궤도를 그리는데 필요한 점 개수),
  for s in range(len(object_dataframe)): # 천체의 개수 만큼 반복 시행
    n = object_dataframe.loc[s, 'full_name'] # 천체의 명칭
    p = object_dataframe.loc[s, 'pdes'] # 천체의 식별번호
    q = object_dataframe.loc[s, 'q'] # 천체의 근일점
    ad = object_dataframe.loc[s, 'ad'] # 천체의 원일점
    a = object_dataframe.loc[s, 'a'] # 천체의 장반경(태양과의 거리)(au)
    e = object_dataframe.loc[s, 'e'] # 천체의 이심률
    i = object_dataframe.loc[s, 'i'] # 천체의 경사각(황도면을 기준으로 기울어진 각도)(degree)
    om = object_dataframe.loc[s, 'om'] # 천체의 승교점 경도(황위가 -에서 +로 올라가면서 황도면과 교차하는 지점의 황경)(degree)
    w = object_dataframe.loc[s, 'w'] # 천체의 근일점 이각(승교점에서 근일점까지의 반시계방향(황경이 증가하는 방향의 이각)(degree)
    tp = object_dataframe.loc[s, 'tp'] # 천체의 근일점 통과시각(율리우스력 일)
    moid = object_dataframe.loc[s, 'moid'] # 천체의 지구와의 최소 궤도 교차거리
    per = object_dataframe.loc[s, 'per'] # 천체의 공전주기(일)
    per_y = object_dataframe.loc[s, 'per_y'] # 천체의 공전주기(년)
    t_jup = object_dataframe.loc[s, 't_jup'] # 천체의 공전주기(년)
    pr = object_dataframe.loc[s, 'pr_class'] # 천체의 주요유형
    dt = object_dataframe.loc[s, 'dt_class'] # 천체의 세부유형
    neo = object_dataframe.loc[s, 'neo'] # 천체의 근지구형 유무
    pha = object_dataframe.loc[s, 'pha'] # 천체의 지구위협형 유무
    r ,x ,y, z = orbit_line(a, e, i, om, w, nps) # 천체 궤도 선 산출 함수로 태양과의 거리, xyz 좌표 산출
    nps_range = np.arange(0, nps) # 입력된 점 개수 만큼 궤도를 그리는데 필요한 점 생성
    globals()['df_line{}'.format(s)] = pd.DataFrame({'full_name':n, 'pdes':p, 'q':q, 'ad':ad, 'a':a, 'e':e, 'i':i, 'om':om, 'w':w,
                                                      'tp':tp, 'moid':moid, 'per':per, 'per_y':per_y, 't_jup':t_jup, 'pr_class':pr, 'dt_class':dt,
                                                      'neo':neo, 'pha':pha, 'x':x, 'y':y, 'z':z, 'nps':nps_range})
    if s == 0:
      globals()['df_line_c{}'.format(s+1)] = globals()['df_line{}'.format(s)]
      print(s)
    elif s > 0 :
      print(s)
      globals()['df_line_c{}'.format(s+1)] = pd.concat([ globals()['df_line{}'.format(s)], globals()['df_line_c{}'.format(s)] ])
      if s == len(object_dataframe)-1:
        df_line_all = globals()['df_line_c{}'.format(s+1)]
  return df_line_all # 함수 출력값

"""## 6 입력된 시간별 행성의 궤도 정보 출력 함수"""

# 입력된 시간별 행성의 궤도 정보 출력 함수
def planet_datetimeframe(start_juliandate, finish_juliandate, timedelta_day):
  # 함수 입력값(시작 시간(단위:율리우스력 일), 종료 시간(단위:율리우스력 일),
  # 시간 간격(단위:율리우스력 일))
  n1 = [] # 입력된 시간별 행성의 명칭 모음
  p1 = [] # 입력된 시간별 행성의 식별번호 모음
  q1 = [] # 입력된 시간별 행성의 근일점 모음
  ad1 = [] # 입력된 시간별 행성의 원일점 모음
  a1 = [] # 입력된 시간별 행성의 장반경 모음
  e1 = [] # 입력된 시간별 행성의 이심률 모음
  i1 = [] # 입력된 시간별 행성의 경사각 모음
  om1 = [] # 입력된 시간별 행성의 승교점 경도 모음
  w1 = [] # 입력된 시간별 행성의 근일점 이각 모음
  tp1 = [] # 입력된 시간별 행성의 근일점 통과시각(율리우스력 일) 모음
  moid1 = [] # 입력된 시간별 행성의 지구와의 최소 궤도 교차거리 모음
  per1 = [] # 입력된 시간별 행성의 공전주기(일) 모음
  per_y1 = [] # 입력된 시간별 행성의 공전주기(년) 모음
  t_jup1 = [] # 입력된 시간별 행성의 목성 티세 모음
  pr1 = [] # 입력된 시간별 행성의 주요유형 모음
  dt1 = [] # 입력된 시간별 행성의 세부유형 모음
  neo1 = [] # 입력된 시간별 행성의 근지구형 여부 모음
  pha1 = [] # 입력된 시간별 행성의 지구위험형 여부 모음
  yr1 = [] # 율리우스력으로 입력된 시간을 그레고리력으로 변환한 시각 모음
  r1 = [] # 입력된 시간별 행성과 태양간의 거리 모음
  x1 = [] # 입력된 시간별 행성의 x축 좌표 모음
  y1 = [] # 입력된 시간별 행성의 y축 좌표 모음
  z1 = [] # 입력된 시간별 행성의 z축 좌표 모음
  # 입력된 시간의 시작 시간부터 종료 시간+시간 간격까지 시간 간격별로 반복 시행
  for j in np.arange(start_juliandate, finish_juliandate+timedelta_day, timedelta_day):
    planet_dataframe = planet_orbit_element(j) # 입력된 율리우스력 시간의 태양계 행성 궤도 요소 데이터 프레임
    for s in range(0, len(planet_dataframe), 1): # 행성 개수 만큼 반복 시행
      n = planet_dataframe.loc[s, 'full_name'] # 행성의 명칭
      p = planet_dataframe.loc[s, 'pdes'] # 행성의 식별번호
      q = planet_dataframe.loc[s, 'q'] # 행성의 근일점
      ad = planet_dataframe.loc[s, 'ad'] # 행성의 원일점
      a = planet_dataframe.loc[s, 'a'] # 행성의 장반경(태양과의 거리)(au)
      e = planet_dataframe.loc[s, 'e'] # 행성의 이심률
      i = planet_dataframe.loc[s, 'i'] # 행성의 경사각(황도면을 기준으로 기울어진 각도)(degree)
      om = planet_dataframe.loc[s,'om'] # 행성의 승교점 경도(황위가 -에서 +로 올라가면서 황도면과 교차하는 지점의 황경)(degree)
      w = planet_dataframe.loc[s, 'w'] # 행성의 근일점 이각(승교점에서 근일점까지의 반시계방향(황경이 증가하는 방향의 이각)(degree)
      tp = planet_dataframe.loc[s, 'tp'] # 행성의 근일점 통과시각(율리우스력 일)
      moid = planet_dataframe.loc[s, 'moid'] # 행성의 지구와의 최소 궤도 교차거리
      per = planet_dataframe.loc[s, 'per'] # 행성의 공전주기(일)
      per_y = planet_dataframe.loc[s, 'per_y'] # 행성의 공전주기(년)
      t_jup = planet_dataframe.loc[s, 't_jup'] # 행성의 목성 티세랑
      pr = planet_dataframe.loc[s, 'pr_class'] # 행성의 주요유형
      dt = planet_dataframe.loc[s, 'dt_class'] # 행성의 세부유형
      neo = planet_dataframe.loc[s, 'neo'] # 행성의 근지구형 여부
      pha = planet_dataframe.loc[s, 'pha'] # 행성의 지구위험형 여부
      rp, xp, yp, zp = orbit_point(a, e, i, om, w, tp, per, j)  # orbit_p 함수로 천체의 시간별 궤도 요소 산출
      gregorian = Time(j, format='jd').iso # 율리우스력 날짜를 그레고리력 날짜로 변환
      n1.append(n) # n1 변수에 입력된 시간별 행성의 명칭 붙여넣기
      p1.append(p) # p1 변수에 입력된 시간별 행성의 식별번호 붙여넣기
      q1.append(q) # q1 변수에 입력된 시간별 행성의 근일점 붙여넣기
      ad1.append(ad) # ad1 변수에 입력된 시간별 행성의 원일점 붙여넣기
      a1.append(a) # a1 변수에 입력된 시간별 행성의 장반경 붙여넣기
      e1.append(e) # e1 변수에 입력된 시간별 행성의 이심률 붙여넣기
      i1.append(i) # i1 변수에 입력된 시간별 행성의 경사각 붙여넣기
      om1.append(om) # om1 변수에 입력된 시간별 행성의 승교점 경도 붙여넣기
      w1.append(w) # w1 변수에 입력된 시간별 행성의 근일점 이각 붙여넣기
      tp1.append(tp) # tp1 변수에 입력된 시간별 행성의 근일점 통과시각(율리우스력 일) 붙여넣기
      moid1.append(moid) # moid1 변수에 입력된 지구와의 최소 궤도 교차거리 붙여넣기
      per1.append(per) # per1 변수에 입력된 시간별 행성의 공전주기(일) 붙여넣기
      per_y1.append(per_y) # per_y1 변수에 입력된 시간별 행성의 공전주기(년) 붙여넣기
      t_jup1.append(t_jup) # t_jup1 변수에 입력된 시간별 행성의 목성 티세랑 붙여넣기
      pr1.append(pr) # pr1 변수에 입력된 시간별 행성의 주요유형 붙여넣기
      dt1.append(dt) # dt1 변수에 입력된 시간별 행성의 세부유형 붙여넣기
      neo1.append(neo) # neo1 변수에 입력된 시간별 행성의 근지구형 여부 붙여넣기
      pha1.append(pha) # pha1 변수에 입력된 시간별 행성의 지구위험형 여부 붙여넣기
      yr1.append(gregorian) # yr1변수에 율리우스력으로 입력된 시간을 그레고리력으로 변환한 시각 붙여넣기
      r1.append(rp) # r1변수에 입력된 시간별 행성과 태양간의 거리 붙여넣기
      x1.append(xp) # x1변수에 입력된 시간별 행성의 x축 좌표 붙여넣기
      y1.append(yp) # y1변수에 입력된 시간별 행성의 y축 좌표 붙여넣기
      z1.append(zp) # z1변수에 입력된 시간별 행성의 z축 좌표 붙여넣기
  # 입력된 기간 동안의 행성 궤도 정보에 대한 데이터 세트 생성
  dt_df_p = pd.DataFrame({'full_name':n1, 'pdes':p1, 'q':q1, 'ad':ad1, 'a':a1, 'e':e1, 'i':i1, 'om':om1, 'w':w1,
                          'tp':tp1, 'moid':moid1, 'per':per1, 'per_y':per_y1, 't_jup':t_jup1, 'pr_class':pr1, 'dt_class':dt1,
                          'neo':neo1, 'pha':pha1, 'cal(TDB)':yr1, 'x':x1, 'y':y1, 'z':z1})
  return dt_df_p # 함수 출력값

"""## 7 입력된 시간별 소천체의 궤도 정보 출력 함수"""

# 입력된 시간별 소천체의 궤도 정보 출력 함수
def object_datetimeframe(object_dataframe, start_juliandate, finish_juliandate, timedelta_day):
  # 함수 입력값(시작 시간(단위:율리우스력 일), 종료 시간(단위:율리우스력 일),
  # 시간 간격(단위:율리우스력 일))
  n1 = [] # 입력된 시간별 천체의 명칭 모음
  p1 = [] # 입력된 시간별 천체의 식별번호 모음
  q1 = [] # 입력된 시간별 천체의 근일점 모음
  ad1 = [] # 입력된 시간별 천체의 원일점 모음
  a1 = [] # 입력된 시간별 천체의 장반경 모음
  e1 = [] # 입력된 시간별 천체의 이심률 모음
  i1 = [] # 입력된 시간별 천체의 경사각 모음
  om1 = [] # 입력된 시간별 천체의 승교점 경도 모음
  w1 = [] # 입력된 시간별 천체의 근일점 이각 모음
  tp1 = [] # 입력된 시간별 천체의 근일점 통과시각(율리우스력 일) 모음
  moid1 = [] # 입력된 시간별 천체의 지구와의 최소 궤도 교차거리 모음
  per1 = [] # 입력된 시간별 천체의 공전주기(일) 모음
  per_y1 = [] # 입력된 시간별 천체의 공전주기(년) 모음
  t_jup1 = [] # 입력된 시간별 천체의 목성 티세 모음
  pr1 = [] # 입력된 시간별 천체의 주요유형 모음
  dt1 = [] # 입력된 시간별 천체의 세부유형 모음
  neo1 = [] # 입력된 시간별 천체의 근지구형 여부 모음
  pha1 = [] # 입력된 시간별 천체의 지구위험형 여부 모음
  yr1 = [] # 율리우스력으로 입력된 시간을 그레고리력으로 변환한 시각 모음
  r1 = [] # 입력된 시간별 천체와 태양간의 거리 모음
  x1 = [] # 입력된 시간별 천체의 x축 좌표 모음
  y1 = [] # 입력된 시간별 천체의 y축 좌표 모음
  z1 = [] # 입력된 시간별 천체의 z축 좌표 모음
  # 입력된 시간의 시작 시간부터 종료 시간+시간 간격까지 시간 간격별로 반복 시행
  # 시작 시간(율리우스력), 마지막 시간(율리우스력), 시간 간격(율리우스력)
  for j in np.arange(start_juliandate, finish_juliandate+timedelta_day, timedelta_day):
    for ii in range(0, len(object_dataframe), 1): # 소천체 개수 만큼 반복 시행
      n = object_dataframe.iloc[ii, 0] # 소천체의 명칭
      p = object_dataframe.iloc[ii, 1] # 소천체의 식별번호
      q = object_dataframe.iloc[ii, 2] # 소천체의 식별번호
      ad = object_dataframe.iloc[ii, 3] # 소천체의 식별번호
      a = object_dataframe.iloc[ii, 4] # 소천체의 장반경(태양과의 거리)(au)
      e = object_dataframe.iloc[ii, 5] # 소천체의 이심률
      i = object_dataframe.iloc[ii, 6] # 소천체의 경사각(황도면을 기준으로 기울어진 각도)(degree)
      om = object_dataframe.iloc[ii, 7] # 소천체의 승교점 경도(황위가 -에서 +로 올라가면서 황도면과 교차하는 지점의 황경)(degree)
      w = object_dataframe.iloc[ii, 8] # 소천체의 근일점 이각(승교점에서 근일점까지의 반시계방향(황경이 증가하는 방향의 이각)(degree)
      tp = object_dataframe.iloc[ii, 9] # 소천체의 근일점 통과시각(율리우스일)
      moid = object_dataframe.iloc[ii, 10] # 소천체의 지구와의 최소 궤도 교차거리(au)
      per = object_dataframe.iloc[ii, 11] # 소천체의 공전주기(일)
      per_y = object_dataframe.iloc[ii, 12] # 소천체의 공전주기(년)
      t_jup = object_dataframe.iloc[ii, 13] # 소천체의 목성 티세랑
      pr = object_dataframe.iloc[ii, 14] # 소천체의 주요유형
      dt = object_dataframe.iloc[ii, 15] # 소천체의 세부유형
      neo = object_dataframe.iloc[ii, 16] # 소천체의 근지구형 여부
      pha = object_dataframe.iloc[ii, 17] # 소천체의 지구위험형 여부
      rp, xp, yp, zp = orbit_point(a, e, i, om, w, tp, per, j)  # orbit_p 함수로 소천체의 시간별 궤도 요소 산출
      gregorian = Time(j, format='jd').iso
      n1.append(n) # n1 변수에 입력된 시간별 소천체의 명칭 붙여넣기
      p1.append(p) # p1 변수에 입력된 시간별 소천체의 식별번호 붙여넣기
      q1.append(q) # q1 변수에 입력된 시간별 소천체의 근일점 붙여넣기
      ad1.append(ad) # ad1 변수에 입력된 시간별 소천체의 원일점 붙여넣기
      a1.append(a) # a1 변수에 입력된 시간별 소천체의 장반경 붙여넣기
      e1.append(e) # e1 변수에 입력된 시간별 소천체의 이심률 붙여넣기
      i1.append(i) # i1 변수에 입력된 시간별 소천체의 경사각 붙여넣기
      om1.append(om) # om1 변수에 입력된 시간별 소천체의 승교점 경도 붙여넣기
      w1.append(w) # w1 변수에 입력된 시간별 소천체의 근일점 이각 붙여넣기
      tp1.append(tp) # tp1 변수에 입력된 시간별 소천체의 근일점 통과시각(율리우스력 일) 붙여넣기
      moid1.append(moid) # moid1 변수에 입력된 시간별 소천체의 최소 궤도 교차거리 붙여넣기
      per1.append(per) # per1 변수에 입력된 시간별 소천체의 공전주기(일) 붙여넣기
      per_y1.append(per_y) # per_y1 변수에 입력된 시간별 소천체의 공전주기(년) 붙여넣기
      t_jup1.append(t_jup) # t_jup1 변수에 입력된 시간별 소천체의 목성 티세랑 붙여넣기
      pr1.append(pr) # pr1 변수에 입력된 시간별 소천체의 주요유형 붙여넣기
      dt1.append(dt) # dt1 변수에 입력된 시간별 소천체의 세부유형 붙여넣기
      neo1.append(neo) # neo1 변수에 입력된 시간별 소천체의 근지구형 여부 붙여넣기
      pha1.append(pha) # pha1 변수에 입력된 시간별 소천체의 지구위험형 여부 붙여넣기
      yr1.append(gregorian) # yr1변수에 율리우스력으로 입력된 시간을 그레고리력으로 변환한 시각 붙여넣기
      r1.append(rp) # r1변수에 입력된 시간별 소천체와 태양간의 거리 붙여넣기
      x1.append(xp) # x1변수에 입력된 시간별 소천체의 x축 좌표 붙여넣기
      y1.append(yp) # y1변수에 입력된 시간별 소천체의 y축 좌표 붙여넣기
      z1.append(zp) # z1변수에 입력된 시간별 소천체의 z축 좌표 붙여넣기
  # 입력된 기간 동안의 소천체 궤도 정보에 대한 데이터 프레임 생성
  dt_df_a = pd.DataFrame({'full_name':n1, 'pdes':p1, 'q':q1, 'ad':ad1, 'a':a1, 'e':e1, 'i':i1, 'om':om1, 'w':w1,
                          'tp':tp1, 'moid':moid1, 'per':per1, 'per_y':per_y1, 't_jup':t_jup1, 'pr_class':pr1, 'dt_class':dt1,
                          'neo':neo1, 'pha':pha1, 'cal(TDB)':yr1, 'x':x1, 'y':y1, 'z':z1})
  return dt_df_a # 함수 출력값

# """## 8 행성과 소천체의 탐색 시간과 위치 정보가 담긴 데이터 세트와 위치 정보만 담긴 데이터 세트 출력 함수"""

# # 행성과 소천체의 탐색 시간과 위치 정보가 담긴 데이터 세트와 위치 정보만 담긴 데이터 세트 출력 함수
# def individual_to_dat_df(object_pdes_list, start_time, finish_time, time_hour):
#   # 함수 입력값(천체 식별번호(pdes) 리스트, 탐색 시작 시간(고레고리력), 탐색 종료 시간(그레고리력), 시간 간격(그레고리력, 시간 단위))
#   s_jd = Time(start_time, format='iso', scale='utc').jd # 율리우스력 일로 변환
#   f_jd = Time(finish_time, format='iso', scale='utc').jd # 율리우스력 일로 변환
#   t_d = time_hour/24 # 시간 단위를 일 단위로 변환
#   for pdes in object_pdes_list:
#     df_o = df[ df['pdes'] == pdes ] # df 데이터 세트에서 입력된 소천체의 기본명칭을 갖는 데이터 추출
#     df_o_1 = df_o[df_o.pr_class != 'Satellite'] # 위 데이터 세트에서 주요 유형이 Satellite(위성)가 아닌 데이터만 다시 추출
#     dat_df_o = object_datetimeframe(df_o_1, s_jd, f_jd, t_d) # 입력된 시작 시간, 종료 시간, 시간 간격에 대한 소천체의 시간 데이터 세트 산출
#     dat_df_p = planet_datetimeframe(s_jd, f_jd, t_d) # 입력된 시작 시간, 종료 시간, 시간 간격에 대한 행성의 시간 데이터 세트 산출
#     if pdes == object_pdes_list[0]:
#       dat_df_p_o = dataframe_concatenate(dat_df_p, dat_df_o) # 행성의 시간 데이터 세트와 소천체의 시간 데이터 세트 합치기
#       df_p_o = dataframe_concatenate(df_p, df_o) # 행성의 데이터 세트과 소천체의 데이터 세트 합치기
#     else:
#       dat_df_p_o = dataframe_concatenate(dat_df_p_o, dat_df_o)
#       df_p_o = dataframe_concatenate(df_p_o, df_o)
#   df_p_o_all = df_p_o # 시간 데이터 세트 없이 행성과 분석하고자 하는 천체의 정보가 합쳐진 데이터 세트
#   df_p_o_all_1 = df_p_o_all[df_p_o_all.pr_class != 'Satellite'] # 시간 데이터 세트가 없으며, 위성 정보도 없는 행성과 분석하고자 하는 천체의 정보가 합쳐진 데이터 세트
#   dat_df_p_o_lb_1 = pr_dt_class_labelencoder(dat_df_p_o) # 위성 정보가 없으며, 합쳐진 시간 데이터 세트의 주요유형과 세부유형의 문자형 데이터를 숫자형으로 레이블 변환
#   return dat_df_p_o_lb_1, df_p_o_all_1, df_p_o_all # 함수 출력값

# """## 9 3d 천체 시뮬레이션 출력 함수"""

# 3d 천체 시뮬레이션 출력 함수
# def threed_simulation(dat_df_p_o_lb_1, df_p_o_all_1, text_tf, orbit_tf, nps):
#   # 함수 입력값(시간과 위 좌표 및 레이블이 지정된 데이터 세트, 위치 좌표가 있는 데이터 세트,
#   # 텍스트 표시 여부(None, full_name), 궤도선 표시 유무(True, False), 궤도를 그리는데 필요한 점 개수)
#   # 애니메이션 구동 파라미터
#   colors = px.colors.qualitative.Dark24 # 색깔 지정
#   fig = px.scatter_3d(data_frame = dat_df_p_o_lb_1, # 데이터프레임에 '행성와 개별 소천체의 시간 데이터 세트' 열 대입
#                       x="x", y="y", z='z', # x, y, z 입력값에 'x, y, z축' 열 대입
#                       animation_frame="cal(TDB)", # 애니메이션 구동 기준에 '입력 시간 그레고리력' 열 대입
#                       size='pr_label', # 마커 사이즈에 '주요유형 레이블' 열 대입
#                       size_max=10, # 마커 사이즈 최대 크기 지정
#                       symbol='pr_class', # 마커 기호에 '주요유형 레이블' 열 대입
#                       color='dt_class', # 마커 색깔에 '세부유형 레이블' 열 대입
#                       color_discrete_map={'TP':colors[3], 'JP':colors[4], 'DP':colors[5],
#                                           'APO':colors[6], 'AMO':colors[7], 'ATE':colors[8], 'IEO':colors[9],
#                                           'MBA':colors[10], 'TJN':colors[11], 'TNO':colors[12],
#                                           'Short-period_JFC':colors[13], 'Short-period_HTC':colors[14],'Long-period':colors[15]},
#                                            ### <color='dt_class'일 때, 세부유형별로 매칭된 마커 색깔 지정, 위 색깔 표 참조하여 정수 입력>
#                       hover_name='full_name', # 마우스를 올렸을때 나타나는 이름에 '천체 명칭' 열 대입
#                       hover_data=['pdes', 'q', 'ad', 'a', 'e', 'i', 'om', 'w', 't_jup', 'moid', 'pr_class', 'dt_class', 'neo', 'pha'], # 마우스를 올렸을때 나타나는 데이터 정보에 열 대입
#                       text=text_tf # 그림 위에 항상 표시되는 텍스트 (None: 안보임, 'full_name': 천체명 보임)
#                       )
#   # 태양 파라미터
#   fig.add_trace(go.Scatter3d(x=[0], y=[0], z=[0], # 태양의 x, y, z 좌표 데이터 입력
#                              mode='markers', # 3d 산점도 데이터의 표시 모드 종류 입력
#                              marker=dict(color='orange', size=4), # 마커 색, 크기, 기호 입력
#                              name='Sun' # 표시되는 명칭 입력
#                              )
#                 )
#   ### 아래 천체 궤도 선 파라미터에서 color=prdt_color[dt] 일 때 세부유형별로 매칭되는 색깔 변수 지정
#   prdt_color = {'TP':colors[3], 'JP':colors[4], 'DP':colors[5],
#                 'APO':colors[6], 'AMO':colors[7], 'ATE':colors[8], 'IEO':colors[9],
#                 'MBA':colors[10], 'TJN':colors[11], 'TNO':colors[12],
#                 'Short-period_JFC':colors[13], 'Short-period_HTC':colors[14],'Long-period':colors[15]}
#   # 천체 궤도 파라미터
#   for s in range(len(df_p_o_all_1)):
#     n = df_p_o_all_1.loc[s, 'full_name'] # 천체의 명칭
#     a = df_p_o_all_1.loc[s, 'a'] # 천체의 장반경(태양과의 거리)(au)
#     e = df_p_o_all_1.loc[s, 'e'] # 천체의 이심률
#     i = df_p_o_all_1.loc[s, 'i'] # 천체의 경사각(황도면을 기준으로 기울어진 각도)(degree)
#     om = df_p_o_all_1.loc[s, 'om'] # 천체의 승교점 경도(황위가 -에서 +로 올라가면서 황도면과 교차하는 지점의 황경)(degree)
#     w = df_p_o_all_1.loc[s, 'w'] # 천체의 근일점 이각(승교점에서 근일점까지의 반시계방향(황경이 증가하는 방향의 이각)(degree)
#     pr = df_p_o_all_1.loc[s, 'pr_class'] # 천체의 주요유형
#     dt = df_p_o_all_1.loc[s, 'dt_class'] # 천체의 세부유형
#     neo = df_p_o_all_1.loc[s, 'neo'] # 천체의 근지구형 유무
#     pha = df_p_o_all_1.loc[s, 'pha'] # 천체의 지구위협형 유무
#     r ,x ,y, z = orbit_line(a, e, i, om, w, nps) # 천체 궤도 선 산출 함수로 태양과의 거리, xyz 좌표 산출
#     if orbit_tf == False: # orbit_tf가 False이면 태양계 천체의 궤도 선만 보이기
#       if pr == 'Planet': # 행성 궤도 파라미터
#         fig.add_trace(go.Scatter3d(x=x, y=y, z=z, # 3d 산점도 xyz그래프
#                                    mode='lines',
#                                    line=dict(color=prdt_color[dt], width=2),
#                                    text=(pr+'_'+dt),
#                                    name=n
#                                    )
#                     )
#     elif orbit_tf == True: # orbit_tf가 True이면 모든 천체의 궤도 선 보이기
#       fig.add_trace(go.Scatter3d(x=x, y=y, z=z, # 3d 산점도 xyz그래프
#                                  mode='lines',
#                                  line=dict(color=prdt_color[dt], width=2),
#                                  text=(pr+'_'+dt),
#                                  name=n
#                                  )
#                   )
#   return fig

"""## 10 2d 천체 시뮬레이션 X-Y축 출력 함수"""

# 2d 천체 시뮬레이션 X-Y축 출력 함수
# def twod_simulation_xy(dat_df_p_o_lb_1, df_p_o_all_1, text_tf, nps):
#   # 함수 입력값(시간과 위 좌표 및 레이블이 지정된 데이터 세트 위치 좌표가 있는 데이터 세트,
#   # 텍스트 표시 여부(None, full_name), 궤도를 그리는데 필요한 점 개수)
#   # 애니메이션 구동 파라미터
#   fig = px.scatter(data_frame = dat_df_p_o_lb_1, # 데이터프레임에 '행성와 개별 소천체의 시간 데이터 세트' 열 대입
#                    x="x", y="y", # x, y, z 입력값에 'x, y, z축' 열 대입
#                    animation_frame="cal(TDB)", # 애니메이션 구동 기준에 '입력 시간 그레고리력' 열 대입
#                    size='pr_label', # 마커 사이즈에 '주요유형 레이블' 열 대입
#                    size_max=10, # 마커 사이즈 최대 크기 지정
#                    symbol='pr_class', # 마커 기호에 '주요유형 레이블' 열 대입
#                    color='full_name', # 마커 색깔에 '세부유형 레이블' 열 대입
#                    hover_name='full_name', # 마우스를 올렸을때 나타나는 이름에 '천체 명칭' 열 대입
#                    hover_data=['pdes', 'q', 'ad', 'a', 'e', 'i', 'om', 'w', 't_jup', 'moid', 'pr_class', 'dt_class', 'neo', 'pha'], # 마우스를 올렸을때 나타나는 데이터 정보에 열 대입
#                    text=text_tf # 그림 위에 항상 표시되는 텍스트
#                    )
#   # 태양 파라미터
#   fig.add_trace(go.Scatter(x=[0], y=[0],
#                             mode='markers',
#                             marker=dict(color='orange', size=7),
#                             name='Sun'
#                             )
#                 )
#   df_line_all = df_orbit_line_xyz(df_p_o_all_1, nps)
#   x_max = np.max(np.abs(df_line_all['x']))
#   y_max = np.max(np.abs(df_line_all['y']))
#   xy_max = np.max(np.abs([x_max, y_max]))
#   fig1 = px.line(df_line_all, x='x', y='y', color='full_name',
#                  hover_data=['pdes', 'q', 'ad', 'a', 'e', 'i', 'om', 'w', 't_jup', 'moid', 'pr_class', 'dt_class', 'neo', 'pha'], hover_name='full_name')
#   fig.add_traces(fig1.data)
#   fig.update_xaxes(title_text="x", range=(-(xy_max+5), xy_max+5))
#   fig.update_yaxes(title_text="y", range=(-(xy_max+5), xy_max+5))
#   return fig

"""## 11 2d 천체 시뮬레이션 nps-z축 출력 함수"""

# # 2d 천체 시뮬레이션 nps-z축 출력 함수
# def twod_simulation_npsz(df_p_o_all_1, nps):
#   # 함수 입력값(위치 좌표가 있는 데이터프레임, 궤도를 그리는데 필요한 점 개수)
#   df_line_all = df_orbit_line_xyz(df_p_o_all_1, nps)
#   fig = px.line(df_line_all, x='nps', y='z', color='full_name',
#                 hover_data=['pdes', 'q', 'ad', 'a', 'e', 'i', 'om', 'w', 't_jup', 'moid', 'pr_class', 'dt_class', 'neo', 'pha'], hover_name='full_name')
#   return fig

"""## 12 데이터 프레임들을 행 방향으로 합쳐주는 함수(10개까지 가능)"""

# 데이터 프레임9세트)들을 행 방향으로 합쳐주는 함수(10개까지 가능)
def dataframe_concatenate(dataframe1, dataframe2=None, dataframe3=None, dataframe4=None, dataframe5=None,
                          dataframe6=None, dataframe7=None, dataframe8=None, dataframe9=None, dataframe10=None):
  # 함수 입력값(데이터 프레임 1번째, 데이터 프레임 2번째, 데이터 프레임 3번째, 데이터 프레임 4번째, 데이터 프레임 5번째)
  dfc = pd.concat([dataframe1, dataframe2, dataframe3, dataframe4, dataframe5,
                   dataframe6, dataframe7, dataframe8, dataframe9, dataframe10], axis=0) # 행 방향으로 데이터 프레임 합치기
  dfc.reset_index(drop=True, inplace=True) # 각 데이터 프레임의 기존 인덱스는 모두 초기화
  return dfc # 함수값 출력

"""## 13 데이터 열 중 주요유형과 세부유형의 문자형 데이터를 숫자형 데이터로 레이블 변환해주는 함수"""

# 데이터 열 중 주요유형과 세부유형의 문자형 데이터를 숫자형 데이터로 레이블 변환해주는 함수
def pr_dt_class_labelencoder(object_dataframe):
  # 함수 입력값(데이터 세트)
  le = LabelEncoder() # 레이블 인코더 함수 실행
  pr_lb = le.fit_transform(object_dataframe['pr_class']) # 주요유형의 문자형 데이터를 숫자형으로 레이블 변환
  pr_lb_lg = le.classes_ # 기존의 문자형 데이터가 어떤 숫자형 데이트로 레이블 되었는지 확인
  dt_lb = le.fit_transform(object_dataframe['dt_class']) # 세부유형의 문자형 데이터를 숫자형으로 레이블 변환
  dt_lb_lg = le.classes_ # 기존의 문자형 데이터가 어떤 숫자형 데이트로 레이블 되었는지 확인
  object_dataframe.insert(12, 'pr_label', # 숫자형으로 레이블된 주요유형의 데이터를 12번째 열에 '주요유형_레이블'열 이름과 함께 넣기
                  pr_lb+1)
  object_dataframe.insert(14, 'dt_label', # 숫자형으로 레이블된 세부유형의 데이터를 13번째 열에 '세부유형_레이블'열 이름과 함께 넣기
                  dt_lb)
#   print('주요유형 인코딩 숫자 범례:', object_dataframe['pr_label'].unique(), object_dataframe['pr_class'].unique())
#   print('세부유형 인코딩 숫자 범례:', object_dataframe['dt_label'].unique(), object_dataframe['dt_class'].unique())
  return object_dataframe # 함수값 출력