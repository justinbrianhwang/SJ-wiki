---
title: Convolutional Neural Networks
sidebar_position: 8
---

# Convolutional Neural Networks

Convolutional neural networks exploit the structure of images. A fully connected layer treats every pixel position as unrelated to every other position, but images have local patterns, repeated motifs, and spatial neighborhoods. D2L develops CNNs by moving from the idea of translation-aware feature extraction to the concrete cross-correlation operation used in deep learning libraries.

The core insight is parameter sharing. A small kernel slides across an image and applies the same weights at every location. This makes the model efficient, encourages it to detect the same pattern anywhere in the image, and builds feature maps that preserve spatial layout. Padding, stride, channels, pooling, and stacked convolutional layers then turn this simple operation into a complete architecture such as LeNet.

## Definitions

For an input image $X$ and kernel $K$, the two-dimensional **cross-correlation** output is

$$
Y_{i,j} =
\sum_{a=0}^{h_k-1}
\sum_{b=0}^{w_k-1}
X_{i+a,j+b}K_{a,b}.
$$

Deep learning libraries usually call this operation convolution, even though mathematical convolution flips the kernel before applying it. Since kernels are learned, the distinction rarely matters for neural network training.

A **convolutional layer** learns one or more kernels and optionally a bias. With multiple input channels, each output channel sums cross-correlations over all input channels. If $X$ has $c_i$ input channels and the layer has $c_o$ output channels, the kernel tensor has shape $(c_o,c_i,h_k,w_k)$ in PyTorch.

**Padding** adds rows and columns around the input. It controls spatial size and lets border pixels participate in more windows. **Stride** is the step size between adjacent kernel positions. A larger stride downsamples the feature map.

For input height $h$, kernel height $k$, padding $p$, and stride $s$, the output height is

$$
\left\lfloor \frac{h + 2p - k}{s} \right\rfloor + 1.
$$

The same formula applies to width.

**Pooling** aggregates local neighborhoods without learned weights. Max pooling returns the largest value in each window; average pooling returns the mean. Pooling adds local translation tolerance and often reduces spatial resolution.

**LeNet** is an early CNN for digit recognition. It alternates convolution, nonlinear activation, pooling, and fully connected layers.

## Key results

Convolutions encode three useful assumptions for images. Locality says nearby pixels are more strongly related than distant pixels. Translation equivariance says shifting an input should shift the feature map in a corresponding way. Parameter sharing says the same detector can be useful at many locations.

For a single-channel input of size $h \times w$ and a kernel of size $k_h \times k_w$, a fully connected layer from all pixels to one hidden unit uses $hw$ weights. A convolutional detector uses only $k_hk_w$ weights and applies them everywhere. With many feature maps, this savings becomes dramatic.

A $1 \times 1$ convolution does not mix spatial neighborhoods, but it mixes channels at each pixel location. If the input has $c_i$ channels and the output has $c_o$ channels, a $1 \times 1$ convolution learns a matrix-like transformation from $\mathbb{R}^{c_i}$ to $\mathbb{R}^{c_o}$ at every spatial position. D2L uses this idea to explain later architectures such as NiN and GoogLeNet.

Pooling is not the same as convolution. It has no learned kernel and usually discards precise spatial information. This can help classification, where exact location may be less important, but it can hurt dense prediction tasks such as segmentation if overused.

Stacking small kernels increases the receptive field. Two $3 \times 3$ convolutional layers without dilation give a $5 \times 5$ effective receptive field, while using fewer parameters than one dense $5 \times 5$ layer with the same channel counts.

Channel dimensions are part of the model's learned representation. Early layers may detect edges or color contrasts, while later layers combine channels into textures, parts, and object-level patterns. A convolution with $c_i$ input channels, $c_o$ output channels, and kernel size $k_h \times k_w$ has $c_oc_ik_hk_w$ weights, plus $c_o$ biases when bias is enabled. This makes channel growth a major driver of parameter count and computation.

The receptive field of a unit is the region of the original input that can affect it. Deeper layers have larger receptive fields because each convolution composes neighborhoods from the previous feature map. However, the theoretical receptive field can be larger than the effective region that strongly influences the output, especially early in training. This is one reason architecture design balances depth, stride, pooling, and skip connections.

Layout conventions matter when translating formulas into code. D2L's mathematical images are often written as height-by-width arrays, but PyTorch stores batches as `(N, C, H, W)`. Most silent CNN mistakes are not in the convolution formula; they are in reshaping, flattening, or feeding a channels-last tensor into a channels-first layer.

Translation equivariance should be distinguished from translation invariance. A convolutional feature map is equivariant: shifting the input tends to shift the feature response. Pooling, striding, and global average pooling add degrees of invariance by reducing the importance of exact position. Classification often wants some invariance, but detection and segmentation need enough equivariance to locate objects accurately.

LeNet is historically small, but its pattern remains recognizable. Convolutional layers learn local features, pooling reduces resolution, and dense layers map the final representation to class logits. Modern networks replace sigmoid with ReLU-like activations, add normalization, and use deeper blocks, but the same tensor flow from image to feature maps to classifier is still present.

## Visual

```mermaid
flowchart TB
  subgraph Generic["Generic CNN feature block"]
    direction TB
    GI["Feature map: #lsqb;N, C_in, H, W"]"] --> GC["Conv k x k, stride s, padding p -> #lsqb;N, C_out, H_out, W_out"]"]
    GC --> GBN["BatchNorm2d C_out"]
    GBN --> GR["ReLU"]
    GR --> GP["Optional pool 2 x 2, stride 2 -> #lsqb;N, C_out, H_out/2, W_out/2"]"]
  end

  subgraph LeNet["LeNet-5 style classifier for 28 x 28 grayscale digits"]
    direction TB
    X["Input image batch: #lsqb;N, 1, 28, 28"]"] --> C1["C1: Conv 5 x 5, 6 channels, pad 2 -> #lsqb;N, 6, 28, 28"]"]
    C1 --> A1["Sigmoid or modern ReLU"]
    A1 --> S2["S2: AvgPool 2 x 2, stride 2 -> #lsqb;N, 6, 14, 14"]"]
    S2 --> C3["C3: Conv 5 x 5, 16 channels, valid -> #lsqb;N, 16, 10, 10"]"]
    C3 --> A3["Sigmoid or modern ReLU"]
    A3 --> S4["S4: AvgPool 2 x 2, stride 2 -> #lsqb;N, 16, 5, 5"]"]
    S4 --> Flat["Flatten -> #lsqb;N, 400"]"]
    Flat --> F5["FC: 400 -> 120"]
    F5 --> A5["Activation"]
    A5 --> F6["FC: 120 -> 84"]
    F6 --> A6["Activation"]
    A6 --> Out["FC classifier: 84 -> 10 logits"]
    Out --> Prob(("Class probabilities after softmax"))
  end
```

The generic block shows the modern Conv-BN-ReLU-Pool pattern with the spatial-size controls called out on the convolution and pooling layers. The LeNet diagram then expands the classic conv-pool-conv-pool-fc-fc-fc contract, including the standard channel counts and key tensor shapes from `[N, 1, 28, 28]` to `[N, 400]` before classification. The final node separates logits from optional softmax probabilities, matching how training code usually consumes classifier outputs.

| Operation | Learned parameters | Main effect | Shape control |
|---|---:|---|---|
| Convolution | Yes | Local feature extraction | Kernel, padding, stride |
| $1 \times 1$ convolution | Yes | Channel mixing | Output channels |
| Max pooling | No | Local winner selection | Window, padding, stride |
| Average pooling | No | Local smoothing | Window, padding, stride |
| Padding | No | Border handling | Added pixels |
| Stride | No | Downsampling | Step size |

## Worked example 1: cross-correlation by hand

Problem: compute the valid cross-correlation of

$$
X =
\begin{bmatrix}
0 & 1 & 2 \\
3 & 4 & 5 \\
6 & 7 & 8
\end{bmatrix}
$$

with kernel

$$
K =
\begin{bmatrix}
0 & 1 \\
2 & 3
\end{bmatrix}.
$$

Method:

1. The input is $3 \times 3$ and the kernel is $2 \times 2$, so the valid output is $(3-2+1) \times (3-2+1) = 2 \times 2$.

2. Top-left output:

$$
Y_{0,0} =
0(0)+1(1)+3(2)+4(3)
=0+1+6+12=19.
$$

3. Top-right output:

$$
Y_{0,1} =
1(0)+2(1)+4(2)+5(3)
=0+2+8+15=25.
$$

4. Bottom-left output:

$$
Y_{1,0} =
3(0)+4(1)+6(2)+7(3)
=0+4+12+21=37.
$$

5. Bottom-right output:

$$
Y_{1,1} =
4(0)+5(1)+7(2)+8(3)
=0+5+14+24=43.
$$

Checked answer:

$$
Y =
\begin{bmatrix}
19 & 25 \\
37 & 43
\end{bmatrix}.
$$

## Worked example 2: output size with padding and stride

Problem: a convolution receives an image of size $32 \times 32$, uses a $5 \times 5$ kernel, padding $p=2$, and stride $s=2$. Find the output spatial size.

Method:

1. Use the formula for height:

$$
h_{\text{out}} =
\left\lfloor \frac{h + 2p - k}{s} \right\rfloor + 1.
$$

2. Substitute values:

$$
h_{\text{out}} =
\left\lfloor \frac{32 + 2(2) - 5}{2} \right\rfloor + 1
=
\left\lfloor \frac{31}{2} \right\rfloor + 1.
$$

3. Evaluate:

$$
\left\lfloor 15.5 \right\rfloor + 1 = 15 + 1 = 16.
$$

4. Width has the same numbers, so $w_{\text{out}}=16$.

Checked answer: the output feature map has spatial size $16 \times 16$. If the layer has $64$ output channels and the batch size is $10$, the full output shape is `(10, 64, 16, 16)`.

## Code

```python
import torch
from torch import nn

class LeNetLike(nn.Module):
    def __init__(self, num_classes=10):
        super().__init__()
        self.net = nn.Sequential(
            nn.Conv2d(1, 6, kernel_size=5, padding=2),
            nn.Sigmoid(),
            nn.AvgPool2d(kernel_size=2, stride=2),
            nn.Conv2d(6, 16, kernel_size=5),
            nn.Sigmoid(),
            nn.AvgPool2d(kernel_size=2, stride=2),
            nn.Flatten(),
            nn.Linear(16 * 5 * 5, 120),
            nn.Sigmoid(),
            nn.Linear(120, 84),
            nn.Sigmoid(),
            nn.Linear(84, num_classes),
        )

    def forward(self, x):
        return self.net(x)

model = LeNetLike()
x = torch.randn(8, 1, 28, 28)
logits = model(x)
print(logits.shape)
print("parameters:", sum(p.numel() for p in model.parameters()))
```

## Common pitfalls

- Forgetting that PyTorch convolution expects `(batch, channels, height, width)`.
- Mixing up mathematical convolution with cross-correlation. Neural network libraries learn the kernel, so the flip is usually irrelevant.
- Calculating output sizes without the floor operation.
- Using too much pooling in tasks that need precise spatial output, such as segmentation.
- Treating padding as harmless. Padding changes border statistics and can affect features near image edges.
- Flattening too early, which discards spatial structure and creates many unnecessary parameters.

## Connections

- [PyTorch builders guide](/cs/deep-learning/pytorch-builders-guide)
- [Modern CNNs](/cs/deep-learning/modern-cnns)
- [Computer vision applications](/cs/deep-learning/computer-vision-applications)
- [Linear algebra](/math/linear-algebra/)
- [Machine learning](/cs/machine-learning/)
