# Morph

![](/plots/morph.png)

This repository contains the code for paper [Scaling Inference-Efficient Language Models (ICML'25)](https://arxiv.org/pdf/2501.18107). Our code is based on [OpenLM](https://github.com/mlfoundations/open_lm) and [DCLM-Morph](https://github.com/Waterpine/dclm-morph).

# Contents
- [Quickstart](#quickstart)
  - [Process training data](#process-training-data)
  - [Setup](#setup)
  - [Run training](#run-training)
  - [Evaluate Model](#evaluate-model)
- [Experimental Results](#experimental-results)
- [Team and Acknowledgements](#team-and-acknowledgements)

# Quickstart
Here we'll go over a basic example where we start from a fresh install, download and preprocess some training data, and train a model.

## Process Training Data

We use the DCLM dataset to train the models. The detailed data preprocessing steps are provided in [DCLM-Morph](https://github.com/Waterpine/dclm-morph).

## Setup

```
conda create -n llm python=3.9
cd open-lm-shape
pip install -r requirements.txt
pip install --editable . 
```

## Run Training
Model choices are contained in the following table, where, for instance `80m` indicates an 80 million parameter model and `1b` indicates a 1 billion parameter model. 

Since we study models with different shapes, the same number of parameters can result in different configurations. For example, `scale_open_lm_80m_v1` differs from `scale_open_lm_80m_v2`. The specific configurations are provided in the [paper](https://arxiv.org/pdf/2501.18107).
<center>

| Model Name                       |
|----------------------------------|
| `scale_open_lm_80m_v{1,2,..,7}`  |
| `scale_open_lm_116m_v{1,2,..,6}` |
| `scale_open_lm_164m_v{1,2,..,8}` |
| `scale_open_lm_237m_v{1,2,..,6}` |
| `scale_open_lm_313m_v{1,2,..,6}` |
| `scale_open_lm_1b_v{1,2,..,8}`   |

</center>

An example training run can be called as follows:
```
export CUDA_VISIBLE_DEVICES=0,1
torchrun --nproc-per-node=2 --master_port=8100 -m open_lm.main \
  --model scale_open_lm_116m_v6 \
  --dataset-manifest /mnt/data/dclm_output_192B/manifest.jsonl \
  --train-num-samples 2315255808 \
  --workers 1 \
  --precision amp_bfloat16 \
  --global-batch-size 128 \
  --accum-freq 16 \
  --grad-checkpointing \
  --log-every-n-steps 100 \
  --grad-clip-norm 1 \
  --data-key json.gz \
  --lr 3e-3 \
  --warmup 2000 \
  --wd 0.033 \
  --beta2 0.95 \
  --epochs 2 \
  --z-loss-coefficient 1e-4 \
  --name open_lm_ex_$RANDOM \
  --resume latest \
  --lr-cooldown-end 3e-5 \
```
Checkpoints and final model weights will be saved to the specified logs directory.

## Evaluate Model
To set up the environment, we first follow these steps.
```
git clone https://github.com/Waterpine/dclm-morph.git
cd dclm-morph
apt install cmake build-essential
apt install g++-9
update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-9 90
pip install -r requirements.txt
conda create -n eval python=3.9
cd open-lm-morph
pip install --editable . 
```
We present an example evaluating Morph-1B on the COPA dataset.
```
cd eval
export CUDA_VISIBLE_DEVICES=0

MODEL_NAME=scale_open_lm_1b_v8
CHECKPOINT_PATH=xxx/logs/checkpoints/morph_1b.pt
CATEGORY=commonsense_reasoning

python eval_openlm_ckpt.py \
--eval-yaml local_yaml_1b/copa.yaml \
--model $MODEL_NAME \
--checkpoint $CHECKPOINT_PATH \
--category $CATEGORY
```

# Experimental Results

We evaluate 1B models over the following datasets: arc_challenge, arc_easy, boolq, copa, hellaswag, jeopardy, lambada_openai, MMLU, piqa, winograd, and winogrande.

| **Models**   | **d_model** | **n_layers** | **Average** | **Latency (s)** |
|--------------|-------------|--------------|-------------|-----------------|
|              |             |              |             |                 |
| Open-LM-1B   | 2048        | 24           | 0.49        | 3.61            |
| OPT-1.3B     | 2048        | 24           | 0.50        | 2.55            |
| Pythia-1.3B  | 2048        | 22           | 0.49        | 3.28            |
| Neox-1.3B    | 2048        | 24           | 0.49        | 3.99            |
| OPT-IML-1.3B | 2048        | 24           | 0.54        | 2.54            |
| Morph-1B-v1  | 2048        | 24           | 0.52        | 3.61            |
| Morph-1B-v2  | 2560        | 16           | 0.52        | 2.57            |
| Morph-1B    | 3072        | 12           | 0.52        | 1.96            |

## Contributing

Authors: Song Bian*, Minghao Yan*, Shivaram Venkataraman

Affiliated: University of Wisconsin-Madison

Citation
--------

If you use this model in your work, please use the following BibTeX citation:
```bibtex
@article{bian2025scaling,
  title={Scaling Inference-Efficient Language Models},
  author={Bian, Song and Yan, Minghao and Venkataraman, Shivaram},
  journal={arXiv preprint arXiv:2501.18107},
  year={2025}
}
```

