---
title: 5 Gan Challenges
date: 2021-10-09
tags: ['wgan', 'wgan_gp', 'lipschitz_constraint']
draft: false
summary: 
---
### Oscillating Loss:

The loss of [[AI/GAN/4-GAN#Generator | generator ]]  and [[AI/GAN/4-GAN#Discriminator | discriminator]]  could start to oscillate wildly, rather than exhibiting long term stability. Vanilla GAN's are very prone to this instability, check the graph below 


![/static/images/gan/gan_oscillating_loss.png](/static/images/gan/gan_oscillating_loss.png)



### Mode Collapse 

Mode collapse occurs when the generator finds a small number of samples that fool the discriminator and therefore isn’t able to produce any examples other than this limited set. Let’s think about how this might occur. Suppose we train the generator over several batches without updating the discriminator in between.

The generator would be inclined to find a single observation (also known as a mode) that always fools the discriminator and would start to map every point in the latent input space to this observation. This means that the gradient of the loss function collapses to near 0.

Even if we then try to retrain the discriminator to stop it being fooled by this one point, the generator will simply find another mode that fools the discriminator, since it has already become numb to its input and therefore has no incentive to diversify its output.


### Uninformative Loss 

We know that models are compiled to minimize the loss function, so its natural to assume lower loss function means the generator is getting better at producing good images, however that is simply not true in this case. 

Because training happens in steps here, if we train the discriminator and then get back to train the generator. At this stage the generator loss may be higher than before but it doesn't necessarily mean that generator is producing less quality images, it could be simply because now the discriminator is much better at identifying fake images and so loss has increased. 


### Hyperparameters 

Even with a simple GAN we have a lot of parameters to train, GAN's are highly sensitive to very slight changes in all of these parameters, and finding a set of parameters that works is often a case of educated trial and error, rather than following an established set of guidelines


## Tackling GAN challenges  

We shall look into 2 advancements, the Wasserstein GAN (WGAN) and Wasserstein GAN–Gradient Penalty (WGAN-GP). Both are only minor adjustments to the vanilla GAN


### Wasserstein GAN (WGAN)

The Wasserstein GAN was one of the first big steps toward stabilizing GAN training, the authors were able to show how to train GAN's that have the following two properties.

1. Meaningful loss metric that correlates the generators convergence to the sample quality generated.
2. Improved stability of optimization process.

WGAN introduces new loss function instead of regular BCE loss to achieve a better stable convergence for both generator and discriminator. 


 - **Wassertein Loss**

	- Vanilla GAN uses sigmoid activation limiting outputs in the range  \[0 , 1] and uses BCE loss  -->  
![/static/images/gan/gan_bce_loss_eq.png](/static/images/gan/gan_bce_loss_eq.png)


	- In WGAN,  the sigmoid activation layer in discriminator is removed and so outputs could be any number in the range \[–∞, ∞]. For this reason, the discriminator in WGAN is usually referred to as critic. The labels are also changed from 0,1 to -1,1  --> -1 for fake image and 1 for original image. Wassertein loss function is given as below : 

	- 
![/static/images/gan/gan_wgan_wasserstein_loss.png](/static/images/gan/gan_wgan_wasserstein_loss.png)


	- Since true labels have y=1 and false labels y=-1, from the above equation we can infer that the loss is trying to maximize the distance between +ve and -ve samples. In other words, ** the WGAN critic tries to maximize the difference between its predictions for real images and generated images, with real images scoring higher. **


- **The Lipschitz Constraint**

	- One problem you might be thinking is how can we let the output be unbounded \[–∞, ∞], yes we definitely cannot. For the critic to work we need a constraint on the critic. Specifically, we require the critic to be a lipschitz continuous function. 

	- The critic is a function that converts the image into a prediction. We say that D is 1-lipschitz function when the below eq is satisfied for any two input images says x1, x2
	- 
![/static/images/gan/gan_wgan_lipschitz_condition.png](/static/images/gan/gan_wgan_lipschitz_condition.png)


	- Here, x1 – x2 is the average pixel wise absolute difference between two images and D(x1) − D(x2) is the absolute difference between the critic predictions. ** So essentially what we are doing is, we are enforcing a limit on the rate at which predictions of the critic could change between 2 images.(i.e., the absolute value of the gradient must be at most 1 everywhere). **

	- Before understanding nature of lipschitz continuous function, lets have a look at different slops -->
	 - 
![/static/images/gan/gan_slopes.png](/static/images/gan/gan_slopes.png)


	- Now, look at the below function. We can observe, at any given point the absolute slope does not go beyond 1 i.e the slope line does not enter inside the cone where abs slope is greater than 1. 
	- 
![/static/images/gan/gan_wgan_lipschitz_function.png](/static/images/gan/gan_wgan_lipschitz_function.png)


	- Now the question is how to enforce this Lipschitz constrain on the critic ? 


- **Weight Clipping**

	- In the WGAN paper, the authors show how it is possible to enforce the Lipschitz constraint by clipping the weights of the critic to lie within a small range, \[–0.01, 0.01], after each training batch.


- **Training WGAN **

	- When using WGAN loss function, we should train the critic to convergence to ensure the gradients for the generator update are accurate, this is in contrast to vanilla GAN where it is important not to let the discriminator get too strong to avoid vanishing gradient descent. 

	- With WGAN, we can simply train critic multiple times between generator updates, to ensure critic is close to convergence and generator loss function has correlation with the quality of samples produced. 

	- We have now covered all of the key differences between a standard GAN and a WGAN. To recap:
		- A WGAN uses the Wasserstein loss. 
		- The WGAN is trained using labels of 1 for real and –1 for fake. 
		- There is no need for the sigmoid activation in the final layer of the WGAN critic. 
		- Clip the weights of the critic after each update to enforce lipschitz constraint on the critic. 
		- Train the critic multiple times for each update of the generator.


- ** Analysis of WGAN**

	- One main problem with WGAN is that, to enforce Lipschitz constraint we are clipping the weights of critic which is limiting the learning potential of critic greatly. 

	- A strong critic is pivotal to the success of a WGAN, since without accurate gradients, the generator cannot learn how to adapt its weights to produce better samples. Therefore effort is put into other ways of enforcing lipschitz constrained (WGAN - GP)


![/static/images/gan/gan_wgan_loss_curve.png](/static/images/gan/gan_wgan_loss_curve.png)


As you can see above, the Wassertein loss decreases as the quality of the images produced by the generator improves, unlike vanilla GAN generator loss. 


### Wasserstein GAN– Gradient Penalty (WGAN-GP)

The WGAN-GP generator is defined and compiled in exactly the same way as the WGAN generator. It is only the definition and compilation of the critic that we need to change.

In total, there are three changes we need to make to our WGAN critic to convert it to a WGAN-GP critic:

• Include a gradient penalty term in the critic loss function that penalizes the model if the gradient norm of the critic deviates from 1.
• Don’t clip the weights of the critic. 
• Don’t use batch normalization layers in the critic.


![/static/images/gan/gan_wgan_gp_loss.png](/static/images/gan/gan_wgan_gp_loss.png)


#### The Gradient Penalty Loss

The gradient penalty loss measures the squared difference between the norm of the gradient of the predictions with respect to the input images and 1. It is intractable to calculate this gradient everywhere during the training process, so instead the WGAN-GP evaluates the gradient at only a handful of points. To ensure a balanced mix, we use a set of interpolated images that lie at randomly chosen points along lines connecting the batch of real images to the batch of fake images pairwise, as shown below :


![/static/images/gan/gan_wgan_gp_interpolated_image.png](/static/images/gan/gan_wgan_gp_interpolated_image.png)


#### Batch Normalization in WGAN-GP

Because batch normalization creates correlation among batch images which makes the gradient penalty term less effective. So in WGAN-GP we avoid batch normalization. 


***
Header Tags : #gan 

Tags:
#wgan
#wgan_gp
#lipschitz_constraint

Reference : 

- Since KL divergence and Jason Shannon divergence cause vanishing gradient problem, we moved to [Wassertein loss (must read blog)](https://medium0.com/@jonathan_hui/gan-wasserstein-gan-wgan-gp-6a1a2aa1b490)
- [WGAN Paper](https://arxiv.org/pdf/1701.07875.pdf)

Source : 

