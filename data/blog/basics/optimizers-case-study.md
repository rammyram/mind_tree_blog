---
title: Optimizers Case Study
date: 2021-10-10
tags: ['momentum', 'rmsprop', 'adam', 'ema', 'squared_ema']
draft: false
summary: 
---
## Pathological Curvature


![/static/images/ai/Gradient_descent_loss_function_with_pathological_curvature.png](/static/images/ai/Gradient_descent_loss_function_with_pathological_curvature.png)


- In the above figure we started off at a random point and got stuck in the blue region, that blue region is called ravine region and the gradient is bouncing along the ridges of ravine moving a lot slower. 


![/static/images/ai/Gradient_descent_pathological_curvature_point_a.png](/static/images/ai/Gradient_descent_pathological_curvature_point_a.png)


- Looking at the region above we can understand the reason for this bounce offs, to reach a local minima we need to move in the direction of w2, but the gradient along w1 is much higher than w2 and so forcing the gradient to keep bouncing along w1 and slowly converge to the minima. 

- Gradient which is the 1st derivative only gives information about the steepness at a point but it has no information about the curvature 


![/static/images/ai/Gradient_descent_slopes.png](/static/images/ai/Gradient_descent_slopes.png)


- For example, gradient is the same for all the curves and even the straight (fig above). To find out the curvature of our loss surface we need the 2nd derivative, which gives us the nature of change of gradient over steps. 

- But deep NN has  billions of parameters and so we can't consider 2nd derivative. 

- However, here's an idea. Second order optimization is about incorporating the information about how is the gradient changing itself. **Though we cannot precisely compute this information, we can choose to follow heuristics that guide our search for optima based upon the past behavior of gradient.**


## Momentum

- A very popular technique that is used along with SGD is called **Momentum**. Instead of using only the gradient of the current step to guide the search, momentum also accumulates the gradient of the past steps to determine the direction to go. The equations of gradient descent are revised as follows.


![/static/images/ai/Momentum_math.png](/static/images/ai/Momentum_math.png)


- We see that the previous gradients are also included in subsequent updates, but the weightage of the most recent previous gradients is more than the less recent ones. (For the mathematically inclined, **we are taking an exponential average of the gradient steps**)


![/static/images/ai/Gradient_descent_pathological_curve.png](/static/images/ai/Gradient_descent_pathological_curve.png)


- For an update, this adds to the component along _w2_, while zeroing out the component in _w1_ direction. This helps us move more quickly towards the minima. For this reason, momentum is also referred to as a technique which dampens oscillations in our search.

- It also builds speed, and quickens convergence, but you may want to use simulated annealing in case you overshoot the minima.

- In practice, the coefficient of momentum is initialized at 0.5, and gradually annealed to 0.9 over multiple epochs.

## RMSProp

- So what momentum does is cancel out the w1 components in opposite direction and so helping our gradient to move in the direction of w2 component avoiding the zig zag... 

- We can also achieve this by taking big steps along w2 and small steps along w1, so we will need different LR for each parameter, that's what RMSProp does. 


![/static/images/ai/Optimizer_rmsProp.png](/static/images/ai/Optimizer_rmsProp.png)


- We are not doing exponential weighted sum of gradients like in momentum, instead we are doing exponential weighted sum of squared gradients. so the w1 gradients in opposite direction are summed instead of canceling. Obviously v(t) of w1 will be very high as compared to w2

- Observe the above fig, to calculate current gradient we are dividing the LR by square root of v(t), so LR will be very less for w1 and high for w2. So big steps are taken towards w2 avoiding zig zag. 

**Note :**
- The reason why we use exponential average is because as we saw, in the momentum example, it helps us weigh the more recent gradient updates more than the less recent ones. In fact, the name "exponential" comes from the fact that the weightage of previous terms falls exponentially (the most recent term is weighted as _p_, the next one as squared of _p_, then cube of _p_, and so on.)


## Adam

So far, we've seen RMSProp and Momentum take contrasting approaches. While momentum accelerates our search in direction of minima, RMSProp impedes our search in direction of oscillations.

**Adam** or **Adaptive Moment Optimization** algorithms combines the heuristics of both Momentum and RMSProp. Here are the update equations.


![/static/images/ai/Optimizer_adam.png](/static/images/ai/Optimizer_adam.png)



# Meta

 Tags: 
#momentum
#rmsprop
#adam
#ema
#squared_ema

References : 
- Best Blog: https://blog.paperspace.com/intro-to-optimization-momentum-rmsprop-adam/

Sources: 

