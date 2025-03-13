# To set up the yaml file, please visit https://github.com/mosaicml/llm-foundry.
export CUDA_VISIBLE_DEVICES=0

MODEL_NAME=scale_open_lm_1b_v6
CHECKPOINT_PATH=/users/Master/open-lm-shape/logs/open_lm_ex_1.5b_v6/checkpoints/epoch_16.pt
CATEGORY=safety

python eval_openlm_ckpt.py \
--eval-yaml local_yaml_1b_bf16/bbq.yaml \
--model $MODEL_NAME \
--checkpoint $CHECKPOINT_PATH \
--category $CATEGORY

python eval_openlm_ckpt.py \
--eval-yaml local_yaml_1b_bf16/enterprise_pii_classification.yaml \
--model $MODEL_NAME \
--checkpoint $CHECKPOINT_PATH \
--category $CATEGORY

python eval_openlm_ckpt.py \
--eval-yaml local_yaml_1b_bf16/winogender_mc_female.yaml \
--model $MODEL_NAME \
--checkpoint $CHECKPOINT_PATH \
--category $CATEGORY

python eval_openlm_ckpt.py \
--eval-yaml local_yaml_1b_bf16/winogender_mc_male.yaml \
--model $MODEL_NAME \
--checkpoint $CHECKPOINT_PATH \
--category $CATEGORY

