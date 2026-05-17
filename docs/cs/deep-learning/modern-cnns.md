---
title: Modern CNNs
sidebar_position: 9
---

# Modern CNNs

D2L's modern CNN chapters show how image models evolved from LeNet into deeper, more modular architectures. AlexNet demonstrated that large CNNs trained on GPUs could dominate image recognition. VGG made depth systematic through repeated small convolutional blocks. NiN and GoogLeNet introduced channel mixing and multi-branch computation. Batch normalization stabilized deep training. ResNet changed the default architecture by making identity paths explicit, and DenseNet pushed feature reuse even further.

These models are more than a historical sequence. They introduce reusable design ideas: blocks, bottlenecks, normalization, residual connections, concatenation, global average pooling, and computational tradeoffs between width, depth, and resolution. Modern vision models still rely on these ideas even when attention or hybrid architectures are added.

## Definitions

An **architecture block** is a repeated module with a recognizable input-output pattern. VGG blocks repeat $3 \times 3$ convolutions and pooling. Inception blocks run several branches in parallel. Residual blocks add an input to a learned transformation.

**AlexNet** is a deep CNN that uses large early kernels, ReLU activations, dropout, and GPU training. It helped establish representation learning for large-scale image classification.

**VGG** uses stacks of small $3 \times 3$ convolutions. Repeating small kernels increases depth and receptive field while keeping the design regular.

**Network in Network** uses $1 \times 1$ convolutions to create per-pixel multilayer transformations over channels and replaces some fully connected classification structure with global average pooling.

**GoogLeNet** uses Inception blocks, where $1 \times 1$, $3 \times 3$, $5 \times 5$, and pooling branches are concatenated. $1 \times 1$ convolutions often reduce channel counts before expensive convolutions.

**Batch normalization** normalizes intermediate activations using minibatch statistics during training and running estimates during evaluation. It learns scale and shift parameters after normalization.

**ResNet** uses residual blocks:

$$
y = x + F(x).
$$

If shapes differ, a projection such as a $1 \times 1$ convolution can transform $x$ before addition.

**DenseNet** concatenates previous feature maps:

$$
x_l = H_l([x_0,x_1,\ldots,x_{l-1}]).
$$

## Key results

Depth increases representational power but makes optimization harder. Residual connections help because a block can learn a residual correction around the identity. If the best transformation is close to identity, it is easier to make $F(x)$ small than to force a plain stack of layers to learn an exact identity mapping.

Batch normalization for a scalar activation within a minibatch computes

$$
\hat{x} = \frac{x-\mu_B}{\sqrt{\sigma_B^2+\epsilon}},
\qquad
y = \gamma \hat{x} + \beta.
$$

The learned $\gamma$ and $\beta$ let the network recover useful scales and offsets. Batch norm can allow larger learning rates and reduce sensitivity to initialization, but it behaves differently for small batches and sequence models.

VGG's repeated $3 \times 3$ convolutions illustrate parameter tradeoffs. Two $3 \times 3$ convolutions have an effective $5 \times 5$ receptive field and add an extra nonlinearity. Three $3 \times 3$ convolutions have an effective $7 \times 7$ receptive field. This favors deeper stacks of small kernels over one large kernel in many settings.

Inception uses parallel branches because useful visual features appear at multiple scales. However, naive branches can be expensive. A $1 \times 1$ bottleneck reduces the number of channels before a $3 \times 3$ or $5 \times 5$ convolution, cutting computation.

DenseNet's concatenation preserves earlier features instead of repeatedly transforming them by addition. This encourages feature reuse but increases channel count, so transition layers reduce spatial size and compress channels.

Batch normalization placement is a design choice, but common modern blocks use convolution, normalization, and activation as a repeated pattern. Some residual variants place normalization and activation before the convolution, creating pre-activation blocks. The practical purpose is the same: keep intermediate signals in a trainable range and make very deep networks easier to optimize.

Architecture families also reflect hardware constraints. A network with fewer parameters is not always faster if it uses operations that are inefficient on the target device. Inception reduces arithmetic with bottlenecks, VGG is regular but heavy, and residual networks offer a strong balance of accuracy and trainability. D2L's architecture tour should therefore be read as a set of design tradeoffs rather than a leaderboard.

Modern CNN design often separates the stem, stages, and head. The stem quickly maps pixels to feature maps, stages reduce resolution while increasing channels, and the head pools and classifies. This pattern makes it easier to reason about where spatial detail is lost and where semantic abstraction grows.

Residual and dense connections can be read as information-routing mechanisms. A plain deep stack forces every layer to transform the representation before passing it onward. A residual block lets information bypass a transformation by addition. A dense block lets later layers see earlier features by concatenation. These paths improve gradient flow and feature reuse, which is why they became standard components in deep vision systems.

Architecture comparison should control for training recipe. AlexNet, VGG, GoogLeNet, ResNet, and DenseNet differ in structure, but reported performance also depends on data augmentation, optimizer, learning-rate schedule, initialization, batch size, and input resolution. D2L's concise implementations are educational baselines; production comparisons need matched compute and tuned recipes.

## Visual

```mermaid
flowchart TB
  X["Input: #lsqb;N, 3, 224, 224"]"] --> C1["Conv 11 x 11, 96, stride 4 -> #lsqb;N, 96, 55, 55"]"]
  C1 --> R1["ReLU"]
  R1 --> P1["MaxPool 3 x 3, stride 2 -> #lsqb;N, 96, 27, 27"]"]
  P1 --> C2["Conv 5 x 5, 256, pad 2 -> #lsqb;N, 256, 27, 27"]"]
  C2 --> R2["ReLU"]
  R2 --> P2["MaxPool 3 x 3, stride 2 -> #lsqb;N, 256, 13, 13"]"]
  P2 --> C3["Conv 3 x 3, 384, pad 1 -> #lsqb;N, 384, 13, 13"]"]
  C3 --> R3["ReLU"]
  R3 --> C4["Conv 3 x 3, 384, pad 1 -> #lsqb;N, 384, 13, 13"]"]
  C4 --> R4["ReLU"]
  R4 --> C5["Conv 3 x 3, 256, pad 1 -> #lsqb;N, 256, 13, 13"]"]
  C5 --> R5["ReLU"]
  R5 --> P5["MaxPool 3 x 3, stride 2 -> #lsqb;N, 256, 6, 6"]"]
  P5 --> Flat["Flatten -> #lsqb;N, 9216"]"]
  Flat --> FC6["FC 4096 + ReLU + Dropout"]
  FC6 --> FC7["FC 4096 + ReLU + Dropout"]
  FC7 --> FC8["FC 1000 logits"]
  FC8 --> Out(("ImageNet class distribution"))
```

AlexNet starts with a large stride-4 convolution that rapidly reduces the 224 x 224 image, then uses three 3 x 3 convolutions before the classifier. The diagram includes the historical channel counts, pooling transitions, and the large fully connected head where dropout was applied. It makes the compute-heavy flattening point explicit: `[N, 256, 6, 6]` becomes `[N, 9216]`.

```mermaid
flowchart TB
  X["Input: #lsqb;N, 3, 224, 224"]"] --> B1["Block 1: 2 conv 3 x 3, 64 -> #lsqb;N, 64, 224, 224"]"]
  B1 --> P1["MaxPool 2 x 2, stride 2 -> #lsqb;N, 64, 112, 112"]"]
  P1 --> B2["Block 2: 2 conv 3 x 3, 128 -> #lsqb;N, 128, 112, 112"]"]
  B2 --> P2["MaxPool -> #lsqb;N, 128, 56, 56"]"]
  P2 --> B3["Block 3: 3 conv 3 x 3, 256 for VGG-16; 4 conv for VGG-19 -> #lsqb;N, 256, 56, 56"]"]
  B3 --> P3["MaxPool -> #lsqb;N, 256, 28, 28"]"]
  P3 --> B4["Block 4: 3 conv 3 x 3, 512 for VGG-16; 4 conv for VGG-19 -> #lsqb;N, 512, 28, 28"]"]
  B4 --> P4["MaxPool -> #lsqb;N, 512, 14, 14"]"]
  P4 --> B5["Block 5: 3 conv 3 x 3, 512 for VGG-16; 4 conv for VGG-19 -> #lsqb;N, 512, 14, 14"]"]
  B5 --> P5["MaxPool -> #lsqb;N, 512, 7, 7"]"]
  P5 --> Flat["Flatten -> #lsqb;N, 25088"]"]
  Flat --> FC1["FC 4096 + ReLU + Dropout"]
  FC1 --> FC2["FC 4096 + ReLU + Dropout"]
  FC2 --> Head["FC 1000 logits"]
  Head --> Out(("Class distribution"))
```

VGG is intentionally regular: each stage keeps the same spatial size inside the repeated 3 x 3 convolutions, then halves resolution with max pooling. The diagram distinguishes VGG-16 and VGG-19 by the number of convolutions in the later blocks while preserving the same 224 -> 112 -> 56 -> 28 -> 14 -> 7 spatial path. It also shows why the original classifier head is parameter-heavy after flattening 512 x 7 x 7 features.

```mermaid
flowchart TB
  X["Input feature map: #lsqb;N, 192, H, W"]"] --> B1R["Branch 1 reduce: Conv 1 x 1, 64 -> #lsqb;N, 64, H, W"]"]
  B1R --> B1["Branch 1 output: 1 x 1 features"]
  X --> B3R["Branch 2 reduce: Conv 1 x 1, 96 -> #lsqb;N, 96, H, W"]"]
  B3R --> B3["Conv 3 x 3, 128, pad 1 -> #lsqb;N, 128, H, W"]"]
  X --> B5R["Branch 3 reduce: Conv 1 x 1, 16 -> #lsqb;N, 16, H, W"]"]
  B5R --> B5["Conv 5 x 5, 32, pad 2 -> #lsqb;N, 32, H, W"]"]
  X --> BP["Branch 4: MaxPool 3 x 3, stride 1, pad 1 -> #lsqb;N, 192, H, W"]"]
  BP --> BPR["Conv 1 x 1, 32 -> #lsqb;N, 32, H, W"]"]
  B1 --> Cat["Concatenate channels -> #lsqb;N, 256, H, W"]"]
  B3 --> Cat
  B5 --> Cat
  BPR --> Cat
```

The Inception module runs multiple receptive-field choices in parallel while preserving the same height and width in every branch. The 1 x 1 reductions before 3 x 3 and 5 x 5 convolutions are the bottlenecks that keep the expensive branches tractable. Concatenation is along channels, so the example branch widths combine into 256 output channels.

```mermaid
flowchart TB
  X["Block input x: #lsqb;N, C, H, W"]"] --> R1["1 x 1 conv, C_mid, stride s -> #lsqb;N, C_mid, H/s, W/s"]"]
  R1 --> BN1["BatchNorm + ReLU"]
  BN1 --> R2["3 x 3 conv, C_mid, pad 1 -> #lsqb;N, C_mid, H/s, W/s"]"]
  R2 --> BN2["BatchNorm + ReLU"]
  BN2 --> R3["1 x 1 conv, 4*C_mid -> #lsqb;N, 4*C_mid, H/s, W/s"]"]
  R3 --> BN3["BatchNorm"]
  X --> Match{"Shape matches [N, 4*C_mid, H/s, W/s]?"}
  Match -->|"yes"| Id["Identity shortcut"]
  Match -->|"no"| Proj["1 x 1 projection, stride s, 4*C_mid"]
  Id --> Add(("Add"))
  Proj --> Add
  BN3 --> Add
  Add --> Act["ReLU"]
  Act --> Y["Block output: #lsqb;N, 4*C_mid, H/s, W/s"]"]
```

![The original residual learning block shows a two-layer residual branch added to an identity shortcut before a ReLU.](https://ar5iv.labs.arxiv.org/html/1512.03385/assets/x2.png)

*Figure: Original residual learning block from [He et al., 2015](https://arxiv.org/abs/1512.03385) — embedded under educational fair use with attribution.*

This bottleneck block shows ResNet's expansion factor of 4: the residual branch compresses with 1 x 1, processes with 3 x 3, then expands back to `4*C_mid`. The shortcut is identity only when channel and spatial shapes already match; otherwise a 1 x 1 projection aligns both the channel count and stride. The addition node is the explicit residual merge.

```mermaid
flowchart TB
  In["Input image: #lsqb;N, 3, 224, 224"]"] --> Stem["Stem: Conv 7 x 7, 64, stride 2 -> #lsqb;N, 64, 112, 112"]"]
  Stem --> Pool["MaxPool 3 x 3, stride 2 -> #lsqb;N, 64, 56, 56"]"]
  Pool --> S1["conv2_x: 3 bottlenecks #lsqb;1 x 1,64; 3 x 3,64; 1 x 1,256"] -> ["N, 256, 56, 56"]"]
  S1 --> S2["conv3_x: 4 bottlenecks #lsqb;1 x 1,128; 3 x 3,128; 1 x 1,512"], first stride 2 -> ["N, 512, 28, 28"]"]
  S2 --> S3["conv4_x: 6 bottlenecks #lsqb;1 x 1,256; 3 x 3,256; 1 x 1,1024"], first stride 2 -> ["N, 1024, 14, 14"]"]
  S3 --> S4["conv5_x: 3 bottlenecks #lsqb;1 x 1,512; 3 x 3,512; 1 x 1,2048"], first stride 2 -> ["N, 2048, 7, 7"]"]
  S4 --> GAP["Global average pool over 7 x 7 -> #lsqb;N, 2048"]"]
  GAP --> FC["FC 1000 logits"]
  FC --> Out(("Class distribution"))
  Pool -. "stage shortcut projections when shape changes" .-> S1
  S1 -. "projection shortcut at first conv3_x block" .-> S2
  S2 -. "projection shortcut at first conv4_x block" .-> S3
  S3 -. "projection shortcut at first conv5_x block" .-> S4
```

The ResNet-50 stage diagram expands the architecture into its stem, four residual stages, and global-average-pooling head. It uses the standard ImageNet shapes: 56 x 56 for `conv2_x`, then 28 x 28, 14 x 14, and 7 x 7 as stages downsample. Dotted arrows mark where projection shortcuts are required because the first block of a stage changes resolution or channel count.

```mermaid
flowchart TB
  X0["Dense block input x0: #lsqb;N, C0, H, W"]"] --> L1["Layer 1: BN-ReLU-Conv 3 x 3, growth k -> x1 #lsqb;N, k, H, W"]"]
  X0 --> Cat1["Concat #lsqb;x0, x1"] -> ["N, C0+k, H, W"]"]
  L1 --> Cat1
  Cat1 --> L2["Layer 2: BN-ReLU-Conv 3 x 3, growth k -> x2 #lsqb;N, k, H, W"]"]
  Cat1 --> Cat2["Concat #lsqb;x0, x1, x2"] -> ["N, C0+2k, H, W"]"]
  L2 --> Cat2
  Cat2 --> L3["Layer 3: BN-ReLU-Conv 3 x 3, growth k -> x3 #lsqb;N, k, H, W"]"]
  Cat2 --> Cat3["Concat #lsqb;x0, x1, x2, x3"] -> ["N, C0+3k, H, W"]"]
  L3 --> Cat3
  Cat3 --> Trans["Transition: 1 x 1 conv compression theta + avg pool 2 x 2 -> #lsqb;N, floor(theta*(C0+3k)), H/2, W/2"]"]
```

![The DenseNet overview shows dense blocks connected by transition layers, with each block reusing features from earlier layers.](https://ar5iv.labs.arxiv.org/html/1608.06993/assets/x2.png)

*Figure: DenseNet architecture overview from [Huang et al., 2016](https://arxiv.org/abs/1608.06993) — embedded under educational fair use with attribution.*

DenseNet differs from ResNet by concatenating features instead of adding them. Every new layer contributes `k` growth-rate channels, so the dense block output channel count grows from `C0` to `C0+3k` in this three-layer example. The transition layer then compresses channels and downsamples spatial resolution to control memory.

```mermaid
flowchart TB
  X["Input feature map: #lsqb;N, C_in, H, W"]"] --> DW["Depthwise conv k x k, groups C_in -> #lsqb;N, C_in, H, W"]"]
  DW --> DWBN["BatchNorm + ReLU6"]
  DWBN --> PW["Pointwise conv 1 x 1, C_out -> #lsqb;N, C_out, H, W"]"]
  PW --> PWBN["BatchNorm + ReLU6"]
  PWBN --> Y["Output feature map"]
  X -. "spatial filtering per channel" .-> DW
  DWBN -. "channel mixing happens only in 1 x 1 conv" .-> PW
```

MobileNet's depthwise-separable block splits spatial filtering from channel mixing. The depthwise convolution applies one spatial kernel per input channel, and the 1 x 1 pointwise convolution then mixes channels to produce `C_out`. This is the main architectural reason MobileNet blocks use far fewer parameters and multiply-adds than a dense k x k convolution.

| Family | Main design idea | Benefit | Cost or caution |
|---|---|---|---|
| AlexNet | Large CNN with ReLU and dropout | Scaled CNNs to ImageNet | Large early kernels are expensive |
| VGG | Repeated small conv blocks | Simple, regular, deep | Many parameters in classifier |
| NiN | $1 \times 1$ channel MLPs | Local channel mixing | Less spatial multi-scale structure |
| GoogLeNet | Inception branches | Multi-scale features | More complex block design |
| BatchNorm | Normalize activations | Stabilizes training | Batch-size dependence |
| ResNet | Residual addition | Very deep optimization | Shape alignment required |
| DenseNet | Feature concatenation | Strong feature reuse | Channel growth |

## Worked example 1: parameters saved by a bottleneck

Problem: compare the parameter count of a direct $5 \times 5$ convolution from $192$ input channels to $32$ output channels with a bottleneck design that first uses a $1 \times 1$ convolution from $192$ to $16$ channels, then a $5 \times 5$ convolution from $16$ to $32$ channels. Ignore biases.

Method:

1. Direct convolution parameters:

$$
32 \cdot 192 \cdot 5 \cdot 5
= 32 \cdot 192 \cdot 25.
$$

2. Compute:

$$
192 \cdot 25 = 4800,
\qquad
32 \cdot 4800 = 153600.
$$

3. Bottleneck $1 \times 1$ parameters:

$$
16 \cdot 192 \cdot 1 \cdot 1 = 3072.
$$

4. Bottleneck $5 \times 5$ parameters:

$$
32 \cdot 16 \cdot 5 \cdot 5
=32 \cdot 16 \cdot 25
=12800.
$$

5. Total bottleneck parameters:

$$
3072 + 12800 = 15872.
$$

6. Reduction factor:

$$
\frac{153600}{15872} \approx 9.68.
$$

Checked answer: the bottleneck design uses $15{,}872$ parameters instead of $153{,}600$, roughly a $9.7$ times reduction. This is why Inception-style blocks use $1 \times 1$ reductions before expensive kernels.

## Worked example 2: residual block shape matching

Problem: an input tensor has shape `(batch, 64, 56, 56)`. A residual branch uses a convolutional path that outputs `(batch, 128, 28, 28)`. Can the original input be added directly to the branch output? If not, specify a projection.

Method:

1. Addition requires identical shapes, or at least broadcast-compatible shapes. Residual feature maps are meant to align elementwise, so the channel and spatial dimensions should match exactly.
2. Compare channels: input has $64$ channels, branch has $128$ channels. They do not match.
3. Compare height and width: input has $56 \times 56$, branch has $28 \times 28$. They do not match.
4. Use a projection shortcut with output channels $128$ and stride $2$:

$$
\mathrm{shortcut}(x)=\mathrm{Conv}_{1 \times 1}(x;\ \text{out}=128,\ \text{stride}=2).
$$

5. The $1 \times 1$ projection changes channels from $64$ to $128$, and stride $2$ changes spatial size from $56 \times 56$ to $28 \times 28$.

Checked answer: direct addition is invalid. A $1 \times 1$ convolution with stride $2$ and $128$ output channels produces a shortcut tensor of shape `(batch, 128, 28, 28)`, which can be added to the residual branch.

## Code

```python
import torch
from torch import nn

class ResidualBlock(nn.Module):
    def __init__(self, in_channels, out_channels, stride=1):
        super().__init__()
        self.body = nn.Sequential(
            nn.Conv2d(in_channels, out_channels, kernel_size=3,
                      stride=stride, padding=1, bias=False),
            nn.BatchNorm2d(out_channels),
            nn.ReLU(),
            nn.Conv2d(out_channels, out_channels, kernel_size=3,
                      padding=1, bias=False),
            nn.BatchNorm2d(out_channels),
        )
        if in_channels != out_channels or stride != 1:
            self.shortcut = nn.Sequential(
                nn.Conv2d(in_channels, out_channels, kernel_size=1,
                          stride=stride, bias=False),
                nn.BatchNorm2d(out_channels),
            )
        else:
            self.shortcut = nn.Identity()
        self.activation = nn.ReLU()

    def forward(self, x):
        return self.activation(self.body(x) + self.shortcut(x))

block = ResidualBlock(64, 128, stride=2)
x = torch.randn(4, 64, 56, 56)
y = block(x)
print(y.shape)
```

## Common pitfalls

- Adding residual tensors with mismatched channel or spatial dimensions.
- Forgetting that batch normalization has different training and evaluation behavior.
- Comparing architectures by depth alone without considering width, resolution, and compute.
- Placing global average pooling too early and destroying useful spatial detail.
- Assuming $1 \times 1$ convolutions are trivial. They can dominate channel mixing and parameter counts.
- Treating named architectures as fixed recipes rather than reusable design patterns.

## Connections

- [Convolutional neural networks](/cs/deep-learning/convolutional-neural-networks)
- [Computer vision applications](/cs/deep-learning/computer-vision-applications)
- [Optimization algorithms](/cs/deep-learning/optimization-algorithms)
- [PyTorch builders guide](/cs/deep-learning/pytorch-builders-guide)
- [Machine learning](/cs/machine-learning/)
