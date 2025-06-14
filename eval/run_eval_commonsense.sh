# To set up the yaml file, please visit https://github.com/mosaicml/llm-foundry.
export CUDA_VISIBLE_DEVICES=3

MODEL_NAME=scale_open_lm_313m_v4
CHECKPOINT_PATH=/home/song/open-lm-shape/logs/open_lm_ex_313m_v4_40N/checkpoints/epoch_2.pt
CATEGORY=commonsense_reasoning

python eval_openlm_ckpt.py \
--eval-yaml local_yaml/bigbench_novel_concepts.yaml \
--model $MODEL_NAME \
--checkpoint $CHECKPOINT_PATH \
--category $CATEGORY

python eval_openlm_ckpt.py \
--eval-yaml local_yaml/bigbench_strange_stories.yaml \
--model $MODEL_NAME \
--checkpoint $CHECKPOINT_PATH \
--category $CATEGORY

python eval_openlm_ckpt.py \
--eval-yaml local_yaml/bigbench_strategy_qa.yaml \
--model $MODEL_NAME \
--checkpoint $CHECKPOINT_PATH \
--category $CATEGORY

python eval_openlm_ckpt.py \
--eval-yaml local_yaml/commonsense_qa.yaml \
--model $MODEL_NAME \
--checkpoint $CHECKPOINT_PATH \
--category $CATEGORY

python eval_openlm_ckpt.py \
--eval-yaml local_yaml/copa.yaml \
--model $MODEL_NAME \
--checkpoint $CHECKPOINT_PATH \
--category $CATEGORY

python eval_openlm_ckpt.py \
--eval-yaml local_yaml/openbook_qa.yaml \
--model $MODEL_NAME \
--checkpoint $CHECKPOINT_PATH \
--category $CATEGORY

python eval_openlm_ckpt.py \
--eval-yaml local_yaml/piqa.yaml \
--model $MODEL_NAME \
--checkpoint $CHECKPOINT_PATH \
--category $CATEGORY

python eval_openlm_ckpt.py \
--eval-yaml local_yaml/siqa.yaml \
--model $MODEL_NAME \
--checkpoint $CHECKPOINT_PATH \
--category $CATEGORY

