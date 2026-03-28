## Property Price Predictor

A small machine-learning demo that trains a linear regression model to estimate property prices from a CSV dataset and exposes a simple interactive runner to make predictions.

### What this repo contains

- `dataset.csv` - training data (CSV). Must contain the columns described below.
- `model-trainer.py` - trains a scikit-learn pipeline (preprocessing + LinearRegression) and saves the model to `price-predictor.pkl`.
- `main.py` - interactive script that loads `price-predictor.pkl` and asks for property details to produce a price estimate.
- `price-predictor.pkl` - serialized trained model (created by `model-trainer.py`).

### Requirements

- Python 3.8 or newer
- pip packages:
  - pandas
  - scikit-learn

Install dependencies (PowerShell):

```powershell
python -m pip install --upgrade pip
python -m pip install pandas scikit-learn
```

### Dataset / CSV format

The training CSV must include these columns (header names expected by `model-trainer.py`):

- `BHK` (numeric)
- `Area` (numeric; carpet area in sqft)
- `Is_Resale` (0 or 1)
- `Bathrooms` (numeric)
- `Location` (categorical)
- `Floor` (categorical)
- `Furnishing` (categorical)
- `Price` (numeric target column)

Example header row (CSV):

```csv
BHK,Area,Is_Resale,Bathrooms,Location,Floor,Furnishing,Price
2,850,0,2,New Delhi,3rd Floor,Unfurnished,4500000
```

### How to train the model

Run the trainer script from the project root. This will read `dataset.csv`, fit a pipeline (numeric passthrough + one-hot encoding for categorical columns) and a `LinearRegression` model, then write `price-predictor.pkl`.

```powershell
python model-trainer.py
```

After success you should see `price-predictor.pkl` in the project folder.

### How to predict (run the app)

Make sure `price-predictor.pkl` exists (run the trainer first if it doesn't). Run the interactive script:

```powershell
python main.py
```

The script will prompt for carpet area, number of bedrooms, bathrooms, location, furnishing, floor and whether the property is a resale. It prints an estimated price (INR).

Sample interaction (user input in parentheses):

```
Enter Carpet Area in sqft:   (900)
Enter number of Bedrooms : (2)
Enter number of Bathrooms:(2)
Enter City/Location where you want to buy: (Mumbai)
Furnishing details (e.g. furnished/unfurnished): (Furnished)
Floor detail (e.g. 1st floor, 2nd floor): (4th Floor)
🔄 Is it a Resale? (y/n): (n)

ESTIMATED PROPERTY VALUE: ₹4,250,000.00
```

### Notes & assumptions

- `model-trainer.py` expects `dataset.csv` in the same directory and a `Price` column as the regression target.
- Categorical columns are one-hot encoded; unseen categories at prediction time are ignored by the encoder (`handle_unknown='ignore'`).
- The project uses `pickle` to serialize the scikit-learn pipeline; avoid loading pickles from untrusted sources.

### Troubleshooting

- If `main.py` prints "Error: Could not find the model. Run model-trainer.py first!" -> run `python model-trainer.py` to create `price-predictor.pkl`.
- If training fails due to missing columns in `dataset.csv`, verify the header names and required columns (see "Dataset / CSV format").
- If you see scikit-learn compatibility errors, try upgrading/downgrading `scikit-learn` to a compatible version (>=0.24 recommended).

### Improvements / Next steps

- Add input validation and clearer CLI arguments (e.g., support `--predict` with JSON input).
- Add unit tests and a small CI workflow.
- Switch to joblib for model serialization or provide a versioned model artifact.

### License

This repository does not include a formal license file. Add a suitable license if you plan to publish or share the code.

---

If you'd like, I can also add a `requirements.txt` or make the prediction script accept command-line arguments for non-interactive use.
