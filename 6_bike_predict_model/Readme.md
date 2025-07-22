# 자전거 대여량 예측 모델

이 프로젝트는 Kaggle의 [Bike Sharing Demand](https://www.kaggle.com/c/bike-sharing-demand/data) 데이터셋을 활용하여 자전거 대여량을 예측하는 머신러닝 모델을 구축하고 평가합니다. 다양한 회귀 모델을 적용하고 성능을 비교하여 최적의 모델을 찾습니다.

## 1. 프로젝트 목표

* 자전거 대여량 예측을 위한 데이터 전처리 및 피처 엔지니어링 수행.
* 다양한 회귀 모델(선형 회귀, 랜덤 포레스트, XGBoost, 릿지, 라쏘, 엘라스틱넷) 학습 및 성능 평가.
* 최적의 예측 모델 도출.

## 2. 데이터셋

* **데이터 출처**: Kaggle Bike Sharing Demand (train.csv)
* **주요 컬럼**:
    * `datetime`: 시간 정보 (년, 월, 일, 시 추출)
    * `season`: 계절 (1: 봄, 2: 여름, 3: 가을, 4: 겨울)
    * `holiday`: 공휴일 여부
    * `workingday`: 근무일 여부
    * `weather`: 날씨 (1: 맑음, 2: 약간 흐림, 3: 가벼운 눈/비, 4: 폭우/폭설)
    * `temp`: 실제 온도
    * `atemp`: 체감 온도
    * `humidity`: 습도
    * `windspeed`: 풍속
    * `casual`: 비등록 사용자 대여량
    * `registered`: 등록 사용자 대여량
    * `count`: 총 대여량 (타겟 변수)

## 3. 개발 환경

* Python 3.x
* Jupyter Notebook
* 주요 라이브러리:
    * `pandas`: 데이터 처리 및 분석
    * `numpy`: 수치 계산
    * `scikit-learn`: 머신러닝 모델 및 전처리 도구
        * `LinearRegression`, `RandomForestRegressor`, `GradientBoostingRegressor`, `Ridge`, `Lasso`, `ElasticNet`
        * `train_test_split`, `StandardScaler`, `PolynomialFeatures`, `Pipeline`, `cross_val_score`
    * `xgboost`: XGBoost 모델
    * `matplotlib`: 데이터 시각화

## 4. 프로젝트 구조
.
├── 39_bike대여량예측모델 - 테스트.ipynb  # Jupyter Notebook 파일
└── data1/
    └── bike-sharing-demand/
        └── train.csv                 # 원본 데이터 파일

## 5. 분석 및 모델링 과정

1.  **라이브러리 임포트**: 필요한 모든 라이브러리 로드.
2.  **데이터 로드 및 초기 탐색**: `train.csv` 파일을 로드하고 `df.head()`, `df.info()`를 통해 데이터 구조 및 결측치 확인.
3.  **피처 엔지니어링**:
    * `datetime` 컬럼을 `datetime` 객체로 변환 후 `year`, `month`, `day`, `hour` 피처 추출.
    * `datetime`, `casual`, `registered` 컬럼 제거 (`count`와 중복되거나 직접 사용하지 않음).
4.  **데이터 분리 및 스케일링**:
    * `count`를 타겟 변수(`y`)로, 나머지를 피처(`X`)로 분리.
    * 훈련 세트와 테스트 세트를 8:2 비율로 분리 (`random_state=50`).
    * `StandardScaler`를 사용하여 피처 스케일링.
5.  **모델 학습 및 평가**:
    * **선형 회귀 (Linear Regression)**:
        * 기본 선형 회귀 모델 학습 및 RMSE, MSE, R2 스코어 평가.
        * 피처 중요도 분석 (회귀 계수).
        * 일부 피처(`workingday`, `holiday`, `weather`, `day`)를 제외하고 모델 재학습 및 성능 재평가.
        * 교차 검증을 통한 성능 평가.
    * **랜덤 포레스트 회귀 (RandomForestRegressor)**:
        * `max_depth=8`로 설정하여 모델 학습 및 RMSE, MSE, R2 스코어 평가.
        * 교차 검증을 통한 성능 평가.
    * **다항 특성 + 선형 회귀 (PolynomialFeatures + LinearRegression)**:
        * `Pipeline`을 사용하여 1차부터 5차까지의 다항 특성을 추가한 선형 회귀 모델 학습.
        * 각 차수별 RMSE, MSE, R2 스코어 비교.
    * **다항 특성 + 랜덤 포레스트 회귀 (PolynomialFeatures + RandomForestRegressor)**:
        * `Pipeline`을 사용하여 1차부터 5차까지의 다항 특성을 추가한 랜덤 포레스트 회귀 모델 학습.
        * 각 차수별 RMSE, MSE, R2 스코어 비교 및 최적 모델 선정.
    * **그레디언트 부스팅 회귀 (GradientBoostingRegressor)**:
        * 모델 학습 및 RMSE, MSE, R2 스코어 평가.
    * **XGBoost 회귀 (XGBRegressor)**:
        * `n_estimators=400`, `learning_rate=0.1`, `max_depth=3`로 설정하여 모델 학습.
        * `early_stopping_rounds`를 사용하여 과적합 방지.
        * RMSE, MSE, R2 스코어 평가.
    * **정규화 선형 회귀 (Ridge, Lasso, ElasticNet)**:
        * `Ridge`, `Lasso`, `ElasticNet` 모델 학습 및 RMSE, MSE, R2 스코어 평가.
        * `RidgeCV`, `LassoCV`를 사용하여 최적의 `alpha` 값 탐색.
        * 각 모델의 회귀 계수 확인.
6.  **모델 성능 비교**: 최종적으로 모든 모델의 RMSE와 R2 스코어를 비교하여 가장 성능이 좋은 모델을 식별합니다.

## 6. 결과 요약

주피터 노트북의 마지막 셀에서 다양한 모델의 RMSE와 R2 스코어를 비교한 결과는 다음과 같습니다:

| 모델         | RMSE        | R2         |
| :----------- | :---------- | :--------- |
| 다항회귀     | 89.190835   | 0.755830   |
| XGB          | 88.262752   | 0.760885   |
| 릿지회귀     | 141.246722  | 0.387638   |
| 라쏘회귀     | 141.245023  | 0.387652   |
| 엘라스틱넷회귀 | 141.396270  | 0.386340   |

**XGBoost 모델이 RMSE가 가장 낮고 R2 스코어가 가장 높아 자전거 대여량 예측에 가장 우수한 성능을 보였습니다.** 다항회귀 모델도 비교적 좋은 성능을 나타냈습니다. 반면, 릿지, 라쏘, 엘라스틱넷과 같은 기본 선형 회귀 기반의 정규화 모델들은 상대적으로 낮은 성능을 보였습니다.

## 7. 실행 방법

1.  이 저장소를 클론합니다.
    ```bash
    git clone [저장소_URL]
    cd [저장소_폴더]
    ```
2.  `data1/bike-sharing-demand/` 경로에 `train.csv` 파일을 다운로드하여 저장합니다. (Kaggle에서 직접 다운로드 필요)
3.  필요한 라이브러리를 설치합니다.
    ```bash
    pip install pandas numpy scikit-learn matplotlib xgboost
    ```
4.  Jupyter Notebook을 실행합니다.
    ```bash
    jupyter notebook
    ```
5.  `39_bike대여량예측모델 - 테스트.ipynb` 파일을 열고 순서대로 셀을 실행합니다.