# Instructions
To preprocess the full Parkceleb dataset, you can follow the code in the `Parkceleb_Pre_processing` notebook.

This repository contains 2 folders:
  * The "Standard Version" folder runs the training once, then evaluates. This was used to get a working baseline.
  * The "K-Fold Version" folder extends and improves upon the "Standard Version" in several ways:
    * This version makes use of K-Fold cross-validation for more reliable results.
    * The total dataset features are saved in a single CSV, which is then split into training and testing partitions during cross-validation.
    * Added patient information (id, label, time before diagnosis) to features CSV.
      * Note: There may be an error causing the label to not be correct in the CSV, however, there is a `fix_labels_in_csv` function at the end of the notebook that           fixes this.
    * Improved displaying and comparison of results with visualization through plots (and saving them).
    * Added testing with random forests.

The notebooks can be uploaded and run in your favorite notebook editor, such as Jupyter or Google Colab.

A few things to note:
1. For the results presented in the paper, the Whisper small and Whisper medium models were used in the K-Fold version.
2. You must recompute the features, as the generated feature CSV is too large to upload to GitHub.
3. Should you want to test with other whisper models, you must change the name of the model in the feature compute function, and of the generated/loaded CSVs.
