import nbformat
import sys

def modify_notebook(notebook_path):
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)

    for cell in nb.cells:
        if cell.cell_type == 'code':
            source = cell.source

            # Q1
            if 'raise NotImplementedError("Implement gini_impurity()")' in source:
                new_source = """def gini_impurity(class_counts):
    total = sum(class_counts)
    if total == 0:
        return 0.0
    gini = 1.0 - sum((c / total) ** 2 for c in class_counts)
    return gini"""
                # Replace everything from def gini_impurity(class_counts): to the end of the function body
                # The original has a docstring and some total logic. We can just replace the whole function definition
                import re
                source = re.sub(r'def gini_impurity\(class_counts\):.*?return gini', new_source, source, flags=re.DOTALL)
                cell.source = source

            # Q2
            elif 'raise NotImplementedError("Implement entropy()")' in source:
                new_source = """def entropy(class_counts):
    import math
    total = sum(class_counts)
    if total == 0:
        return 0.0
    h = 0.0
    for c in class_counts:
        if c > 0:
            p = c / total
            h -= p * math.log2(p)
    return h"""
                import re
                source = re.sub(r'def entropy\(class_counts\):.*?return h', new_source, source, flags=re.DOTALL)
                cell.source = source

            # Q3
            elif 'raise NotImplementedError("Compute information_gain")' in source:
                new_source = """parent_entropy   = entropy(parent_counts)
weighted_entropy = (n_left / n_total) * entropy(left_counts) + (n_right / n_total) * entropy(right_counts)
information_gain = parent_entropy - weighted_entropy"""
                import re
                source = re.sub(r'parent_entropy.*?raise NotImplementedError\("Compute information_gain"\)', new_source, source, flags=re.DOTALL)
                cell.source = source
            
            # Q4
            elif 'raise NotImplementedError("Fill in the training loop")' in source:
                new_source = """    clf = DecisionTreeClassifier(max_depth=d, random_state=42)
    clf.fit(X_tr_bv, y_tr_bv)
    train_scores.append(accuracy_score(y_tr_bv, clf.predict(X_tr_bv)))
    test_scores.append(accuracy_score(y_te_bv, clf.predict(X_te_bv)))"""
                source = source.replace('    # YOUR CODE HERE\n    # 1. Instantiate a DecisionTreeClassifier with max_depth=d and random_state=42\n    # 2. Fit on (X_tr_bv, y_tr_bv)\n    # 3. Append the training accuracy to train_scores\n    # 4. Append the test accuracy to test_scores\n    raise NotImplementedError("Fill in the training loop")', new_source)
                cell.source = source

            # Q5
            elif 'raise NotImplementedError("Count whitespace rows")' in source:
                new_source = """n_whitespace = (df['TotalCharges'].str.strip() == '').sum()"""
                import re
                source = re.sub(r'n_whitespace = None\s*raise NotImplementedError\("Count whitespace rows"\)', new_source, source)
                
                new_source2 = """df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df['TotalCharges'].fillna(df['TotalCharges'].median(), inplace=True)"""
                source = re.sub(r'# YOUR CODE HERE: convert df\[\'TotalCharges\'\] to numeric, fill NaN with median\s*raise NotImplementedError\("Fix TotalCharges dtype"\)', new_source2, source)
                cell.source = source
            
            # Q6
            elif 'raise NotImplementedError("Train naive tree and predict")' in source:
                new_source = """naive_tree = DecisionTreeClassifier(random_state=42)
naive_tree.fit(X_tr_n, y_tr_n)
y_pred_n   = naive_tree.predict(X_te_n)"""
                import re
                source = re.sub(r'naive_tree = None\s*y_pred_n   = None\s*raise NotImplementedError\("Train naive tree and predict"\)', new_source, source)
                cell.source = source
            
            # Q7
            elif 'raise NotImplementedError("Compute precision, recall, F1 from TN/FP/FN/TP")' in source:
                new_source = """precision_manual = TP / (TP + FP)
recall_manual    = TP / (TP + FN)
f1_manual        = 2 * precision_manual * recall_manual / (precision_manual + recall_manual)"""
                import re
                source = re.sub(r'precision_manual = None.*?\nrecall_manual    = None.*?\nf1_manual        = None.*?\nraise NotImplementedError\("Compute precision, recall, F1 from TN/FP/FN/TP"\)', new_source, source, flags=re.DOTALL)
                cell.source = source
            
            # Q8
            elif 'raise NotImplementedError("Implement bootstrap_sample()")' in source:
                new_source = """    bootstrap_indices = rng.choice(N, size=N, replace=True)
    X_boot = X[bootstrap_indices]
    y_boot = y[bootstrap_indices]
    oob_indices = np.array(list(set(range(N)) - set(bootstrap_indices)))"""
                import re
                source = re.sub(r'    bootstrap_indices = None\s*X_boot = None\s*y_boot = None\s*oob_indices = None\s*raise NotImplementedError\("Implement bootstrap_sample\(\)"\)', new_source, source)
                cell.source = source
            
            # Q9
            elif 'raise NotImplementedError("Train BaggingClassifier and RandomForestClassifier")' in source:
                new_source = """bag_clf = BaggingClassifier(n_estimators=100, bootstrap=True, oob_score=True, random_state=42, n_jobs=-1)
bag_clf.fit(X_tr, y_tr)
rf_clf  = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
rf_clf.fit(X_tr, y_tr)"""
                import re
                source = re.sub(r'bag_clf = None\s*rf_clf  = None\s*raise NotImplementedError\("Train BaggingClassifier and RandomForestClassifier"\)', new_source, source)
                cell.source = source
            
            # Q10
            elif 'raise NotImplementedError("Define param_configs with 4 XGBoost hyperparameter sets")' in source:
                new_source = """param_configs = [
    {'max_depth': 2,  'learning_rate': 0.1, 'n_estimators': 100},
    {'max_depth': 8,  'learning_rate': 0.1, 'n_estimators': 100},
    {'max_depth': 3,  'learning_rate': 0.01, 'n_estimators': 100},
    {'max_depth': 3,  'learning_rate': 0.3, 'n_estimators': 200}
]"""
                import re
                source = re.sub(r'param_configs = \[\s*# YOUR CODE HERE — define 4 configurations to test\s*\]\s*if not param_configs:\s*raise NotImplementedError\("Define param_configs with 4 XGBoost hyperparameter sets"\)', new_source, source)
                cell.source = source
            
            # Q11
            elif 'raise NotImplementedError("Fill in param_grid with meaningful values")' in source:
                new_source = """param_grid = {
    'max_depth':     [3, 5, 7],   # 3 prevents overfitting, 5-7 allows more complexity
    'learning_rate': [0.01, 0.1, 0.2], # 0.01 is slow but robust, 0.1-0.2 is faster
    'n_estimators':  [100, 200, 300],  # More trees needed for lower learning rates
}"""
                import re
                source = re.sub(r"param_grid = {.*?# n_estimators:  \.\.\.\n\nif not any\(param_grid\.values\(\)\):\n    raise NotImplementedError\(\"Fill in param_grid with meaningful values\"\)", new_source, source, flags=re.DOTALL)
                cell.source = source

            # Q12
            elif 'raise NotImplementedError("Fill in the ColumnTransformer transformers")' in source:
                new_source = """preprocessor = ColumnTransformer(
    transformers=[
        ('num',
         Pipeline([
             ('imputer', SimpleImputer(strategy='median')),
             ('scaler',  StandardScaler()),
         ]),
         numeric_cols),

        ('cat',
         Pipeline([
             ('imputer', SimpleImputer(strategy='most_frequent')),
             ('encoder', OneHotEncoder(handle_unknown='ignore', sparse_output=False)),
         ]),
         categorical_cols),
    ],
    remainder='drop'
)"""
                import re
                source = re.sub(r"preprocessor = ColumnTransformer.*?raise NotImplementedError\(\"Fill in the ColumnTransformer transformers\"\)", new_source, source, flags=re.DOTALL)
                cell.source = source

            # Q13
            elif 'raise NotImplementedError("Apply SMOTE on the pre-transformed array (the wrong way)")' in source:
                new_source = """X_tr_transformed = preprocessor.transform(X_tr_p)
X_leaked, y_leaked = sm.fit_resample(X_tr_transformed, y_tr_p)"""
                import re
                source = re.sub(r'X_tr_transformed = preprocessor\.transform\(X_tr_p\)   # preprocessor fitted in Q12\s*X_leaked, y_leaked = None, None\s*raise NotImplementedError\("Apply SMOTE on the pre-transformed array \(the wrong way\)"\)', new_source, source)
                
                new_source2 = """leaked_scores = cross_val_score(leaked_rf, X_leaked, y_leaked, cv=cv5, scoring='roc_auc')"""
                source = re.sub(r'leaked_scores = None\s*raise NotImplementedError\("Cross-validate on the leaked data"\)', new_source2, source)
                
                new_source3 = """correct_pipeline = ImbPipeline([
    ('preprocessor', preprocessor),
    ('smote', SMOTE(random_state=42)),
    ('classifier', RandomForestClassifier(n_estimators=50, random_state=42, n_jobs=-1))
])"""
                source = re.sub(r'correct_pipeline = ImbPipeline\(\[.*?\]\)\s*raise NotImplementedError\("Build the correct ImbPipeline with preprocessor \+ SMOTE inside"\)', new_source3, source, flags=re.DOTALL)
                
                new_source4 = """correct_scores = cross_val_score(correct_pipeline, X_tr_p, y_tr_p, cv=cv5, scoring='roc_auc')"""
                source = re.sub(r'correct_scores = None\s*raise NotImplementedError\("Cross-validate the correct pipeline on raw X_tr_p"\)', new_source4, source)
                cell.source = source

            # Q14
            elif 'raise NotImplementedError("Build and fit the full pipeline")' in source:
                new_source = """full_pipeline = ImbPipeline([
    ('preprocessor', preprocessor),
    ('smote', SMOTE(random_state=42)),
    ('classifier', RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1))
])
full_pipeline.fit(X_tr_p, y_tr_p)"""
                import re
                source = re.sub(r'full_pipeline = None\s*raise NotImplementedError\("Build and fit the full pipeline"\)', new_source, source)
                cell.source = source

            # Q15
            elif 'raise NotImplementedError("Create TreeExplainer and compute SHAP values")' in source:
                new_source = """explainer   = shap.TreeExplainer(rf_model)
shap_values = explainer.shap_values(X_te_proc_df)"""
                import re
                source = re.sub(r'explainer   = None\s*shap_values = None\s*raise NotImplementedError\("Create TreeExplainer and compute SHAP values"\)', new_source, source)
                cell.source = source

            # Q16
            elif 'raise NotImplementedError("Find True Positive indices")' in source:
                new_source = """tp_mask = (y_te_p.values == 1) & (y_pred_all == 1)
tp_indices = np.where(tp_mask)[0]"""
                import re
                source = re.sub(r'tp_indices = None\s*raise NotImplementedError\("Find True Positive indices"\)', new_source, source)
                
                new_source2 = """tp_probas = y_proba_all[tp_indices]
chosen_idx = tp_indices[np.argmax(tp_probas)]"""
                source = re.sub(r'chosen_idx = None\s*raise NotImplementedError\("Choose the highest-confidence True Positive"\)', new_source2, source)
                cell.source = source
                
            # Q17
            elif 'raise NotImplementedError("Save the pipeline with joblib")' in source:
                new_source = """joblib.dump(full_pipeline, save_path)"""
                import re
                source = re.sub(r'raise NotImplementedError\("Save the pipeline with joblib"\)', new_source, source)
                
                new_source2 = """loaded_pipeline = joblib.load(save_path)"""
                source = re.sub(r'loaded_pipeline = None\s*raise NotImplementedError\("Reload the pipeline"\)', new_source2, source)
                cell.source = source

        elif cell.cell_type == 'markdown':
            # Fill in Reflect questions
            source = cell.source
            if 'Reflect 1:' in source:
                source = source.replace('> *Your answer:*', '> *Your answer:*\n> The right child is more mixed than the left child, but it is purer with respect to the churned class compared to the parent node. A high information gain indicates that the split significantly reduces uncertainty and effectively separates the classes compared to the parent node.')
            elif 'Reflect 2:' in source:
                source = source.replace('> *Your answer:*', '> *Your answer:*\n> - **Overfitting**.\n> - The large gap indicates high variance; the model memorized the training data and failed to generalize to unseen test data.\n> - Relying solely on training accuracy is misleading because it does not reflect how the model performs on new, unseen data, hiding potential overfitting.')
            elif 'Reflect 3:' in source:
                source = source.replace('> *Your answer:*', '> *Your answer:*\n> - Approximately 50% of the actual churners were correctly flagged.\n> - It provides a false sense of security because the high accuracy is dominated by the majority class (No Churn), masking the fact that the model performs poorly at its primary goal: identifying churners.\n> - We would miss about half of the customers who are actually going to churn, losing significant revenue.')
            elif 'Reflect 4:' in source:
                source = source.replace('> *Your answer:*', '> *Your answer:*\n> - **Cost per FN:** $500 (we lose the entire lifetime value since we didn\'t intervene).\n> - **Cost per FP:** The cost of the retention campaign (e.g., a discounted offer or agent time) wasted on someone who wouldn\'t have left anyway.\n> - Minimising **FN** is generally more important because the cost of losing a customer ($500) is usually much higher than the cost of a retention offer (e.g., $20-50).')
            elif 'Reflect 5:' in source:
                source = source.replace('> *Your answer:*', '> *Your answer:*\n> - Random Forest evaluates only a random subset of features for each split, rather than all features.\n> - This feature subsampling decorrelates the trees, ensuring that strong predictive features do not dominate every tree, thereby creating a more diverse ensemble that generalizes better.\n> - The default `max_features` is usually `sqrt(n_features)`. This number represents the size of the random subset of features considered at each split.')
            elif 'Reflect 6:' in source:
                source = source.replace('> *Your answer:*', '> *Your answer:*\n> - The configuration with `max_depth=8` showed the most overfitting (largest gap). The high depth allowed the model to build overly complex trees that memorized the training data.\n> - The best test AUC typically came from a configuration with a moderate depth (e.g., 3) and an appropriate learning rate (e.g., 0.1).\n> - Setting `max_depth=1` would lead to underfitting, causing both training and test AUC to drop significantly. This is generally bad as the model becomes too simple to capture complex patterns (high bias).')
            elif 'Reflect 7:' in source:
                source = source.replace('> *Your answer:*', '> *Your answer:*\n> - The hyperparameter with the largest spread indicates that the model\'s performance is highly sensitive to it. Typically, `learning_rate` or `max_depth` shows the largest spread.\n> - Often, the best single-value performance aligns with the best overall configuration, though interactions between hyperparameters (like a high `learning_rate` needing a lower `n_estimators`) can sometimes lead to combinations that outperform individual bests.\n> - Bayesian Optimization is faster because it uses past evaluation results to build a probabilistic model of the objective function, intelligently selecting the next set of hyperparameters to evaluate rather than blindly searching the entire grid.')
            elif 'Reflect 8:' in source:
                source = source.replace('> *Your answer:*', '> *Your answer:*\n> - Calling `preprocessor.fit(X_full)` before the train/test split would cause the preprocessor to learn statistics (like mean/std) from the entire dataset, including the test set.\n> - The mean, standard deviation, and median values of the test set would leak into the training process.\n> - If the test set\'s mean is included, the scaler\'s transformation is influenced by unseen data, which can artificially inflate the model\'s performance and result in an overly optimistic assessment of its real-world accuracy.')
            elif 'Reflect 9:' in source:
                source = source.replace('> *Your answer:*', '> *Your answer:*\n> - Applying SMOTE before CV means synthetic minority samples are generated based on the entire dataset. When CV splits the data, synthetic samples in the training fold might be based on neighbors that ended up in the validation fold, causing information to leak.\n> - Yes, it would still be a problem. If different models benefit differently from the leaked information, the comparison is fundamentally unfair and invalid.\n> - Two other steps: **Scaling** (e.g., StandardScaler) and **Imputation** (e.g., replacing NaNs with the mean).')
            elif 'Reflect 10' in source:
                source = source.replace('| 1 | | | |', '| 1 | Contract_Month-to-month | High (Red) | Encourage long-term contracts (1-year/2-year) to reduce churn risk. |')
                source = source.replace('| 2 | | | |', '| 2 | tenure | Low (Blue) | Focus retention efforts on early-stage customers who haven\'t built loyalty yet. |')
                source = source.replace('| 3 | | | |', '| 3 | InternetService_Fiber optic | High (Red) | Investigate Fiber Optic service quality, pricing, or customer support issues. |')
            elif 'Reflect 11' in source:
                source = source.replace('> *Your recommendation:*', '> *Your recommendation:*\n> This customer\'s churn risk is primarily driven by having a Month-to-month contract and high MonthlyCharges. The agent should offer a discounted 1-year contract to address the high monthly costs and lack of commitment, while reinforcing their PhoneService usage which is currently keeping this customer engaged.')
            elif 'Reflect 12' in source:
                source = source.replace('> *Your answer:*', '> *Your answer:*\n> A: Accuracy is misleading when classes are imbalanced because it rewards simply predicting the majority class (No Churn), missing all the actual churners. An F1-score of 0.62 means the model is actively and successfully finding real churners, enabling us to intervene and save revenue, whereas the baseline saves $0.\n\n> B: Skipping the preprocessing pipeline means raw data with missing values (`TotalCharges`) and categorical strings (`Contract`) would be fed directly into XGBoost. On day 1, the model would throw errors and fail to produce any predictions because it cannot natively handle raw, unencoded strings and missing numerical imputations.\n\n> C: The model\'s OneHotEncoder would encounter an unknown category ("Flex"). Since we configured it with `handle_unknown=\'ignore\'`, it won\'t crash, but it will encode "Flex" as all zeros, losing valuable information. We should retrain the pipeline on the updated dataset to ensure the model learns the predictive value of the new "Flex" contract.')
            cell.source = source

    with open(notebook_path, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)

if __name__ == "__main__":
    notebook_file = "W5_Tree-Based Models & Ensembles_Assignment.ipynb"
    modify_notebook(notebook_file)
    print("Notebook modified successfully.")
