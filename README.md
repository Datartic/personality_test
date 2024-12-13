## 🎭 Personality Test Web Application
Welcome to the Personality Test Web App! 🚀 This is a fun, interactive, and insightful platform to explore personality types while integrating cutting-edge tech like Flask, Google Cloud SQL, and analytics with Looker Studio. Follow this guide to run the app locally, contribute, or deploy it in the cloud! <br /><br />

### ✨ Features
📝 Interactive Personality Test <br />
🌍 Track Ethnic Diversity and Personality Insights <br />
📊 Analytics Dashboard using Looker Studio <br />
🌐 Deployed on Google Cloud Run with CI/CD automation <br />

### 📂 Getting Started
Clone the Repository <br />
Start by cloning this repository to your local machine:
git clone https://github.com/Datartic/personality_test.git <br />
cd personality_test<br />

### 💻 Run Locally  
Install Dependencies  
Ensure you have Python installed (version 3.9+ recommended). Then, install the required libraries:<br />

pip install -r requirements.txt<br />

Update the code with your creds<br />
DB_USER=your_database_user<br />
DB_PASS=your_database_password<br />
INSTANCE_CONNECTION_NAME=your_instance_connection_name<br />

### Run the Flask App
Fire up the application:<br />
python app.py<br />
Open your browser and navigate to http://127.0.0.1:5000.<br />

### Deploy on Google Cloud
1. Install Google Cloud SDK<br />
Follow this guide to install the Google Cloud SDK for your OS. Authenticate and set your project: <br />
gcloud auth login <br />
gcloud config set project [PROJECT_ID] <br />
2. Configure Cloud SQL<br />
Create a MySQL instance in Google Cloud SQL.<br />
Use the provided schema in the README to set up your database.<br />
3. Deploy Using Google Cloud Build <br />
The CI/CD pipeline automates the deployment:<br />

Link your repository with Google Cloud Build.<br />
Add a build trigger to deploy on every git push.<br />
Review the cloudbuild.yaml file for details.<br />
📊 Analytics Integration<br />
Use Looker Studio to create and visualize ethnicity and personality insights:<br />

Connect Looker Studio to the Cloud SQL database.<br />
Build your dashboards and embed them in the application.<br />
👩‍💻 Contributing<br />
Want to improve the app? Awesome! Here's how you can contribute:<br />

Fork this repository.<br />
Create a new branch:<br />
git checkout -b feature-idea<br />
Make your changes and commit:<br />
git commit -m "Add amazing feature"<br />
Push your branch:<br />
git push origin feature-idea<br />
Open a pull request!<br />
🎉 Have Fun Building and Exploring!<br />
Dive into the world of tech with this project and discover how personality types vary <br />across diverse ethnicities. Happy coding!<br />