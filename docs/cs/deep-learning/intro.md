---
title: Deep Learning
sidebar_position: 1
---

# Deep Learning

These notes follow Aston Zhang, Zachary C. Lipton, Mu Li, and Alexander J. Smola's *Dive into Deep Learning* and emphasize the book's central style: concepts, mathematics, and runnable code together. The path starts with tensors, data preparation, linear algebra, calculus, probability, and automatic differentiation, then builds complete training loops for regression and classification before moving to modern architectures.

![An artificial neural network diagram shows input, hidden, and output layers connected by weights.](https://commons.wikimedia.org/wiki/Special:FilePath/Artificial_neural_network.svg)

*Figure: Layered neural networks make differentiable function approximation visible. Image: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Artificial_neural_network.svg), Cburnett, CC BY-SA 3.0/GFDL.*

![A grid of MNIST handwritten digits shows the small grayscale examples used in many ML tutorials.](https://commons.wikimedia.org/wiki/Special:FilePath/MNIST_dataset_example.png)

*Figure: MNIST gives classification, vision, and neural-network pages a familiar benchmark image. Image: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:MNIST_dataset_example.png), Suvanjanprasai, CC BY-SA 4.0.*

![A simplified neural network diagram shows units connected from input to output.](https://commons.wikimedia.org/wiki/Special:FilePath/Neural_network.svg)

*Figure: A compact network diagram gives deep-learning pages a quick visual model of learned weights. Image: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Neural_network.svg), Dake and Mysid, CC BY 1.0.*

The later pages cover the main deep learning families: multilayer perceptrons, convolutional networks, recurrent networks, attention, transformers, NLP applications, computer vision systems, recommender systems, GANs, reinforcement learning, Gaussian processes, and hyperparameter optimization. Code examples use PyTorch for portability. For classical context, compare these notes with [machine learning](/cs/machine-learning/); for prerequisites, see [linear algebra](/math/linear-algebra/) and [probability](/math/probability-and-random-variables/).

```mermaid
flowchart TB
  Data["Data as tensors: tabular (N,d), images (N,C,H,W), tokens (N,T)"] --> Model["Differentiable model: linear layers, MLPs, CNNs, RNNs, attention"]
  Model --> Pred["Predictions: scalar, class logits, token logits, boxes, masks, scores"]
  Target["Targets or self-supervised labels"] --> Loss["Scalar objective"]
  Pred --> Loss
  Loss --> Grad["Automatic differentiation computes parameter gradients"]
  Grad --> Optim["Optimizer and schedule update weights"]
  Optim -. "new parameters for next minibatch" .-> Model
  Model --> Eval["Validation and deployment checks"]
  Eval --> Data
```

This overview diagram shows the repeated contract behind the chapter sequence. Data enters as shaped tensors, a differentiable model produces task-specific predictions, a scalar loss drives automatic differentiation, and an optimizer updates parameters for the next minibatch. The validation loop is separate from the gradient path because evaluation should measure behavior rather than train the model.

1. [Tensors and Data Preprocessing](/cs/deep-learning/tensors-data-preprocessing)
2. [Math for Deep Learning](/cs/deep-learning/math-for-deep-learning)
3. [Linear Regression and Training Loops](/cs/deep-learning/linear-regression-training)
4. [Softmax Classification and Generalization](/cs/deep-learning/softmax-classification-generalization)
5. [Multilayer Perceptrons and Regularization](/cs/deep-learning/multilayer-perceptrons-regularization)
6. [PyTorch Builders Guide](/cs/deep-learning/pytorch-builders-guide)
7. [Convolutional Neural Networks](/cs/deep-learning/convolutional-neural-networks)
8. [Modern CNNs](/cs/deep-learning/modern-cnns)
9. [Sequence Modeling and RNNs](/cs/deep-learning/sequence-modeling-rnns)
10. [Gated RNNs and Sequence-to-Sequence](/cs/deep-learning/gated-rnns-seq2seq)
11. [Attention and Transformers](/cs/deep-learning/attention-transformers)
12. [Efficient Sequence Modeling](/cs/deep-learning/efficient-sequence-modeling)
13. [Pretrained Transformers and BERT](/cs/deep-learning/pretrained-transformers-nlp)
14. [Optimization Algorithms](/cs/deep-learning/optimization-algorithms)
15. [Computational Performance](/cs/deep-learning/computational-performance)
16. [Computer Vision Applications](/cs/deep-learning/computer-vision-applications)
17. [NLP Pretraining and Applications](/cs/deep-learning/nlp-pretraining-and-applications)
18. [Generative Adversarial Networks](/cs/deep-learning/generative-adversarial-networks)
19. [Recommender Systems](/cs/deep-learning/recommender-systems)
20. [Reinforcement Learning and Bayesian Tuning](/cs/deep-learning/reinforcement-learning-and-bayesian-tuning)
