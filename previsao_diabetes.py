import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_auc_score

# Carregamento dos Dados
FILE_PATH = 'diabetes.csv'
data = pd.read_csv(FILE_PATH)

# Preparação dos Dados

X = data.drop('Outcome', axis=1)
y = data['Outcome']

# Divisão da base

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Escalonamento dos Dados

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Treinamento (usando KNN)
from sklearn.neighbors import KNeighborsClassifier

k = 3
knn_model = KNeighborsClassifier(n_neighbors=k)
knn_model.fit(X_train_scaled, y_train)

# Previsão
y_pred = knn_model.predict(X_test_scaled)
y_prob = knn_model.predict_proba(X_test_scaled)[:, 1]

# Avaliação do modelo
print("Avaliação do Modelo")
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)
auc_score = roc_auc_score(y_test, y_prob)

print(f"Acurácia: {accuracy:.4f}\n")
print("\nMatriz de Confusão:")
print(conf_matrix)
print("\nRelatório de Classificação:")
print(class_report)
print(f"\nAUC Score: {auc_score:.4f}")
