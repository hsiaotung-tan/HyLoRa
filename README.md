# HyLoRa
Low-Rank Prompt-Guided Transformer for Hyperspectral Image Denoising

## Guide
Git clone the [HSIR](https://github.com/bit-isp/HSIR) repository, and copy files in model into corresponding position HSIR. 

Then 
```
python -m hsirun.train -a hylora.hylora -s schedule.denoise_default
```

```bibtex
@article{tanxiaodong2024lowrankprompt,
  author={Tan, Xiaodong and Shao, Mingwen and Qiao, Yuanjian and Liu, Tiyao and Cao, Xiangyong},
  journal={IEEE Transactions on Geoscience and Remote Sensing}, 
  title={Low-Rank Prompt-Guided Transformer for Hyperspectral Image Denoising}, 
  year={2024},
  doi={10.1109/TGRS.2024.3414956}}
```
## Acknowledgements
This repository is based on [HSIR](https://github.com/bit-isp/HSIR).
