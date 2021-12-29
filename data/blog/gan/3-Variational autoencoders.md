---
title: 3 Variational autoencoders
date: 2021-10-09
tags: ['gan', 'variational_autoencoder', 'autoencoder', 'kullback_leibler_divergence', 'Normal']
draft: false
summary: 
---
How exactly variational autoencoders are going to solve the problems of [[AI/GAN/2-Autoencoders|autoencoder]] ?
We are going to split to 2 parts in var autoencoder, they are encoder and the loss function, the decoder is exactly the same as in autoencoder. 


# Encoder

In an autoencoder each image is mapped to a point in the latent space, however in VAR each image is mapped to a multivariate [[AI/Math/2_probability distribution#Normal Distribution|normal distribution]] in the latent space  as shown below :


![/static/images/gan/gan_ae_vs_vae.png](/static/images/gan/gan_ae_vs_vae.png)


Its understood that parameters for a normal distribution are --> mean and variance , using just these 2 parameters we can form all sorts of normal distribution possible. So the encoder will take each input image and encode it into 2 vectors.

1. $\mu$ The mean point of the distribution. 
2. log_var The logarithm of the variance of each dimension. 
		
	>Here we are estimating log of variance as it can take any value in range (– ∞, ∞) matching the natural output range from a neural network unit, whereas variance values are always positive.

These parameters define a multivariate normal distribution in the latent space. Now to encode the image to  a specific point in the latent space, we sample a point z from the normal distribution formed using the above parameters. 

> z = $\mu$ + $\sigma$ * epsilon ; where $\sigma$ = exp(log_var / 2)
> $\sigma$ = $e^{log\:\sigma}$ = exp(  2 log σ /2 ) = exp( log σ2 /2 )  
> 
> Variance = $σ^2$ 
> Epsilon is a point sampled for standard normal distribution i.e where $\mu$ = 0 and $\sigma$ = 0

### So why does this small change to the encoder help?

Previously, we saw how there was no requirement for the latent space to be continuous even if the point (–2, 2) decodes to a well-formed image of a 4, there was no requirement for (–2.1, 2.1) to look similar. 

Now, since we are sampling a random point from an area around mu, the decoder must ensure that all points in the same neighborhood produce very similar images when decoded, so that the reconstruction loss remains small. 

This is a very nice property that ensures that even when we choose a point in the latent space that has never been seen by the decoder, it is likely to decode to an image that is well formed

A glance on the changes for VAR encoder in terms of code : 

![/static/images/gan/gan_encoder_code.png](/static/images/gan/gan_encoder_code.png)



# Loss Function

Previously, our loss function only consisted of the RMSE loss between images and their reconstruction after being passed through the encoder and decoder. This reconstruction loss also appears in a variational autoencoder, but we require one extra component: the Kullback–Leibler (KL) divergence.

KL divergence is a way of measuring how much one probability distribution differs from another. In a VAE, we want to measure how different our normal distribution with parameters mu and log_var is from the standard normal distribution. In this special case, the KL divergence has the closed form:

>kl_loss = -0.5 * sum(1 + log_var - mu ^ 2 - exp(log_var))

The sum is taken over all the dimensions in the latent space. kl_loss is minimized to 0 when mu = 0 and log_var = 0 for all dimensions. As these two terms start to differ from 0, kl_loss increases.

In summary, the KL divergence term penalizes the network for encoding observations to mu and log_var variables that differ significantly from the parameters of a standard normal distribution, namely mu = 0 and log_var = 0.


### How does this additional term in loss function help ?

1. Now we have a defined normal distribution that we can use to choose points in latent space, unlike autoencoder, where we choose points randomly for image generation. 
2. Since we sample from this distribution, we know that we’re very likely to get a point that lies within the limits of what the VAE is used to seeing
3. Since this term tries to force all encoded distributions toward the standard normal distribution, there is less chance that large gaps will form between point clusters

The loss function for a VAE is simply the addition of the reconstruction loss and the KL divergence loss term. We weight the reconstruction loss with a term, r_loss_factor, that ensures that it is well balanced with the KL divergence loss

Sample code where RMSE and KL loss is combined with a r_loss_factor

![/static/images/gan/gan_vae_compilation_code.png](/static/images/gan/gan_vae_compilation_code.png)


Find below, latent space of the trained VAE. 

![/static/images/gan/gan_latent_space_vae_by_digitcolor.png](/static/images/gan/gan_latent_space_vae_by_digitcolor.png)


We can notice that 
1. KL divergence loss ensures that sigma value stays close to standard normal distribution 
2. Latent space is locally continuous with no large gaps making sure the generated images are well formed.
3. Also by viewing the colored points per digit in latent space we can safely say that no digit is given preferential treatment.  


# Latent space arithmetic 

One benefit of mapping images into a lower-dimensional space is that we can perform arithmetic on vectors in this latent space that has a visual analogue when decoded back into the original image domain.

For example, suppose we want to take an image of somebody who looks sad and give them a smile. To do this we first need to find a vector in the latent space that points in the direction of increasing smile 

So how can we find the smile vector? Each image in the CelebA dataset is labeled with attributes, one of which is smiling. If we take the average position of encoded images in the latent space with the attribute smiling and subtract the average position of encoded images that do not have the attribute smiling, we will obtain the vector that points from not smiling to smiling, which is exactly what we need.

Conceptually, we are performing the following vector arithmetic in the latent space, where alpha is a factor that determines how much of the feature vector is added or subtracted:

>z_new = z + alpha * feature_vector

Fig below shows several images that have been encoded into the latent space. We then add or subtract multiples of a certain vector (e.g., smile, blonde, male, eyeglasses) to obtain different versions of the image, with only the relevant feature changed.


![/static/images/gan/gan_latent_space_arthematic.png](/static/images/gan/gan_latent_space_arthematic.png)



---
Tags: 
#gan
#variational_autoencoder 
#autoencoder  
#kullback_leibler_divergence

Reference : 
- [[AI/GAN/2-Autoencoders]] 
- [[AI/Math/2_probability distribution#Normal Distribution]]
- https://www.oreilly.com/library/view/generative-deep-learning/9781492041931/

Source : 

