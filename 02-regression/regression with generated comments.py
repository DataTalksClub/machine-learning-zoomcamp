# 🚗 CAR PRICE PREDICTION MODEL — EXPLAINED LIKE YOU'RE 10 🍭
# Every comment tells you: WHAT, WHY, WHAT IF YOU SKIP, and WHAT THE RESULT MEANS!

# Import necessary libraries — our toolbox!
import pandas as pd          # Like a super notebook for data — rows and columns!
import numpy as np           # Math helper — does fast calculations on big lists of numbers
import matplotlib.pyplot as plt  # Drawing tool — makes graphs and charts
import seaborn as sns        # Fancy drawing tool — makes prettier graphs
from sklearn.linear_model import LinearRegression  # Smart robot that learns patterns from numbers
from sklearn.metrics import mean_squared_error     # Robot’s report card — tells us how wrong it was
import warnings              # Hides scary-looking (but harmless) messages
warnings.filterwarnings('ignore')

# Set matplotlib style for better visualizations — makes graphs cute and clean!
plt.style.use('seaborn-v0_8')

# 📂 STEP 1: LOAD THE DATA — Open the car notebook!
print("Loading car data...")
df = pd.read_csv('car_data.csv')  # Load data from file — like opening your toy box
print(f"Dataset loaded with {df.shape[0]} rows and {df.shape[1]} columns")
# 🧒 WHY? We need data to teach the robot! Each row = one car, each column = a fact (price, color, etc.)
# ⚠️ SKIP? No data = no learning. Robot sits idle.
# 📊 RESULT: If it says 10,000 rows — that’s 10,000 cars to learn from!

# 👀 STEP 2: LOOK AT THE DATA — Peek inside the toy box!
print("\nFirst 5 rows of the dataset:")
print(df.head())  # Show first 5 cars — like flipping first pages of a book

print("\nDataset info:")
print(df.info())  # Tells us which columns are text/numbers, and if any are empty

print("\nDescriptive statistics:")
print(df.describe())  # Gives averages, min/max — e.g., “average car price is $30,000”

print("\nMissing values per column:")
print(df.isnull().sum())  # Counts holes in data — like missing LEGO pieces
# 🧒 WHY? Robot gets confused by missing or weird data. We check for traps!
# ⚠️ SKIP? Robot might learn nonsense — e.g., “if price is missing, guess $0!”
# 📊 RESULT: Big number in “engine_hp”? We’ll need to fix that later.

# 🕵️ STEP 3: VISUALIZE MISSING VALUES — Draw the holes!
try:
    import missingno as msno
    print("\nVisualizing missing values...")

    msno.matrix(df)  # Shows missing data as white gaps — like holes in Swiss cheese!
    plt.title("Missing Values Matrix")
    plt.show()

    msno.bar(df)     # Bar chart — taller bar = more complete data
    plt.title("Missing Values Bar Chart")
    plt.show()

    msno.heatmap(df) # Shows if missingness in one column relates to another
    plt.title("Missingness Correlation Heatmap")
    plt.show()

    msno.dendrogram(df) # Groups columns by how similarly they’re missing
    plt.title("Missingness Dendrogram")
    plt.show()
except ImportError:
    print("Missingno library not available. Skipping missing value visualizations.")
# 🧒 WHY? Pictures help us see patterns — maybe all electric cars are missing “gas mileage”?
# ⚠️ SKIP? We might miss BIG problems — like “convertible” cars missing “roof type”!
# 📊 RESULT: White gaps = missing data. Clusters = related missingness — fix together!

# 🧩 STEP 4: SPLIT DATA — Homework, Quiz, Final Exam!
print("\nSetting up validation framework...")
n = len(df)
n_val = int(0.2 * n)   # 20% → validation (quiz)
n_test = int(0.2 * n)  # 20% → test (final exam)
n_train = n - n_val - n_test  # 60% → training (homework)

print(f"Training set size: {n_train}")
print(f"Validation set size: {n_val}")
print(f"Test set size: {n_test}")

# Shuffle data — mix up the cars so robot doesn’t cheat!
print("\nShuffling data...")
np.random.seed(2)  # Same shuffle every time — like using same dice
idx = np.arange(n)
np.random.shuffle(idx)

df_shuffled = df.iloc[idx]
df_val = df_shuffled.iloc[:n_val]         # First 20% → quiz
df_test = df_shuffled.iloc[n_val:n_val+n_test]  # Next 20% → final exam
df_train = df_shuffled.iloc[n_val+n_test:]      # Last 60% → homework

# Reset index so no confusion later
df_train = df_train.reset_index(drop=True)
df_val = df_val.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)

print("Data split completed.")
# 🧒 WHY? Robot must learn on homework, get graded on quiz, and take secret final exam!
# ⚠️ SKIP? Robot memorizes answers → fails in real world. Like cheating on test!
# 📊 RESULT: Train=learn, Val=tweak, Test=TRUE score. Never touch Test until the end!

# 🎨 STEP 5: CLEAN TEXT — Make it robot-friendly!
print("Cleaning string columns...")
string_columns = df.select_dtypes(include=['object']).columns
for col in string_columns:
    # Turn "Red Car" → "red_car" so robot doesn’t think “Red” ≠ “red”
    df[col] = df[col].str.lower().str.replace(" ", "_")
    df_train[col] = df_train[col].str.lower().str.replace(" ", "_")
    df_val[col] = df_val[col].str.lower().str.replace(" ", "_")
    df_test[col] = df_test[col].str.lower().str.replace(" ", "_")

print("String columns cleaned.")
# 🧒 WHY? Robot thinks “TOYOTA”, “Toyota”, “toyota” are 3 different brands! We make them same.
# ⚠️ SKIP? Robot splits data wrong → bad learning. “toyota” gets ignored, “TOYOTA” gets all attention.
# 📊 RESULT: All text is lowercase with underscores — clean and consistent!

# 📈 STEP 6: LOOK AT PRICE — Is it fair or crazy?
print("\nVisualizing price distribution...")
plt.figure(figsize=(10, 6))
sns.histplot(df.msrp[df.msrp < 100000], bins=50)  # Ignore super expensive cars for now
plt.title('Distribution of Car Prices (MSRP)')
plt.xlabel('Price ($)')
plt.ylabel('Count')
plt.show()
# 🧒 WHY? Most cars are $20K–$50K, but Ferraris are $500K! Robot gets distracted by rare cars.
# ⚠️ SKIP? Robot cares too much about Lambos → fails on normal cars.
# 📊 RESULT: Long tail to the right = skewed. Needs fixing!

# 📐 STEP 7: LOG-TRANSFORM PRICE — Squish the rich cars!
print("\nApplying log1p transformation to price...")
price_log = np.log1p(df.msrp)  # log1p(x) = log(1+x) — safe even if price=0!
print("First 5 log-transformed prices:")
print(price_log.head())

plt.figure(figsize=(10, 6))
sns.histplot(price_log, bins=50)
plt.title('Distribution of Log-Transformed Car Prices')
plt.xlabel('Log(1 + Price)')
plt.ylabel('Count')
plt.show()
# 🧒 WHY? Turns $1, $10, $100, $1000 → 0, 1, 2, 3. Squishes rich cars next to normal ones!
# ⚠️ SKIP? Robot obsessed with outliers → bad predictions for regular cars.
# 📊 RESULT: Bell curve! Robot’s favorite shape. Errors now balanced.

# 🎯 STEP 8: PREPARE TARGET (Y) — What we want to predict!
print("\nPreparing target variables...")
y_train = np.log1p(df_train.msrp.values)  # Log-price for training cars
y_val = np.log1p(df_val.msrp.values)
y_test = np.log1p(df_test.msrp.values)

# REMOVE PRICE FROM FEATURES — no peeking at answers!
del df_train['msrp']
del df_val['msrp']
del df_test['msrp']

print("Target variables prepared.")
# 🧒 WHY? Robot must guess price — not copy it! Like hiding answer key during test.
# ⚠️ SKIP? Robot sees price → 100% accurate but USELESS. Like cheating.
# 📊 RESULT: y_train = list of correct answers robot must learn to guess.

# 🧱 STEP 9: PICK FEATURES — What clues help guess price?
base_features = ['engine_hp', 'engine_cylinders', 'highway_mpg', 'city_mpg', 'popularity']
print(f"\nBase features: {base_features}")

categorical_vars = ['make', 'engine_fuel_type', 'transmission_type', 'driven_wheels', 
                   'market_category', 'vehicle_size', 'vehicle_style']
print(f"Categorical variables: {categorical_vars}")

# Get top 5 most common categories — avoid rare ones that confuse robot!
print("\nIdentifying most frequent categories...")
categories = {}
for var in categorical_vars:
    categories[var] = list(df[var].value_counts().head().index)
    print(f"{var}: {categories[var]}")

popular_makes = list(df.make.value_counts().head().index)
print(f"Most popular makes: {popular_makes}")
# 🧒 WHY? Robot only understands numbers. “Toyota” → becomes a 1/0 switch. Only top 5 to avoid clutter.
# ⚠️ SKIP? Too many categories → robot overfits. “Cars with ‘x’ in name cost more?!” — nonsense!
# 📊 RESULT: “make_toyota” = 1 if Toyota, 0 otherwise. Robot learns brand effect.

# 🧮 STEP 10: PREPARE FEATURES (X) — Build robot’s LEGO set!
def prepare_X(df_input):
    """
    🧒 WHY? Robot needs clean numbered blocks to play with.
    We add age, door switches, brand switches, fill holes with 0.
    ⚠️ SKIP? Robot crashes on missing values or text.
    📊 RESULT: X = big table of numbers — robot food!
    """
    df_copy = df_input.copy()
    features = base_features.copy()  # Start with engine, mpg, etc.

    # Add car age — older cars usually cheaper!
    df_copy['age'] = 2017 - df_copy.year
    features.append('age')

    # Add door switches — is it 2-door? 4-door?
    for num_doors in [2, 3, 4]:
        df_copy[f'num_doors_{num_doors}'] = (df_copy.number_of_doors == num_doors).astype('int')
        features.append(f'num_doors_{num_doors}')

    # Add brand switches — is it Toyota? Ford?
    for make in popular_makes:
        df_copy[f'make_{make}'] = (df_copy.make == make).astype('int')
        features.append(f'make_{make}')

    # Add category switches — automatic? AWD? SUV?
    for cat_var, cat_values in categories.items():
        for value in cat_values:
            df_copy[f'{cat_var}_{value}'] = (df_copy[cat_var] == value).astype('int')
            features.append(f'{cat_var}_{value}')

    # Keep only prepared features
    df_numeric = df_copy[features]

    # Fill holes with 0 — “if we don’t know, assume average”
    df_numeric = df_numeric.fillna(0)

    # Give robot the LEGO set!
    X = df_numeric.values
    return X

# 🤖 STEP 11: TRAIN ROBOT — Find best guessing rules!
def train_linear_regression(X, y):
    """
    🧒 WHY? Robot learns: price = w0 + w1*HP + w2*is_Toyota + ...
    We calculate best w’s using math magic (matrix inversion).
    ⚠️ SKIP? No model = no predictions. Just guessing!
    📊 RESULT: w0 = base price. w[0] = how much HP adds to price.
    """
    ones = np.ones(X.shape[0])
    X = np.column_stack([ones, X])  # Add column for w0 (intercept)

    XTX = X.T.dot(X)        # Robot’s “memory matrix”
    XTX_inv = np.linalg.inv(XTX)  # Solve the puzzle!
    w_full = XTX_inv.dot(X.T).dot(y)  # Best weights ever!

    w0 = w_full[0]  # Base price (if all features=0)
    w = w_full[1:]  # How much each feature changes price
    return w0, w

# 📏 STEP 12: SCORE ROBOT — How wrong is it?
def rmse(y_true, y_pred):
    """
    🧒 WHY? Robot’s report card. Lower = better.
    Measures average mistake in log-price units.
    ⚠️ SKIP? We wouldn’t know if robot is good or bad.
    📊 RESULT: RMSE=0.3 → e^0.3≈1.35 → robot off by ~35% in real dollars.
    """
    error = y_true - y_pred
    se = error ** 2
    mse = se.mean()
    return np.sqrt(mse)

# 🎯 STEP 13: TRAIN & SCORE BASE MODEL — Homework grade!
print("\nTraining linear regression model...")
X_train = prepare_X(df_train)
w0, w = train_linear_regression(X_train, y_train)

X_val = prepare_X(df_val)
y_pred = w0 + X_val.dot(w)

val_rmse = rmse(y_val, y_pred)
print(f"Validation RMSE: {val_rmse:.6f}")
# 🧒 WHY? Teach on homework, grade on quiz.
# ⚠️ SKIP? No idea if robot learned anything.
# 📊 RESULT: ~0.5 = okay, ~0.2 = great! We’ll try to improve.

# 🎨 STEP 14: PLOT PREDICTIONS — Are dots near the line?
plt.figure(figsize=(10, 6))
plt.scatter(y_val, y_pred, alpha=0.5)
plt.plot([y_val.min(), y_val.max()], [y_val.min(), y_val.max()], 'r--', lw=2)
plt.xlabel('Actual Log Price')
plt.ylabel('Predicted Log Price')
plt.title('Predictions vs Actual Values (Validation Set)')
plt.show()
# 🧒 WHY? Picture > numbers. Dots on line = good! Cloud = bad.
# ⚠️ SKIP? Might miss bias — robot always guesses low.
# 📊 RESULT: Look for patterns — hard to predict luxury cars?

# 🔄 STEP 15: ADD TRAINING WHEELS — Regularization!
def train_linear_regression_reg(X, y, r=0.001):
    """
    🧒 WHY? Sometimes robot memorizes noise (“cars with ‘z’ cost more!”).
    Regularization says: “Don’t trust any one feature too much!”
    ⚠️ SKIP? Robot overfits — perfect on homework, fails on quiz.
    📊 RESULT: Small r = gentle. Big r = robot ignores features. Find sweet spot!
    """
    ones = np.ones(X.shape[0])
    X = np.column_stack([ones, X])

    XTX = X.T.dot(X)
    reg = r * np.eye(XTX.shape[0])  # Penalty matrix
    reg[0, 0] = 0  # Don’t penalize base price

    XTX = XTX + reg  # Add penalty
    XTX_inv = np.linalg.inv(XTX)
    w_full = XTX_inv.dot(X.T).dot(y)

    w0 = w_full[0]
    w = w_full[1:]
    return w0, w

# 🔍 STEP 16: FIND BEST TRAINING WHEELS — Tune r!
print("\nFinding optimal regularization parameter...")
r_values = [0, 0.000001, 0.0001, 0.001, 0.01, 0.1, 1, 5, 10]
rmse_scores = []

for r in r_values:
    X_train_reg = prepare_X(df_train)
    w0_reg, w_reg = train_linear_regression_reg(X_train_reg, y_train, r=r)

    X_val_reg = prepare_X(df_val)
    y_pred_reg = w0_reg + X_val_reg.dot(w_reg)

    score = rmse(y_val, y_pred_reg)
    rmse_scores.append(score)
    print(f"r={r}: RMSE={score:.6f}")

# Plot RMSE vs r — find the valley!
plt.figure(figsize=(10, 6))
plt.plot(r_values, rmse_scores, 'bo-')
plt.xscale('log')
plt.xlabel('Regularization Parameter (r)')
plt.ylabel('RMSE')
plt.title('RMSE vs Regularization Parameter')
plt.grid(True, alpha=0.3)
plt.show()
# 🧒 WHY? Test different tightness of training wheels.
# ⚠️ SKIP? Might use too much or too little → robot underfits or overfits.
# 📊 RESULT: Lowest point = best r. Usually 0.001–0.1.

# 🏁 STEP 17: FINAL MODEL & TEST SET — FINAL EXAM!
best_idx = np.argmin(rmse_scores)
best_r = r_values[best_idx]
best_rmse = rmse_scores[best_idx]

print(f"\nBest regularization parameter: r={best_r}")
print(f"Best RMSE: {best_rmse:.6f}")

print("\nTraining final model with optimal regularization...")
X_train_final = prepare_X(df_train)
w0_final, w_final = train_linear_regression_reg(X_train_final, y_train, r=best_r)

X_val_final = prepare_X(df_val)
y_pred_final = w0_final + X_val_final.dot(w_final)
final_rmse = rmse(y_val, y_pred_final)
print(f"Final model RMSE (validation): {final_rmse:.6f}")

# 🧪 TEST ON SECRET TEST SET — TRUE SCORE!
print("\nEvaluating final model on test set...")
X_test = prepare_X(df_test)
y_pred_test = w0_final + X_test.dot(w_final)
test_rmse = rmse(y_test, y_pred_test)
print(f"TEST RMSE (final exam!): {test_rmse:.6f}")
# 🧒 WHY? Final exam — never touched during training. TRUE measure of skill.
# ⚠️ SKIP? We’d be lying to ourselves. Like grading your own test.
# 📊 RESULT: Should be close to validation RMSE. Much worse? Overfit. Better? Lucky (or bug 😉).

# 💰 STEP 18: PREDICT NEW CARS — Magic 8-ball for prices!
def predict_car_price(car_features, w0=w0_final, w=w_final):
    """
    🧒 WHY? Now YOU can ask: “How much is this car?”
    ⚠️ SKIP? All that work for nothing — no real use!
    📊 RESULT: Robot says $28,500? Check real listings. Close? Robot is smart!
    """
    if isinstance(car_features, dict):
        car_df = pd.DataFrame([car_features])
    else:
        car_df = car_features.copy()

    X_car = prepare_X(car_df)           # Build LEGO set for this car
    y_pred_log = w0 + X_car.dot(w)      # Robot’s guess (log scale)
    predicted_price = np.expm1(y_pred_log)  # Convert back to real dollars!

    return predicted_price

# 🚗 EXAMPLE: Predict price for a specific car!
print("\nExample prediction for a specific car:")
example_car = {
    'make': 'chevrolet',
    'model': 'trailblazer_ext',
    'year': 2004,
    'engine_fuel_type': 'regular_unleaded',
    'engine_hp': 275.0,
    'engine_cylinders': 6.0,
    'transmission_type': 'automatic',
    'driven_wheels': 'rear_wheel_drive',
    'number_of_doors': 4.0,
    'market_category': 'crossover',
    'vehicle_size': 'large',
    'vehicle_style': '4dr_suv',
    'highway_mpg': 18,
    'city_mpg': 13,
    'popularity': 1385
}

predicted_price = predict_car_price(example_car)
print(f"Predicted price: ${predicted_price:,.0f}")

# ✅ CONGRATS! You built a car price wizard! 🧙‍♂️🚗💸
# Remember:
# - Clean data → happy robot
# - Split data → honest robot
# - Regularize → wise robot
# - Test set → true robot score
# Now go predict some cars!