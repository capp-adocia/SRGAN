# SRGAN-PyTorch

## Overview

This repository contains an op-for-op PyTorch reimplementation
of [Photo-Realistic Single Image Super-Resolution Using a Generative Adversarial Network](https://arxiv.org/abs/1609.04802v5).

## Table of contents

- [SRGAN-PyTorch](#srgan-pytorch)
  - [Overview](#overview)
  - [Table of contents](#table-of-contents)
  - [Download weights](#download-weights)
  - [Download datasets](#download-datasets)
  - [How Test and Train](#how-test-and-train)
    - [Test srgan\_x4](#test-srgan_x4)
    - [Test srresnet\_x4](#test-srresnet_x4)
    - [Train srresnet\_x4](#train-srresnet_x4)
    - [Resume train srresnet\_x4](#resume-train-srresnet_x4)
    - [Train srgan\_x4](#train-srgan_x4)
    - [Resume train srgan\_x4](#resume-train-srgan_x4)
  - [Result](#result)

## Download weights

Download all available model weights.

```shell
# Download `SRGAN_x4-SRGAN_ImageNet.pth.tar` weights to `./results/pretrained_models`
$ bash ./scripts/download_weights.sh SRGAN_x4-SRGAN_ImageNet
# Download `SRResNet_x4-SRGAN_ImageNet.pth.tar` weights to `./results/pretrained_models`
$ bash ./scripts/download_weights.sh SRResNet_x4-SRGAN_ImageNet
# Download `DiscriminatorForVGG_x4-SRGAN_ImageNet.pth.tar` weights to `./results/pretrained_models`
$ bash ./scripts/download_weights.sh DiscriminatorForVGG_x4-SRGAN_ImageNet
```

## Download datasets

These train images are randomly selected from the verification part of the ImageNet2012 classification dataset.

```shell
$ bash ./scripts/download_datasets.sh SRGAN_ImageNet
```

It is convenient to download some commonly used test data sets here.

```shell
$ bash ./scripts/download_datasets.sh Set5
```

## How Test and Train

Both training and testing only need to modify yaml file.

Set5 is used as the test benchmark in the project, and you can modify it by yourself.

If you need to test the effect of the model, download the test dataset.

```shell
$ bash ./scripts/download_datasets.sh Set5
```

### Test srgan_x4

```shell
$ python3 test.py --config_path ./configs/test/SRGAN_x4-SRGAN_ImageNet-Set5.yaml
```

### Test srresnet_x4

```shell
$ python3 test.py --config_path ./configs/test/SRResNet_x4-SRGAN_ImageNet-Set5.yaml
```

### Train srresnet_x4

First, the dataset image is split into several small images to reduce IO and keep the batch image size uniform.

```shell
$ python3 ./scripts/split_images.py
```

Then, run the following commands to train the model

```shell
$ python3 train_net.py --config_path ./configs/train/SRResNet_x4-SRGAN_ImageNet.yaml
```

### Resume train srresnet_x4

Modify the `./configs/train/SRResNet_x4-SRGAN_ImageNet.yaml` file.

- line 33: `RESUMED_G_MODEL` change to `./samples/SRResNet_x4-SRGAN_ImageNet/g_epoch_xxx.pth.tar`.

```shell
$ python3 train_net.py --config_path ./configs/train/SRResNet_x4-SRGAN_ImageNet.yaml
```

### Train srgan_x4

```shell
$ python3 train_gan.py --config_path ./configs/train/SRGAN_x4-SRGAN_ImageNet.yaml
```

### Resume train srgan_x4

Modify the `./configs/train/SRGAN_x4-SRGAN_ImageNet.yaml` file.

- line 38: `PRETRAINED_G_MODEL` change to `./results/SRResNet_x4-SRGAN_ImageNet/g_last.pth.tar`.
- line 40: `RESUMED_G_MODEL` change to `./samples/SRGAN_x4-SRGAN_ImageNet/g_epoch_xxx.pth.tar`.
- line 41: `RESUMED_D_MODEL` change to `./samples/SRGAN_x4-SRGAN_ImageNet/d_epoch_xxx.pth.tar`.

```shell
$ python3 train_gan.py --config_path ./configs/train/SRGAN_x4-SRGAN_ImageNet.yaml
```

## Result

Source of original paper results: [https://arxiv.org/pdf/1609.04802v5.pdf](https://arxiv.org/pdf/1609.04802v5.pdf)

In the following table, the psnr value in `()` indicates the result of the project, and `-` indicates no test.

| Set5  | Scale |      SRResNet      |       SRGAN        |
| :---: | :---: | :----------------: | :----------------: |
| PSNR  |   4   |  32.05(**32.16**)  |  29.40(**30.67**)  |
| SSIM  |   4   | 0.9019(**0.8938**) | 0.8472(**0.8627**) |

| Set14 | Scale |      SRResNet      |       SRGAN        |
| :---: | :---: | :----------------: | :----------------: |
| PSNR  |   4   |  28.49(**28.57**)  |  26.02(**27.12**)  |
| SSIM  |   4   | 0.8184(**0.7815**) | 0.7397(**0.7321**) |

| BSD100 | Scale |      SRResNet      |       SRGAN        |
| :----: | :---: | :----------------: | :----------------: |
|  PSNR  |   4   |  27.58(**27.56**)  |  25.16(**26.22**)  |
|  SSIM  |   4   | 0.7620(**0.7367**) | 0.6688(**0.6867**) |

```bash
# If you do not train the model yourself, you can download the model weights and test them.
$ bash ./scripts/download_weights.sh SRGAN_x4-SRGAN_ImageNet
$ python3 ./inference.py
```

Input:

<span align="center"><img width="240" height="360" src="figure/comic.png"/></span>

Output:

<span align="center"><img width="240" height="360" src="figure/sr_comic.png"/></span>

```text
Build `srresnet_x4` model successfully.
Load `srresnet_x4` model weights `SRGAN-PyTorch/results/pretrained_models/SRGAN_x4-SRGAN_ImageNet.pth.tar` successfully.
SR image save to `./figure/sr_comic.png`
```