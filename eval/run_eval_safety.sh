# To set up the yaml file, please visit https://github.com/mosaicml/llm-foundry.
export CUDA_VISIBLE_DEVICES=2

MODEL_NAME=scale_open_lm_80m_v1
CHECKPOINT_PATH=/home/song/open-lm-shape/logs/open_lm_ex_80m_v1/checkpoints/epoch_8.pt
CATEGORY=safety

python eval_openlm_ckpt.py \
--eval-yaml local_yaml/bbq.yaml \
--model $MODEL_NAME \
--checkpoint $CHECKPOINT_PATH \
--category $CATEGORY

python eval_openlm_ckpt.py \
--eval-yaml local_yaml/enterprise_pii_classification.yaml \
--model $MODEL_NAME \
--checkpoint $CHECKPOINT_PATH \
--category $CATEGORY

python eval_openlm_ckpt.py \
--eval-yaml local_yaml/winogender_mc_female.yaml \
--model $MODEL_NAME \
--checkpoint $CHECKPOINT_PATH \
--category $CATEGORY

python eval_openlm_ckpt.py \
--eval-yaml local_yaml/winogender_mc_male.yaml \
--model $MODEL_NAME \
--checkpoint $CHECKPOINT_PATH \
--category $CATEGORY

