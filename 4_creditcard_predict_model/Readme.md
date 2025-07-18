## 🚀 신용카드 사기 거래 예측 모델링 (분류 문제) 💳

---

### 📝 프로젝트 개요

본 프로젝트는 2013년 9월 유럽 카드 소지자들의 신용카드 거래 내역 데이터를 활용하여 사기 거래를 예측하는 머신러닝 분류 모델을 개발하는 실습입니다. 총 284,807건의 거래 데이터(`creditcard.csv`)를 사용하여 사기 거래 예측 모형을 구축하고, 모델의 성능을 평가합니다.

---

### 🎯 실습 프로세스

1.  **라이브러리 불러오기**: 필요한 Python 라이브러리들을 임포트합니다.
2.  **데이터 불러오기**: 신용카드 거래 데이터를 로드합니다.
3.  **데이터 탐색**: 데이터의 구조, 특징, 결측치 및 통계적 특성을 파악하여 데이터를 이해합니다.
4.  **데이터 전처리**: 모델 학습에 적합하도록 데이터를 가공합니다.
5.  **학습/테스트 데이터 분리**: 모델 학습과 평가를 위해 데이터를 분할합니다.
6.  **모델 선택 및 학습**: 다양한 분류 모델을 선택하고 데이터를 학습시킵니다.
7.  **예측 및 평가**: 학습된 모델의 성능을 예측하고 `정확도(accuracy)`, `혼동 행렬(confusion matrix)`, `분류 보고서(classification report)` 등을 통해 평가합니다.

---

### 🛠️ 사용 라이브러리

* `numpy`
* `pandas`
* `matplotlib.pyplot`
* `warnings`
* `sklearn.preprocessing.LabelEncoder`
* `sklearn.preprocessing.StandardScaler`
* `sklearn.model_selection.train_test_split`
* `sklearn.linear_model.LogisticRegression`
* `sklearn.metrics.accuracy_score`
* `sklearn.metrics.classification_report`
* `sklearn.metrics.confusion_matrix`
* `sklearn.tree.DecisionTreeClassifier`
* `sklearn.model_selection.GridSearchCV`
* `sklearn.ensemble.RandomForestClassifier`
* `xgboost`
* `xgboost.XGBClassifier`

---

### 💾 데이터

* **데이터 출처**: [Kaggle - Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud?resource=download)
* **파일**: `creditcard.csv`
* **데이터셋 구성**:
    * **총 거래 건수**: 284,807건
    * **컬럼**: `Time`, `V1` ~ `V28` (PCA 변환된 익명화된 특징), `Amount`, `Class`
    * **타겟 변수**: `Class` (0: 정상 거래, 1: 사기 거래)
    * **특징**: 대부분의 특징(`V1` ~ `V28`)은 PCA 변환되어 익명화된 수치형 데이터입니다. `Time`은 각 거래가 발생한 시간(초), `Amount`는 거래 금액입니다.
* **데이터 불균형**: `Class` 변수의 통계에서 사기 거래(1)의 비율이 매우 낮아, **심각한 데이터 불균형** 문제를 가지고 있습니다 (약 0.17%만이 사기 거래). 이는 모델 학습 시 특별한 고려가 필요함을 시사합니다.

---

### ⚙️ 데이터 전처리 주요 내용

* **`Time` 및 `Amount` 스케일링**: `StandardScaler`를 사용하여 `Time`과 `Amount` 컬럼을 표준화합니다. 이는 각 특징이 모델에 동등하게 기여하도록 돕습니다.
* **결측치 처리**: `df.info()` 결과에 따르면 모든 컬럼에 결측치가 없습니다.

---

### 📊 모델링 및 평가

본 프로젝트에서는 **Logistic Regression**, **Decision Tree**, **Random Forest**, **XGBoost** 등 다양한 분류 모델을 사용하여 사기 거래를 예측했습니다.

* **정확도(Accuracy)**: 0.999596...
* **혼동 행렬(Confusion Matrix)**:
    ```
    [[56860     4]
     [   20    78]]
    ```
    * **True Negative (TN)**: 56860 (실제 정상, 예측 정상)
    * **False Positive (FP)**: 4 (실제 정상, 예측 사기) - **Type I Error**
    * **False Negative (FN)**: 20 (실제 사기, 예측 정상) - **Type II Error**
    * **True Positive (TP)**: 78 (실제 사기, 예측 사기)
* **분류 보고서(Classification Report)**:
    ```
                  precision    recall  f1-score   support

           0       1.00      1.00      1.00     56864
           1       0.95      0.80      0.87        98

    accuracy                           1.00     56962
   macro avg       0.97      0.90      0.93     56962
   weighted avg       1.00      1.00      1.00     56962
    ```
    * **정상 거래 (Class 0)**: 매우 높은 정밀도, 재현율, F1-점수를 보입니다.
    * **사기 거래 (Class 1)**: 상대적으로 낮은 재현율(Recall)을 보이지만, 높은 정밀도(Precision)를 유지합니다. 사기 거래와 같이 **불균형한 데이터셋**에서는 정확도보다는 **정밀도, 재현율, F1-점수**와 같은 지표를 종합적으로 고려하는 것이 중요합니다. 특히, 사기 거래 예측에서는 **재현율(실제 사기 거래를 얼마나 잘 감지하는가)**이 매우 중요합니다.

---
