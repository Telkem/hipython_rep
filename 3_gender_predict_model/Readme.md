## 🚀 고객 구매 데이터 기반 성별 예측 모델링 📊

---

### 📝 프로젝트 개요

본 프로젝트는 백화점 고객의 1년 간 구매 데이터를 활용하여 성별 예측 모델을 개발하는 머신러닝 실습입니다. 총 3,500명의 고객에 대한 학습 데이터(X.csv, y.csv)를 사용하여 분류 모델을 구축하고 성능을 측정합니다.

---

### 🎯 실습 프로세스

1.  **데이터 불러오기**: 주어진 고객 구매 데이터를 로드합니다.
2.  **데이터 탐색**: 데이터의 구조와 특성을 이해하기 위한 탐색적 데이터 분석을 수행합니다.
3.  **데이터 전처리**: 머신러닝 모델 학습에 적합한 형태로 데이터를 전처리합니다.
4.  **학습/테스트 데이터 분리**: 모델 학습과 평가를 위해 데이터를 분리합니다.
5.  **모델 선택 및 학습**: 다양한 분류 모델을 선택하고 학습을 진행합니다.
6.  **예측 및 평가**: 학습된 모델의 성능을 예측하고 평가합니다.

---

### 🛠️ 사용 라이브러리

* `numpy`
* `pandas`
* `matplotlib.pyplot`
* `sklearn.preprocessing.LabelEncoder`
* `sklearn.preprocessing.StandardScaler`
* `sklearn.model_selection.train_test_split`
* `sklearn.linear_model.LogisticRegression`
* `sklearn.tree.DecisionTreeClassifier`
* `sklearn.ensemble.RandomForestClassifier`
* `xgboost.XGBClassifier`
* `sklearn.metrics.accuracy_score`
* `sklearn.model_selection.GridSearchCV`

---

### 💾 데이터

* **데이터 출처**: 한국데이터산업진흥원 빅데이터분석기사 실기 공개 예시 문항
* **파일**:
    * `X.csv`: 독립 변수 데이터셋 (고객 구매 기록)
    * `y.csv`: 종속 변수 데이터셋 (고객 성별)
* **인코딩 방식**: `euc-kr`

---

### ⚙️ 데이터 전처리 주요 내용

* `cust_id` 컬럼 제거: 단순히 부여된 숫자형 ID로 인해 발생할 수 있는 데이터 왜곡 방지.
* 결측치 처리: `환불금액` (refund amount) 컬럼의 결측치(NaN)를 0으로 대체.
* **범주형 데이터 인코딩**: `주구매상품` (main purchase item) 및 `주구매지점` (main purchase branch)과 같은 문자형 범주 데이터를 `LabelEncoder`를 사용하여 수치형으로 변환.
* **데이터 스케일링**: `StandardScaler`를 사용하여 데이터의 평균을 0, 표준편차를 1로 표준화하여 정규 분포 형태로 변환.

---

### 📊 모델링 및 평가

본 프로젝트에서는 **Logistic Regression**, **Decision Tree**, **Random Forest**, **XGBoost** 등 다양한 분류 모델을 사용하여 성별을 예측했습니다.

특히, 독립 변수(X값)로 **'주구매상품', '주구매지점', '주말방문비율', '구매주기'** 만을 사용하여 모델을 학습하고 평가했습니다.

**XGBoost 모델 최적화**:
`GridSearchCV`를 사용하여 XGBoost 모델의 최적 파라미터를 탐색했습니다.
* **최적 파라미터**: `{'max_depth': 1, 'min_samples_split': 2}`
* **최고 성능 (정확도)**: 0.6614
