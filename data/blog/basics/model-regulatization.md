---
title: Model Regulatization
date: 2021-10-10
tags: ['model_regularization', 'weight_decay']
draft: false
summary: 
---

![/static/images/ai/Regularization_model_complexity.png](/static/images/ai/Regularization_model_complexity.png)

- Model optimization process works on the basis of minimizing loss function
$$Error = MSE = (y-\hat y)^2$$

| left model       | right model                                 |
| ---------------- | ------------------------------------------- |
| more error       | less error                                  |
| simpler model    | complex model with many features or weights |
| generalizes well | over-fitting the data                       |

- Its obvious our model will end up being the one on the right if our goal is to minimize the loss function only.


![/static/images/ai/Regularization_error_with_complexity.png](/static/images/ai/Regularization_error_with_complexity.png)

$$ Error = MSE + \lambda * Model \;Complexity $$
- So along with loss function we target to reduce the complexity of model also. 
- Regularization works on assumption that smaller weights generate simpler model and thus helps avoid over-fitting.
- $\lambda$ is a hyper parameter, which helps us to control by how much we want to penalize the model complexity. 


# L1  


![/static/images/ai/Regularization_L1.png](/static/images/ai/Regularization_L1.png)

$$Error = MSE + \lambda \sum |W| $$

![/static/images/ai/Regularization_L1_form.png](/static/images/ai/Regularization_L1_form.png)

- Sum of absolute weights 
- Reduces complexity by pushing unnecessary weights towards 0.
- Helpful in feature selection and yields sparse models.
- Robust to outliers 


# L2 


![/static/images/ai/Regularization_L2.png](/static/images/ai/Regularization_L2.png)

$$Error = MSE + \lambda \sum W^2 $$

![/static/images/ai/Regularization_L2_form.png](/static/images/ai/Regularization_L2_form.png)

- Sum of squares of weights
- Forces the weights to be small but does not make them zero
- Not robust to outliers
- Gives better prediction when output variable is a function of all input features


# Elastic net 

- This regression is a compromise between L1 and L2. Generally called L1 Ratio.
-  It defines what proportion of L1 penalty is to be applied to the model.
- L1 Ratio = 1 => Completely L1 loss 
- L1 Ratio = 0 => Completely L2 loss


# Dropout
- During training, with some probability P few neurons of the neural network gets turned off. 
- This forces the network to focus on other weights that are neglected.


# Weight Decay 
- Weight decay is simply decaying the weight by a constant factor during training, this term is added to loss and gets subtracted from weights during each epoch of training. 
- Purpose of weight decay is to control the weights from getting overly complex and perform over-fitting of the data. 
- > Weight Update  :
       >W  = W - lr  ( Loss + weight decay * W )
- [Good read](https://towardsdatascience.com/this-thing-called-weight-decay-a7cd4bcfccab)


# Summary
-   Over-fitting occurs in more complex neural network models (many layers, many neurons)
-   Complexity of the neural network can be reduced by using L1 and L2 regularization as well as dropout
-   L1 regularization forces the weight parameters to become zero
-   L2 regularization forces the weight parameters towards zero (but never exactly zero)
-   Smaller weight parameters make some neurons neglectable → neural network becomes less complex → less overfitting
-   During dropout, some neurons get deactivated with a random probability **P** → Neural network becomes less complex → less overfitting

# ToRead
- #toread
- [# Survey of Techniques All Classifiers Can Learn from Deep Networks: Models, Optimizations, and Regularization](https://arxiv.org/abs/1909.04791)
- Label Smoothing 
- DropBlock
- CutMix


---
Status : #writing

Tags: 
#model_regularization
#weight_decay

References : 
- [L2 and L2 intuition](https://medium.datadriveninvestor.com/l1-l2-regularization-7f1b4fe948f2)
- [L1 and L2](https://towardsdatascience.com/intuitions-on-l1-and-l2-regularisation-235f2db4c261)

