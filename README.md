## Credibility Verification System
This project focuses on text-based classification, specifically in the domain of fact-checking statements. The dataset comprises statements paired with verdicts, where the verdicts are binary labels indicating the statements' truthfulness. The goal is to develop and evaluate machine learning models for automating the classification of statements as either true or false.

The project involves tasks such as data preprocessing, exploratory data analysis, feature engineering, and the implementation of various machine learning algorithms. Natural Language Processing (NLP) techniques are employed to extract meaningful features from the textual data. Additionally, statistical tests, including chi-square analysis, are performed to explore relationships between categorical variables.

The evaluation metrics, such as accuracy, precision, recall, and F1 score, are employed to assess the performance of the models. The project provides insights into the efficiency of different algorithms in handling the fact-checking task and aims to contribute to the field of automated content verification.

model_and_analysis.ipynb:

This notebook encompasses the entire data science pipeline, starting with data exploration and preprocessing, followed by model creation and analysis. The steps involved are:

Data Loading and Exploration: The dataset, containing statements and their corresponding verdicts, is loaded and explored to gain insights into the data distribution, null values, and key statistics.
Data Preprocessing: The textual data undergoes preprocessing steps such as text cleaning, handling missing values, and transforming categorical labels into numerical representations suitable for machine learning models.
Exploratory Data Analysis (EDA): Comprehensive EDA is conducted to understand the distribution of verdicts, uncover patterns, and identify potential features. Visualizations are used to illustrate key findings.
Feature Engineering: Relevant features are engineered, especially focusing on extracting meaningful information from the textual statements using techniques like TF-IDF and word embeddings.
Model Building: Various machine learning algorithms are employed to build classification models. This includes traditional algorithms such as Logistic Regression and SVM, as well as ensemble methods made up of Random Forest, svm and Logistic Regression . Model performance metrics are computed, and models are fine-tuned accordingly.
NLP_model.ipynb:

This notebook is dedicated to the creation of a Natural Language Processing (NLP) model using GloVe embeddings. The main highlights include:

Data Preparation: The notebook commences with the loading of the combined dataset, containing statements and corresponding verdicts (True or False). Data exploration and preprocessing steps, including cleaning and handling missing values, are performed to ensure a reliable dataset.
Text Preprocessing: Textual data undergoes preprocessing steps, such as denoising and tokenization, to prepare it for embedding.
GloVe Embeddings: Pre-trained GloVe embeddings are employed to impart a semantic understanding to the words in the dataset. An embedding matrix is constructed, incorporating the pre-trained word vectors.
LSTM Model Architecture: The core of the notebook revolves around the implementation of a Long Short-Term Memory (LSTM) neural network. The model architecture consists of an embedding layer initialized with GloVe embeddings, an LSTM layer for sequential context capture, and dense layers with regularization for effective training.
Training and Evaluation: The model is trained using the prepared dataset, and its performance is evaluated on a separate test set. Metrics such as accuracy are employed to gauge the model's effectiveness.
Results and Visualizations: Key results, including accuracy scores and visualizations depicting the model's training and testing performance over epochs, are presented.
Further Considerations: The notebook provides insights into potential adjustments, such as varying the number of epochs and fine-tuning hyperparameters, to enhance model performance.
By separating the tasks into these two notebooks, the project maintains a clear and organized structure, allowing for a focused exploration of both traditional machine learning approaches and advanced NLP techniques using GloVe embeddings

### Deployment with Django Framework

#### verview
After developing and evaluating the machine learning models for fact-checking statements, the next step was to deploy the model using the Django framework. Django provides a robust environment for building web applications, making it an ideal choice for deploying machine learning models into production.

#### Steps for Deployment
- Integration with Django Project: The trained machine learning model was integrated into a Django project. This involved creating appropriate directories and files within the Django project structure to accommodate the model files and associated code.
- Model Serialization: Before deploying the model, it was serialized using libraries like pickle or joblib. Serialization converts the model into a format that can be easily stored and loaded. This step ensures that the model can be retrieved and used within the Django application.
- Web Interface Development: A user-friendly web interface was developed using Django's built-in functionalities. The interface allows users to input statements for fact-checking and receive the corresponding verdict (true or false) based on the deployed machine learning model.
- Request Handling: Django's views were utilized to handle incoming requests from the web interface. When a user submits a statement for fact-checking, Django processes the input, passes it to the deployed model, and returns the verdict to the user.

### Conclusion
Deploying the machine learning model using the Django framework enables easy access and utilization of the fact-checking functionality. B
