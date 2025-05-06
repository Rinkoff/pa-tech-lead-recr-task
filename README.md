# 🌍 Happiness Data App

This is a web application for visualizing data from the World Happiness Reports. It displays interactive maps, charts, 
and analyses of happiness scores by country and year.

---

## ⚙ Prerequisites

1. **Python 3.10+**
2. **Dependencies:**
   - pandas
   - streamlit
   - plotly
   - base64 
   - etc.

All dependencies are listed in `requirements.txt`.

---

## Configuration: `config.toml`

The `config.toml` file allows you to customize the behavior and appearance of your Streamlit app. By configuring this file, you can control the app's port and theme.

#### Server Settings:
- **`port = 8501`**: Sets the port on which the app will run (default is 8501). You can change this if needed.

#### Theme Settings:
- **`primaryColor`**: Customizes the primary color of your app (e.g., buttons, headers).
- **`backgroundColor`**: Sets the background color of the app.
- **`secondaryBackgroundColor`**: Changes the color of secondary background areas (e.g., sidebar).
- **`textColor`**: Sets the color for the text in your app.
- **`font`**: Defines the font used in your app's interface.

---

## 🛠 How to Run Locally

1️⃣ Clone the repository:  
`git clone Rinkoff/pa-tech-lead-recr-task`  
`cd pa-tech-lead-recr-task`

2️⃣ (Optional) Set up a virtual environment:  
`python -m venv venv`  
`.\venv\Scripts\activate`

3️⃣ Install the dependencies:  
`pip install -r requirements.txt`

4️⃣ Run the app:  
`streamlit run app.py`  

---

## 🐳 Run with Docker

1️⃣ Make sure Docker is installed.

2️⃣ Build the Docker image:  
`docker build -t pa-tech-lead-recr-task .`

3️⃣ Run the container:  
`docker run -p 8501:8501 pa-tech-lead-recr-task`

Then open your browser at:  
[http://localhost:8501](http://localhost:8501)

---

## 🗂 Project Structure
├── .streamlit/
│ └── config.toml
│ └── secrets.toml
├── requirements.txt
├── Dockerfile
├── README.md
├── data/
│ └── (CSV files for each year)
├── utils/
│ └── data_processing.py
│ └── file_helpers.py
├── app.py
└── ...

