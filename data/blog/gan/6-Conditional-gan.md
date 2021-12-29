---
title: 6 Conditional Gan
date: 2021-10-09
tags: ['gan', 'conditional_gan']
draft: false
summary: 
---
# What is the difference of conditional GAN from vanilla GAN?

- Let's say we train vanilla GAN on 2 different classes say cats and dogs, then the generated result could be either cat or dog or some weird image combining both.
-  So how to control the generation of certain class of images, well one solution is trail and error method. Basically to generate image we pick a point from the multi variate normal distribution and pass it to generator. So we can trail to find out in which direction we need to move to generate images that look like a cat. 
-  Look at example below for the latent space of MNIST


![/static/images/gan/gan_cgan_exmaple_1.png](/static/images/gan/gan_cgan_exmaple_1.png)


- So how can we make GAN generate image containing certain class ? Answer is conditioning the GAN by providing extra input i.e the class label we are interested in generating. 


# Architecture 

- Below is the architecture of CGAN
	- Y is the one hot vector of the class label we want to generate.
	- Random Noise is the randomly picked point from normal distribution. 	
 
![/static/images/gan/gan_cgan_architecture.png](/static/images/gan/gan_cgan_architecture.png)

- An in depth architecture view is given below: 
 
![/static/images/gan/gan_cgan_arch.jpg](/static/images/gan/gan_cgan_arch.jpg)



# Loss 

- **The Discriminator has two task**
	-   Discriminator has to correctly label real images which are coming from training data set as “real”.
	-   Discriminator has to correctly label generated images which are coming from Generator as “fake”.
	-   We need to calculate two losses for the Discriminator. The sum of the “fake” image and “real” image loss is the overall Discriminator loss.  So the loss function of the Discriminator is aiming at minimizing the error of predicting real images coming from the dataset and fake images coming from the Generator given their one-hot labels.

	 
![/static/images/gan/gan_cgan_discriminator_loss.png](/static/images/gan/gan_cgan_discriminator_loss.png)


- **The Generator network has one task**
	- To create an image that looks as “real” as possible to fool the Discriminator.
	- The loss function of the Generator minimizes the correct prediction of the Discriminator on fake images conditioned on the specified one-hot labels.
	
	 
![/static/images/gan/gan_cgan_generator_loss.png](/static/images/gan/gan_cgan_generator_loss.png)



# Training Flow 

- Find below the training flow for Discriminator and Generator: 


![/static/images/gan/gan_cgan_discriminator_training.png](/static/images/gan/gan_cgan_discriminator_training.png)

 
![/static/images/gan/gan_cgan_generator_training.png](/static/images/gan/gan_cgan_generator_training.png)


---
Tags:
#gan
#conditional_gan

Reference : 
    - https://www.oreilly.com/library/view/generative-deep-learning/9781492041931/
	- [An-introduction-to-conditional-gans-cgans](https://medium.datadriveninvestor.com/an-introduction-to-conditional-gans-cgans-727d1f5bb011)
	- [[Conditional_GAN.pdf]]

Source : 

