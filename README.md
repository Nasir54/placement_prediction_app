# Placement Prediction App 🎯

A machine learning web application that predicts student placement chances using Perceptron algorithm.

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)

## 🌟 Features

- 🤖 ML-powered predictions using Perceptron algorithm
- 🌐 Beautiful Streamlit web interface
- 🐳 Docker containerization for easy deployment
- 📊 Interactive input forms with real-time validation
- 🎯 Instant placement probability predictions
- 📱 Responsive design works on desktop and mobile

## 🚀 Quick Start

### Prerequisites
- Docker installed on your system
- Git for cloning the repository

### Installation & Running

```bash
# Clone the repository
git clone https://github.com/Nasir54/placement_prediction_app.git
cd placement_prediction_app

# Build and run with Docker
docker build -t placement-app .
docker run -p 8501:8501 placement-app
Visit http://localhost:8501 in your browser to use the app!
📖 Usage
Open the application at http://localhost:8501

Enter student details:

CGPA (0.0 to 10.0)

IQ score (0 to 200)

Click "Predict" button

View results:

🎉 Green success message for high placement chance

❌ Red message for low placement chance
🏗️ Project Structure
placement_prediction_app/
├── data/                   # Dataset folder
│   └── placement.csv       # Student placement dataset
├── notebooks/              # Jupyter notebooks
│   └── perceptron_project1.ipynb  # Model experimentation
├── src/                    # Source code
│   ├── __init__.py         # Package initialization
│   └── perceptron_model.py # Model training and utilities
├── model/                  # Trained models
│   ├── model.joblib        # Trained Perceptron model
│   └── scaler.joblib       # Feature scaler
├── tests/                  # Test cases
│   └── test_model.py       # Model tests
├── .streamlit/             # Streamlit configuration
│   └── config.toml         # App settings
├── app_streamlit.py        # Main Streamlit application
├── Dockerfile              # Docker build instructions
├── requirements.txt        # Python dependencies
├── .gitignore             # Git ignore rules
└── README.md              # Project documentation
🛠️ Technologies Used
Python 3.8+ - Core programming language

Streamlit - Web application framework

Docker - Containerization and deployment

Scikit-learn - Machine learning library (Perceptron)

Pandas - Data manipulation and analysis

NumPy - Numerical computations

Joblib - Model serialization

Jupyter Notebook - Model experimentation
📊 Dataset
The model is trained on student placement data with the following features:

Feature	Description	Range	Type
CGPA	Cumulative Grade Point Average	0.0 - 10.0	Numerical
IQ	Intelligence Quotient score	0 - 200	Numerical
placement	Target variable (1=placed, 0=not placed)	Binary	Categorical
Dataset Characteristics:

100 samples

Balanced classes (50 placed, 50 not placed)

Clean data with no missing values
🎯 Model Details
Algorithm: Perceptron (Linear classifier)

Accuracy: ~85% (on test data)

Input Features: CGPA and IQ scores

Output: Binary prediction (0 = not placed, 1 = placed)

Preprocessing: StandardScaler for feature normalization

Train-Test Split: 80-20 split with random_state=42
🤝 Contributing
Contributions are welcome! Here's how you can contribute:

Fork the repository

Create a feature branch (git checkout -b feature/amazing-feature)

Commit your changes (git commit -m 'Add amazing feature')

Push to the branch (git push origin feature/amazing-feature)

Open a Pull Request

Please ensure your code follows PEP8 guidelines and includes appropriate tests.
📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

The MIT License is permissive and allows others to use your code freely, which is great for open-source projects.

👨‍💻 Author
Nasir

GitHub: @Nasir54

Project Repository: placement_prediction_app

🙏 Acknowledgments
Dataset sourced from educational research

Built for learning machine learning deployment

Inspired by real-world placement prediction systems

Thanks to the open-source community for amazing tools

⭐ If you find this project useful, please give it a star on GitHub!
EOF
