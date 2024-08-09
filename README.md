# Movie Recommender

## Overview

The Movie Recommender application provides movie recommendations based on a selected movie from a dropdown menu. This project is built using Python, Streamlit, and pickle files for model storage. The recommender system helps users find movies similar to their preferences.

## Getting Started

Follow these steps to run the Movie Recommender application locally:

### Prerequisites

- Python 3.x
- pip (Python package installer)
- Jupyter Notebook
- Streamlit

### Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/movie-recommender.git
cd movie-recommender
```

### Setting up environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
### Running the application 
- Install required packages
- Run Main.ipynb file to generate pickle model
```bash
pip install jupyter streamlit
jupyter notebook main.ipynb
streamlit run main.py
```
- This would run app locally
- select the movie and voila you would get recommended.
