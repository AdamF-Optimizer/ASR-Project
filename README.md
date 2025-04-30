# Instructions
This repository contains 2 folders:
  * The "Standard Version" folder runs the training once, then evaluates. This was used to get a working baseline.
  * The "K-Fold Version" folder extends upon the "Standard Version" by performing K-Fold cross-validation, in addition to testing with random forests.

The notebooks can be uploaded and run in your favorite notebook editor, such as Jupyter or Google Colab.

There are 2 things to note:
1. For the results presented in the paper, the Whisper small and Whisper medium models were used.
2. You must recompute the features, as the generated feature CSV is too large to upload to GitHub.
