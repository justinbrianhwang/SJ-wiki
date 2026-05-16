---
title: "PointPillars (Lang et al., 2019)"
sidebar_position: 20
---

# PointPillars (Lang et al., 2019)

PointPillars, introduced by Lang, Vora, Caesar, Zhou, Yang, and Beijbom in the CVPR 2019 paper "PointPillars: Fast Encoders for Object Detection from Point Clouds," is a LiDAR 3D object detection architecture built around a simple idea: do not voxelize the vertical direction if the downstream detector mostly wants a bird's-eye-view representation. Instead, group points into vertical columns, learn a PointNet-style feature for each nonempty column, scatter those features into a 2D pseudo-image, and use a fast 2D convolutional detector.

The method sits between older hand-engineered BEV encoders and heavier voxel networks. It matters because real autonomous vehicles cannot spend the whole compute budget on 3D detection; the perception stack must also run tracking, fusion, prediction, planning, diagnostics, and safety monitors. PointPillars showed that a learned point-cloud encoder could be both accurate and fast enough for real-time driving workloads, and it remains a standard baseline for [3D perception](/cs/autonomous-driving/perception-object-detection-and-segmentation), [sensor fusion](/cs/autonomous-driving/sensor-fusion), and BEV planning systems.

## Definitions

A **pillar** is a vertical column in the point cloud. The $x$-$y$ ground plane is divided into a regular grid, but the $z$ axis is not subdivided. A pillar is therefore like a voxel with unbounded height inside the configured detection range. If the grid cell size is $\Delta x \times \Delta y$, a point $(x,y,z,r)$ with reflectance $r$ is assigned to

$$
i = \left\lfloor \frac{x - x_{\min}}{\Delta x} \right\rfloor,\qquad
j = \left\lfloor \frac{y - y_{\min}}{\Delta y} \right\rfloor.
$$

PointPillars decorates each point with local geometry before the PointNet layer. In the paper's notation, a point is augmented with reflectance, offsets from the mean of points in the pillar, and offsets from the pillar center. A typical decorated vector is

$$
\hat{p} = [x,y,z,r,x-x_c,y-y_c,z-z_c,x-x_p,y-y_p],
$$

where $(x_c,y_c,z_c)$ is the mean of the points in the pillar and $(x_p,y_p)$ is the pillar center in the ground grid. This gives the network both absolute position and local shape information.

The **pillar feature network** applies a shared linear layer, normalization, nonlinearity, and a symmetric pooling operation across points in each pillar. Because point order is arbitrary, the pooling step is essential: it makes the feature invariant to how points are listed inside the pillar. The output is one feature vector per nonempty pillar.

The **pseudo-image** is the dense BEV tensor obtained by scattering nonempty pillar features back into their grid locations. Empty cells are zeros. After this scatter, the rest of the detector can be a standard 2D CNN backbone and SSD-style detection head. This design is the key difference from VoxelNet-style systems, which use 3D convolution in voxel space before collapsing to BEV.

The target output is a set of oriented 3D boxes. A box is commonly parameterized as

$$
b=(x,y,z,w,l,h,\theta,c,s),
$$

with center, dimensions, yaw angle, class $c$, and confidence score $s$. The detector regresses offsets relative to anchors in BEV and classifies object categories such as cars, pedestrians, and cyclists.

## Key results

The core result is architectural: a learned LiDAR encoder does not require 3D convolution if the vertical structure can be summarized per ground-plane cell. PointPillars keeps the useful part of PointNet, namely permutation-invariant local feature learning, and moves the expensive spatial reasoning into efficient 2D convolution.

The pipeline is:

1. Filter points to a fixed 3D range.
2. Partition the $x$-$y$ plane into pillars.
3. Keep at most $P$ nonempty pillars and at most $N$ points per pillar.
4. Decorate points with local offsets.
5. Apply the pillar feature network and max-pool across the points in each pillar.
6. Scatter pillar features into a BEV pseudo-image.
7. Run a 2D CNN backbone.
8. Predict oriented 3D boxes with a dense detection head.

The paper reports that PointPillars significantly outperformed prior encoders in the speed-accuracy tradeoff on KITTI. The abstract states that the full LiDAR-only pipeline ran at 62 Hz while improving 3D and BEV detection performance, and that a faster variant matched then state-of-the-art performance at 105 Hz. The paper also emphasizes that this was achieved without image fusion, which is important: the gain came from the point-cloud representation and network design, not from adding camera information.

Mathematically, the pillar feature for pillar $k$ can be viewed as

$$
f_k = \max_{n=1,\dots,N_k} \phi(\hat{p}_{kn}),
$$

where $\phi$ is a shared learned point function and max is channelwise. The scatter operation maps $f_k$ to pseudo-image cell $(i_k,j_k)$. The 2D backbone then learns spatial context:

$$
F_{\mathrm{BEV}} = \mathrm{CNN}_{2D}(\mathrm{scatter}(\{f_k\})).
$$

This representation trades vertical detail for speed. That is often reasonable for road driving because many objects occupy the ground plane and are separated more strongly in BEV than in perspective image space. But the tradeoff is not free: stacked objects, overpasses, steep grades, and unusual vertical structure can be harder to model if all height detail is compressed into one pillar feature.

PointPillars also helps explain later designs such as [CenterPoint](/cs/autonomous-driving/centerpoint): the encoder and the output representation can be improved separately. PointPillars is mainly about fast LiDAR encoding; CenterPoint is mainly about detecting and tracking objects as center points.

## Visual

```mermaid
flowchart LR
  A["Raw LiDAR points"] --> B["Crop range and grid x-y plane"]
  B --> C["Nonempty vertical pillars"]
  C --> D["Decorate each point with local offsets"]
  D --> E["Shared point MLP plus max pool"]
  E --> F["Scatter to BEV pseudo-image"]
  F --> G["2D CNN backbone"]
  G --> H["SSD-style 3D box head"]
  H --> I["Cars, pedestrians, cyclists"]
```

| Representation | Vertical handling | Main compute | Strength | Weakness |
|---|---:|---|---|---|
| Hand-crafted BEV grid | Collapsed manually | 2D CNN | Fast and simple | Fixed features may miss geometry |
| VoxelNet-style voxels | Discretized into $z$ bins | 3D then 2D CNN | Richer 3D structure | 3D convolution cost |
| PointPillars | One learned feature per column | PointNet plus 2D CNN | Fast learned encoding | Compresses vertical detail |
| Raw point transformer | No fixed grid or weak grid | Attention or point ops | Flexible geometry | Often expensive at full scale |

## Worked example 1: Assigning points to pillars

Problem: A detector uses $x \in [0, 4)$ meters, $y \in [-2,2)$ meters, and a pillar size $\Delta x=\Delta y=1$ meter. Three LiDAR points are

$$
p_1=(0.2,-1.4,0.6,0.8),\quad
p_2=(0.7,-1.1,0.4,0.7),\quad
p_3=(2.3,0.2,1.2,0.5).
$$

Find their pillar indices and the mean-centered offsets for $p_1$ inside its pillar.

1. The grid index formula is

$$
i=\left\lfloor \frac{x-0}{1}\right\rfloor,\qquad
j=\left\lfloor \frac{y-(-2)}{1}\right\rfloor.
$$

2. For $p_1$, $i=\lfloor 0.2\rfloor=0$ and $j=\lfloor 0.6\rfloor=0$, so $p_1$ is in pillar $(0,0)$.

3. For $p_2$, $i=\lfloor 0.7\rfloor=0$ and $j=\lfloor 0.9\rfloor=0$, so $p_2$ is also in pillar $(0,0)$.

4. For $p_3$, $i=\lfloor 2.3\rfloor=2$ and $j=\lfloor 2.2\rfloor=2$, so $p_3$ is in pillar $(2,2)$.

5. The mean of the two points in pillar $(0,0)$ is

$$
\bar{x}=\frac{0.2+0.7}{2}=0.45,\quad
\bar{y}=\frac{-1.4-1.1}{2}=-1.25,\quad
\bar{z}=\frac{0.6+0.4}{2}=0.5.
$$

6. The mean-centered offset for $p_1$ is

$$
(x-\bar{x},y-\bar{y},z-\bar{z})=(-0.25,-0.15,0.10).
$$

Answer: $p_1$ and $p_2$ share pillar $(0,0)$, $p_3$ is in pillar $(2,2)$, and the local offset for $p_1$ relative to its pillar mean is $(-0.25,-0.15,0.10)$.

Check: The two points in pillar $(0,0)$ have offsets that sum to zero in each coordinate, as mean-centered offsets should.

## Worked example 2: Estimating the pseudo-image size

Problem: A LiDAR detector covers $x \in [0, 70.4]$ m and $y \in [-40,40]$ m. It uses $\Delta x=\Delta y=0.16$ m. How large is the BEV pseudo-image before the CNN backbone, and how many cells does it contain?

1. Compute the number of cells in $x$:

$$
W_x=\frac{70.4-0}{0.16}=440.
$$

2. Compute the number of cells in $y$:

$$
W_y=\frac{40-(-40)}{0.16}=\frac{80}{0.16}=500.
$$

3. The pseudo-image has spatial size $440 \times 500$ if indexed as range-by-width, or $500 \times 440$ depending on tensor convention.

4. The number of spatial cells is

$$
440\cdot 500=220000.
$$

5. If the pillar feature dimension is $C=64$, the dense pseudo-image has

$$
220000\cdot 64=14080000
$$

feature values.

Answer: the pseudo-image has 220,000 BEV cells and about 14.1 million feature values at 64 channels.

Check: Most cells are empty before scattering because LiDAR point clouds are sparse. PointPillars exploits sparsity before the scatter, then lets dense 2D convolution handle spatial reasoning.

## Code

```python
import torch
import torch.nn as nn

class PillarFeatureNet(nn.Module):
    def __init__(self, in_dim=9, out_dim=64):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(in_dim, out_dim, bias=False),
            nn.BatchNorm1d(out_dim),
            nn.ReLU(inplace=True),
        )

    def forward(self, pillars, mask):
        # pillars: [P, N, D], mask: [P, N] with True for real points
        p, n, d = pillars.shape
        x = self.net(pillars.reshape(p * n, d)).reshape(p, n, -1)
        x = x.masked_fill(~mask.unsqueeze(-1), float("-inf"))
        return x.max(dim=1).values

def scatter_to_bev(features, indices, height, width):
    # features: [P, C], indices: [P, 2] as row, col
    bev = features.new_zeros(features.shape[1], height, width)
    rows, cols = indices[:, 0].long(), indices[:, 1].long()
    bev[:, rows, cols] = features.T
    return bev.unsqueeze(0)

pillars = torch.randn(128, 32, 9)
mask = torch.rand(128, 32) > 0.2
indices = torch.randint(0, 64, (128, 2))
features = PillarFeatureNet()(pillars, mask)
bev = scatter_to_bev(features, indices, height=64, width=64)
print(bev.shape)
```

## Common pitfalls

- Treating pillars as ordinary 3D voxels. A pillar has no vertical binning; its vertical geometry is compressed into a learned feature.
- Forgetting point-order invariance. The PointNet-style shared MLP plus max-pooling is what makes the pillar feature independent of point ordering.
- Comparing runtime without the same range, grid size, and backbone. Pillar count and pseudo-image size dominate the speed profile.
- Assuming PointPillars solves sensor fusion. The original system is LiDAR-only; camera fusion is a separate design choice.
- Using too large a pillar size. Coarse grids are fast but can merge nearby pedestrians, cyclists, or curb objects.
- Using too small a pillar size. Fine grids improve geometry but increase memory and CNN cost.
- Ignoring coordinate conventions. BEV row-column order, ego-frame orientation, and yaw sign errors can silently destroy labels.

## Connections

- [Perception, object detection, and segmentation](/cs/autonomous-driving/perception-object-detection-and-segmentation)
- [Sensors, cameras, LiDAR, radar, and IMU](/cs/autonomous-driving/sensors-cameras-lidar-radar-imu)
- [Sensor fusion](/cs/autonomous-driving/sensor-fusion)
- [CenterPoint](/cs/autonomous-driving/centerpoint)
- [MV3D sonar](/cs/autonomous-driving/mv3d-sonar)
- [Deep learning](/cs/deep-learning/)
- Further reading: VoxelNet, SECOND, PIXOR, AVOD, PointNet, CenterPoint, and BEVFusion.
