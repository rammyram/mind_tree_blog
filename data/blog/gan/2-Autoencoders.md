---
title: 2 Autoencoders
date: 2021-10-09
tags: ['gan', 'autoencoder', 'variational_autoencoder', 'Representational']
draft: false
summary: 
---
Auto encoder consists of an encoder and decoder. The network is trained to find weights for the encoder and decoder that minimize the loss between the original input and the reconstruction of the input after it has passed through the encoder and decoder. 

The representation vector is a compression of the original image into a lower dimensional, latent space. The idea is that by choosing any point in the latent space, we should be able to generate novel images by passing this point through the decoder, since the decoder has learned how to convert points in the latent space into viable images.

>An encoder network that compresses high-dimensional input data into a lower dimensional 	representation vector

>A decoder network that decompresses a given representation vector back to the original domain

# Autoencoder to generate digits 

We built an autoencoder and trained on digits, now our autoencoder should be able to generate new images. 

We can choose a random point in the latent space and feed it to decoder, since the decoder has learned how to convert points to images, the decoder should output a digit alike image. 


![/static/images/gan/gan_autoencoder.png](/static/images/gan/gan_autoencoder.png)


# Analysis of autoencoder

Now that our autoencoder is trained, we can start to investigate how it is representing images in the latent space. We’ll then see how variational autoencoders are a natural extension that fixes the issues faced by autoencoders.


![/static/images/gan/gan_latent_space_colored_by_digit.png](/static/images/gan/gan_latent_space_colored_by_digit.png)



From the above figure of latent space and distribution of digits in the latent space, we can infer some interesting points 

1. The plot is not symmetrical about the point (0, 0), or bounded. For example, there are far more points with negative y-axis values than positive, and some points even extend to a y-axis value of < –30.

>This point explains why its not obvious on how we should go about picking random points in latent space since the distribution of these points is undefined. 

2. Some digits are represented over a very small area and others over a much larger area.

>This point explains the lack of diversity in the generated images, Ideally we would like to have a equal spread of digits in latent space so that when we sample random points we have equal distribution of all digits. For example, the area of 1’s is far bigger than the area for 8’s, so when we pick points randomly in the space, we’re more likely to sample something that decodes to look like a 1 than an 8.
		
3. There are large gaps between colors containing few points. 

>These large gaps explain why some generated images are poorly formed. From the figure below the latent space and their decoded images, we can see that none of images are particularly well formed. 
		

![/static/images/gan/gan_latent_space_2.png](/static/images/gan/gan_latent_space_2.png)


>Partly, this is because of the large spaces at the edge of the domain where there are few points. The autoencoder has no reason to ensure that points here are decoded to legible digits as very few images are encoded here. However, more worryingly, even points that are right in the middle of the domain may not be decoded into wellformed images. 
>
>This is because the autoencoder is not forced to ensure that the space is continuous. For example, even though the point (2, –2) might be decoded to give a satisfactory image of a 4, there is no mechanism in place to ensure that the point (2.1, –2.1) also produces a satisfactory 4.
>
>This is just 2d, the problem of spacing will be huge when we move to higher complex dimensions which is often the case for many tasks, If we give the autoencoder free rein in how it uses the latent space to encode images, there will be huge gaps between groups of similar points with no incentive for the space between to generate well-formed images.

>Answer to all these problems is Variational Autoencoder 

		
---
Tags:
#gan
#autoencoder 
#variational_autoencoder

Reference : 
- [[AI/GAN/1-Generative-modeling#Representational Learning]]
- https://www.oreilly.com/library/view/generative-deep-learning/9781492041931/

Source : 

