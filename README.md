# Rice Plant Disease Classification

This project implements a deep learning-based pipeline to classify rice plant images into disease categories, paddy varieties, and plant age groups. It includes data preprocessing, exploratory analysis, model training using ANN, DNN, and CNN architectures, as well as deployment via a FastAPI backend and a Next.js frontend.

## Folder Structure

<pre>
./
├── data/                           # Stores the training and test datasets
│   ├── train_images/               # Training dataset
│   │   ├── bacterial_leaf_blight/
│   │   ├── bacterial_leaf_streak/
│   │   └── ...
│   ├── test_images/                # Test dataset
│   └── meta_train.csv              # Metadata file
├── models/                         # Trained model files
│   ├── disease_classification_model.keras
│   ├── variety_identification_model.keras
│   └── age_prediction_model.keras
├── notebooks/                      # Jupyter notebooks for each task
│   ├── task0_exploratory_data_analysis.ipynb
│   ├── task1_disease_classification.ipynb
│   ├── task2_variety_identification.ipynb
│   └── task3_age_prediction.ipynb
├── prediction/                     # Final prediction
│   └── COSC2753_A2_S1_G7.csv
├── scripts/                        # Standalone scripts for model inference
│   ├── data/
│   ├── preprocessing.py
│   ├── task1_disease_classification.py
│   ├── task2_variety_identification.py
│   └── task3_age_prediction.py
├── client/                         # Frontend (Next.js)
└── server/                         # Backend (FastAPI)
</pre>

## Quick Start

### Prerequisites

- Python version: `3.10`
- Install dependencies using:

```bash
pip install -r requirements.txt
```

- Ensure that the dataset is placed in the correct directory structure (as described above).
- If the dataset is missing, download it from one of the following sources:
  - [RMIT Canvas Assignment](https://rmit.instructure.com/courses/152392/assignments/1059949)
  - [Kaggle Competition Dataset](https://www.kaggle.com/competitions/paddy-disease-classification/data)

---

### Run Notebooks

```bash
cd notebooks/
```

- Run all cells in the following notebooks:
  - `task0_exploratory_data_analysis.ipynb`
  - `task1_disease_classification.ipynb`
  - `task2_variety_identification.ipynb`
  - `task3_age_prediction.ipynb`

---

### Run Python Scripts for Inference

```bash
cd scripts/
```

- Execute the model pipelines with:

```bash
python task1_disease_classification.py  
```

```bash
python task2_variety_identification.py  
```

```bash
python task3_age_prediction.py
```

---

### Web Application

#### Live Demo

- Frontend: https://rice-plant-disease-classification.vercel.app/  
- API Docs: https://rice-plant-disease-classification.k-clowd.top/docs  

#### Run Locally

Backend (FastAPI):

```bash
cd server  
pip install -r requirements.txt  
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

Frontend (Next.js):

```bash
cd client  
npm install  
npm run dev
```
