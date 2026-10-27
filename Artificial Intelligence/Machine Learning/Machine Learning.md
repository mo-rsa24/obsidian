# Machine Learning

Up: [[Artificial Intelligence]]

Artificial Intelligence, Machine Learning. [[Cross-Entropy]] and [[Backpropagation]] sit elsewhere in the vault: Cross-Entropy under Mathematics, Statistics, and Backpropagation at the top of Artificial Intelligence.

**Machine learning fits a model to data by choosing the parameters that make a loss small. These notes cover the losses, the loop that lowers them, and the numbers that say how well a trained classifier does.**

- [[Loss Function]]: A loss function turns a model's predictions on the training data into one number that says how badly the model fits, and training means changing the parameters to make that number small.
- [[Mean Squared Error]]: Mean squared error is the average of the squared differences between a model's predictions and the true values, so a miss of 2 costs four times a miss of 1.
- [[Mean Absolute Error]]: Mean absolute error is the average of the absolute differences between predictions and true values, so a miss of 2 costs twice a miss of 1 and an outlier pulls the fit far less than under squared error.
- [[Gradient Descent]]: Gradient descent fits a model by repeatedly computing the gradient of the loss with respect to the parameters and moving the parameters a small step in the opposite, downhill direction; stochastic gradient descent estimates that gradient on a random batch of examples instead of the whole training set.
- [[Learning Rate]]: The learning rate is the number that multiplies the gradient in each update, so it sets how far the parameters move per step: too small and training crawls, too large and the loss overshoots and can blow up.
- [[Epoch]]: An epoch is one complete pass through the training data; with minibatches, one epoch is as many updates as there are batches in the dataset.
- [[Classifier]]: A classifier is a model that assigns each input one label from a fixed set of classes, such as spam or not spam, or one of three iris species, usually by first giving a probability for every class.
- [[Accuracy]]: Accuracy is the share of predictions a classifier gets right, correct predictions divided by all predictions; one minus it is the misclassification rate.
- [[Precision And Recall]]: Precision is the share of the items a model flagged that really are positive, TP / (TP + FP); recall is the share of the real positives it found, TP / (TP + FN); the F1 score is their harmonic mean.
- [[Mean Reciprocal Rank]]: Mean reciprocal rank scores a ranked list by where the first relevant item lands, 1 divided by its rank, averaged over queries; MRR@k scores 0 outside the top k.
