from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report


def run_model(df, model_type='RandomForest'):
    X = df.drop(columns=['label'], errors='ignore')
    y = df.get('label')
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    models = {
        'RandomForest': RandomForestClassifier(),
        'SVM': SVC(),
        'XGBoost': XGBClassifier(use_label_encoder=False, eval_metric='logloss')
    }
    model = models[model_type]
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    return {
        'accuracy': accuracy_score(y_test, preds),
        'report': classification_report(y_test, preds, output_dict=True)
    }
