Movie Recommendation System
This project is a web-based movie recommendation system that suggests movies to users based on a movie they input. The frontend is built with HTML, Tailwind CSS, and JavaScript, while the backend is powered by a Python Flask server that uses a content-based filtering model built with scikit-learn.

Features
Clean UI: A modern, user-friendly interface for getting movie recommendations.

Autocomplete Search: Helps users find movies that are in the dataset.

Real-time Recommendations: Fetches and displays recommendations dynamically.

Content-Based Filtering: Recommends movies based on genres, keywords, cast, and crew.

Prerequisites
Before you begin, ensure you have the following installed on your system:

Python 3.8+

Git

Git LFS (for handling large model files)

Setup and Installation
Follow these steps to get the project running on your local machine.

1. Clone the Repository

First, clone the repository to your local machine.

git clone https://github.com/gauravit131/movie-recommendation-system.git
cd movie-recommendation-system

2. Install Git LFS and Pull Large Files

This project uses Git LFS to manage the large model files (.pkl).

# Install Git LFS (if you haven't already)
git lfs install

# Pull the large files from the LFS storage
git lfs pull

3. Create and Activate a Virtual Environment

It is highly recommended to use a virtual environment to manage project dependencies.

# Create a virtual environment
python -m venv venv

# Activate the environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

4. Install Dependencies

Install all the required Python packages using the requirements.txt file.

pip install -r requirements.txt

You will also need to download a data package for the NLTK library. Run the following commands in your terminal:

python -c "import nltk; nltk.download('punkt')"

5. Run the Application

You are now ready to start the Flask server.

python app.py

How to Use
Once the server is running, you will see output in your terminal indicating it's running on http://127.0.0.1:5000.

Open your web browser.

Navigate to http://127.0.0.1:5000.

Start typing a movie title in the input field.

Select a movie and click "Get Recommendations" to see the results.