---
title: Back Propagation
date: 2021-10-10
tags: ['back_propagation', 'udacity']
draft: false
summary: 
---
# What is Back Propagation 


![/static/images/ai/Backpropagation_weight_update_1.png](/static/images/ai/Backpropagation_weight_update_1.png)


=> Back Propagation
- Step 1 : Calculate Gradient 
- Step 2 : Update Weight by subtracting gradient

- Back Propagation is the process of updating the weights to decrease the loss. 
- It's done by gradually subtracting the network weights by gradients of the loss function. 


# Why gradient and why subtract gradient to decreases loss ?

 
![/static/images/ai/Backpropagation_loss_curve_1.png](/static/images/ai/Backpropagation_loss_curve_1.png)


- Assume there's only 1 weight in the NN that we need to learn. 
- $E_A$ : Value of loss function at point A where weight =  $W_A$
- From the graph its evident that we need to increase the weight to decrease the loss
- The gradient or derivative or slope of the curve at point A is negative, So by subtracting -ve gradient to weight increases weight there by reducing loss. 


![/static/images/ai/Backpropagation_loss_curve_2.png](/static/images/ai/Backpropagation_loss_curve_2.png)


- B : At point B, we need to decrease the weights to reduce the loss function. 
- Gradient : Grad at point B is positive there by subtracting gradient from weights decreases the weights. 


# Why Partial Derivatives


![/static/images/ai/Backpropagation_partial_derviatives.png](/static/images/ai/Backpropagation_partial_derviatives.png)

- Above we considered only 1 weight for simplicity. But in reality we have millions of weights in NN. The loss is a function of all these millions of weights.


# Defining notations before divining in  

 
![/static/images/ai/Backpropagation_sample.png](/static/images/ai/Backpropagation_sample.png)


- $K:$ Superscript K indicates the weight is connecting from layer K to K+1 
- $\nabla:$ Gradient
- $W^k_{i,j}:$ Weight connecting from neuron i in layer k to neuron J in layer k+1
- $\nabla W^k_{i,j}:$ Amount by which weight $W^k_{i,j}$ is updated

 
 
![/static/images/ai/Backpropagation_error_considerations.png](/static/images/ai/Backpropagation_error_considerations.png)


- $E:$ Error function or loss function (Parameterized by weights ex: aw1+bw2+....)


# Example Network :


![/static/images/ai/Backpropagation_sample_network.png](/static/images/ai/Backpropagation_sample_network.png)


- Consider a single hidden layer network with one output for simplicity

- $W^1_{ij}:$ Weight Matrix connecting from neuron i to j in layer 1
- $W^2_{i}:$ Since we only have one output, the weights connecting from layer 1 to 2 is just a vector $w^2_i$
- $\nabla_{w^1_{ij}}(-E):$ Derivative of loss function w.r.t weight   $w^1_{ij}$
- $\nabla_{w^2_{i}}(-E):$ Derivative of loss function w.r.t weight   $w^2_{i}$
- $h_1, h_2, h_3:$ Activation's of hidden layer


## First feed forward :


### Calculate hidden layer activation's :


![/static/images/ai/Backpropagation_hidden_layer_activations.png](/static/images/ai/Backpropagation_hidden_layer_activations.png)


$w^1_{i1}:$ Weights connecting from inputs $x_1,x_2$ to hidden layer $h_1$
$\phi:$ Activation function ex: Sigmoid 
$\sum^2_i x_i * w^1_{i1}$ : Sum of Matrix multiplication of inputs and weights. 


### Calculate output :


![/static/images/ai/Backpropagation_sample_network_output.png](/static/images/ai/Backpropagation_sample_network_output.png)


- $y:$ Similar to calculating hidden units, calculation of output y


## Now Back propagation steps 

- Remember chain rule ?

	
![/static/images/ai/Backpropagation_chain_rule.png](/static/images/ai/Backpropagation_chain_rule.png)


	- Feed Forward : We can relate the above process as feed forward because feed forwarding is nothing but composing functions of functions parameterized by weights. 
	- $\partial B/ \partial x:$ Partial derivative of B w.r.t x.  
	- Considering B be our loss function and x be our weights, notice that chain rule makes it quite easy to calculate partial derivatives. 

- Partial derivative of loss function w.r.t weights 

	
![/static/images/ai/Backpropagation_patial_derivatives.png](/static/images/ai/Backpropagation_patial_derivatives.png)


	$d:$ Desired output (d is a constant)
	$y:$ Calculated output (y is a function is weights) 
	$E:$ Squared error loss function ( divided by 2 is just done so that during partial derivative it cancels out )
	$\nabla W_{ij}:$ Gradient w.r.t loss function E 
	$\alpha :$ Learning rate 

- Calculating partial derivatives 

	 
![/static/images/ai/Backpropagation_calculating_partial_derivatives.png](/static/images/ai/Backpropagation_calculating_partial_derivatives.png)

	- Our sample network has 2 weights, $w^1_{ij}$ and $w^2_{i}$ for which partial derivatives are to be calculated. 

	- Step 1: Find $\partial y/ \partial {w^2_i}$ 	
		 
![/static/images/ai/Backpropagation_layer2_gradients.png](/static/images/ai/Backpropagation_layer2_gradients.png)

		- So from above figure, the partial derivative is simply the hidden activation itself. 
		
![/static/images/ai/Backpropagation_layer2_gradients_1.png](/static/images/ai/Backpropagation_layer2_gradients_1.png)

		- Back propagating the gradients for weight $W^2$

	- Step 2: Find  $\partial y/ \partial w^1_{ij}$
		- This calculation requires chain rule to be used. 
		
![/static/images/ai/Backpropagation_layer1_gradients_calculation_1.png](/static/images/ai/Backpropagation_layer1_gradients_calculation_1.png)

		- We need $\partial y/ \partial h$ and $\partial h/ \partial w$

		
![/static/images/ai/Backpropagation_layer1_gradients_calculation_2.png](/static/images/ai/Backpropagation_layer1_gradients_calculation_2.png)
		
		
![/static/images/ai/Backpropagation_layer1_gradients_calculation_3.png](/static/images/ai/Backpropagation_layer1_gradients_calculation_3.png)
		
		
![/static/images/ai/Backpropagation_layer1_gradients_calculation_4.png](/static/images/ai/Backpropagation_layer1_gradients_calculation_4.png)

		
		- $h_j$ is a function of activation function $\phi$ 
		- $\phi$ is  a function of $\sum(x_iW^1_{i,j})$
		
		> So using chain rule, we can write as below :
		> 
		> $\partial h_i/ \partial w^1_{i,j}$ = $\partial h_i/ \partial \phi$ * $\partial \sum(x_iW^1_{i,j})/ \partial W^1_{i,j}$
		> 
		>   $\partial h_i/ \partial w^1_{i,j}$ = $\phi^1$ * $x_i$

		
![/static/images/ai/Backpropagation_layer1_gradients_update.png](/static/images/ai/Backpropagation_layer1_gradients_update.png)

		- Updating gradients at layer 1 for weight $W^1$

- We have implemented back propagation on  a simple network in mathematical terms. 


---
Status: #done

Tags: 
#back_propagation

References: 
#udacity

Sources:

