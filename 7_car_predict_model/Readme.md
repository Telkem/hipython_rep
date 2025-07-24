# 중고차 가격 예측 모델

이 프로젝트는 Dubizzle의 중고차 판매 데이터셋을 활용하여 중고차 가격을 예측하는 머신러닝 모델을 구축하고 평가합니다. 다양한 회귀 모델을 적용하고 성능을 비교하여 최적의 모델을 찾습니다.

## 1. 프로젝트 목표

* 중고차 가격 예측을 위한 데이터 전처리 및 피처 엔지니어링 수행.
* 다양한 회귀 모델(선형 회귀, XGBoost, 릿지, 라쏘, 엘라스틱넷) 학습 및 성능 평가.
* 최적의 예측 모델 도출.

## 2. 데이터셋

* **데이터 출처**: `Dubizzle_used_car_sales.csv`
* **주요 컬럼**:
    * `title`: 차량 제목
    * `price_in_aed`: 가격 (타겟 변수)
    * `kilometers`: 주행 거리
    * `body_condition`: 차체 상태
    * `mechanical_condition`: 기계적 상태
    * `seller_type`: 판매자 유형
    * `body_type`: 차체 유형
    * `no_of_cylinders`: 실린더 개수
    * `transmission_type`: 변속기 유형
    * `regional_specs`: 지역 사양
    * `horsepower`: 마력
    * `fuel_type`: 연료 유형
    * `steering_side`: 운전대 위치
    * `year`: 연식
    * `color`: 색상
    * `emirate`: 지역 (에미리트)
    * `motors_trim`: 트림
    * `company`: 제조사
    * `model`: 모델
    * `date_posted`: 게시일

## 3. 개발 환경

* Python 3.x
* Jupyter Notebook
* 주요 라이브러리:
    * `pandas`: 데이터 처리 및 분석
    * `numpy`: 수치 계산
    * `matplotlib`: 데이터 시각화
    * `scikit-learn`: 머신러닝 모델 및 전처리 도구 (예: `LinearRegression`, `LabelEncoder`, `StandardScaler`, `train_test_split`, `mean_squared_error`, `r2_score`)
    * `xgboost`: XGBoost 모델

## 4. 데이터 전처리

* **결측치 처리**:
    * `no_of_cylinders`: 최빈값으로 대체
    * `motors_trim`: 'unknown'으로 대체
    * `title`: 'unknown'으로 대체
    * `year`: 중앙값으로 대체
* **범주형 데이터 인코딩**: `LabelEncoder`를 사용하여 `object` 타입의 컬럼들을 수치형으로 변환.
* **데이터 분리**: 데이터를 훈련 세트와 테스트 세트로 8:2 비율로 분리.
* **피처 스케일링**: `StandardScaler`를 사용하여 훈련 세트에 맞춰 스케일링 적용.

## 5. 모델 구축 및 평가

다양한 회귀 모델을 사용하여 중고차 가격 예측 모델을 구축하고 RMSE (Root Mean Squared Error), MSE (Mean Squared Error), R2 스코어를 평가했습니다.

* **선형 회귀 (LinearRegression)**:
    * 모델 학습 및 RMSE, MSE, R2 스코어 평가.
    * 회귀 계수를 통해 피처 중요도 분석.
* **다항회귀**:
    * 모델 학습 및 RMSE, MSE, R2 스코어 평가.
* **XGBoost 회귀 (XGBRegressor)**:
    * 모델 학습 및 RMSE, MSE, R2 스코어 평가.
* **정규화 선형 회귀 (Ridge, Lasso, ElasticNet)**:
    * `Ridge`, `Lasso`, `ElasticNet` 모델 학습 및 RMSE, MSE, R2 스코어 평가.

## 6. 결과 요약

주피터 노트북의 마지막 셀에서 다양한 모델의 RMSE와 R2 스코어를 비교한 결과는 다음과 같습니다:

| 모델          | RMSE            | R2             |
| :------------ | :-------------- | :------------- |
| 다항회귀      | 174556.119275   | 0.847005       |
| XGB           | 211608.028652   | 0.775161       |
| 릿지회귀      | 409341.228140   | 0.158646       |
| 라쏘회귀      | 409331.017362   | 0.158688       |
| 엘라스틱넷회귀 | 409776.772824   | 0.156855       |