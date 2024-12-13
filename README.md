## 🎭 Personality Test Web Application
Welcome to the Personality Test Web App! 🚀 This is a fun, interactive, and insightful platform to explore personality types while integrating cutting-edge tech like Flask, Google Cloud SQL, and analytics with Looker Studio. Follow this guide to run the app locally, contribute, or deploy it in the cloud!

### ✨ Features
📝 Interactive Personality Test
🌍 Track Ethnic Diversity and Personality Insights
📊 Analytics Dashboard using Looker Studio
🌐 Deployed on Google Cloud Run with CI/CD automation

### 📂 Getting Started
Clone the Repository
Start by cloning this repository to your local machine:

git clone https://github.com/Datartic/personality_test.git \n
cd personality_test

### 💻 Run Locally
Install Dependencies
Ensure you have Python installed (version 3.9+ recommended). Then, install the required libraries:

pip install -r requirements.txt

Update the code with your creds
DB_USER=your_database_user
DB_PASS=your_database_password
INSTANCE_CONNECTION_NAME=your_instance_connection_name

### Run the Flask App
Fire up the application:

python app.py
Open your browser and navigate to http://127.0.0.1:5000.

### ☁️ Deploy on Google Cloud
1. Install Google Cloud SDK
Follow this guide to install the Google Cloud SDK for your OS. Authenticate and set your project:
gcloud auth login
gcloud config set project [PROJECT_ID]
2. Configure Cloud SQL
Create a MySQL instance in Google Cloud SQL.
Use the provided schema in the README to set up your database.
3. Deploy Using Google Cloud Build
The CI/CD pipeline automates the deployment:

Link your repository with Google Cloud Build.
Add a build trigger to deploy on every git push.
Review the cloudbuild.yaml file for details.
📊 Analytics Integration
Use Looker Studio to create and visualize ethnicity and personality insights:

Connect Looker Studio to the Cloud SQL database.
Build your dashboards and embed them in the application.
👩‍💻 Contributing
Want to improve the app? Awesome! Here's how you can contribute:

Fork this repository.
Create a new branch:
git checkout -b feature-idea
Make your changes and commit:
git commit -m "Add amazing feature"
Push your branch:
git push origin feature-idea
Open a pull request!
🎉 Have Fun Building and Exploring!
Dive into the world of tech with this project and discover how personality types vary across diverse ethnicities. Happy coding!