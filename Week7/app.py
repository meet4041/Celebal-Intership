import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.datasets import load_iris

st.set_page_config(page_title="ML Model Deployment", layout="wide")

@st.cache_resource
def load_model():
    data = load_iris()
    X = pd.DataFrame(data.data, columns=data.feature_names)
    y = pd.Series(data.target, name='target')
    y = y.map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    return model, X_test, y_test, data.feature_names

model, X_test, y_test, feature_names = load_model()

st.title("🌼 Iris Flower Classification Model Deployment")
st.markdown("""
The model predicts iris flower species based on their sepal and petal measurements.
""")

tab1, tab2, tab3 = st.tabs(["Make Prediction", "Model Performance", "Feature Importance"])

with tab1:
    st.header("Make a Prediction")
    
    with st.form("input_form"):
        st.subheader("Enter Flower Measurements")
        col1, col2 = st.columns(2)
        
        with col1:
            sepal_length = st.slider("Sepal Length (cm)", 4.0, 8.0, 5.8)
            sepal_width = st.slider("Sepal Width (cm)", 2.0, 4.5, 3.0)
        
        with col2:
            petal_length = st.slider("Petal Length (cm)", 1.0, 7.0, 3.8)
            petal_width = st.slider("Petal Width (cm)", 0.1, 2.5, 1.2)
        
        submitted = st.form_submit_button("Predict")
    
    if submitted:
        input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
        
        prediction = model.predict(input_data)[0]
        probabilities = model.predict_proba(input_data)[0]
        
        st.subheader("Prediction Result")
        
        if prediction == 'setosa':
            st.success(f"Predicted Species: {prediction} 🌸")
        elif prediction == 'versicolor':
            st.success(f"Predicted Species: {prediction} 🌺")
        else:
            st.success(f"Predicted Species: {prediction} 🌷")
        
        st.write("Prediction Probabilities:")
        prob_df = pd.DataFrame({
            'Species': model.classes_,
            'Probability': probabilities
        }).sort_values('Probability', ascending=False)
        
        fig, ax = plt.subplots()
        sns.barplot(x='Probability', y='Species', data=prob_df, palette='viridis', ax=ax)
        ax.set_title("Class Probabilities")
        st.pyplot(fig)

with tab2:
    st.header("Model Performance Evaluation")
    
    y_pred = model.predict(X_test)
    
    st.subheader("Confusion Matrix")
    cm = confusion_matrix(y_test, y_pred)
    fig, ax = plt.subplots()
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                xticklabels=model.classes_, 
                yticklabels=model.classes_,
                ax=ax)
    ax.set_xlabel("Predicted")
    ax.set_ylabel("Actual")
    st.pyplot(fig)
    
    st.subheader("Classification Report")
    report = classification_report(y_test, y_pred, output_dict=True)
    report_df = pd.DataFrame(report).transpose()
    st.dataframe(report_df.style.background_gradient(cmap='Blues'))

with tab3:
    st.header("Feature Importance Analysis")
    
    st.subheader("Feature Importance Scores")
    importance = model.feature_importances_
    importance_df = pd.DataFrame({
        'Feature': feature_names,
        'Importance': importance
    }).sort_values('Importance', ascending=False)
    
    st.dataframe(importance_df.style.background_gradient(cmap='Greens'))
    
    st.subheader("Feature Importance Plot")
    fig, ax = plt.subplots()
    sns.barplot(x='Importance', y='Feature', data=importance_df, palette='viridis', ax=ax)
    ax.set_title("Feature Importance")
    st.pyplot(fig)
    
    st.subheader("Feature Relationships")
    iris = load_iris()
    iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
    iris_df['species'] = iris.target
    iris_df['species'] = iris_df['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})
    
    fig = sns.pairplot(iris_df, hue='species', palette='viridis')
    st.pyplot(fig)