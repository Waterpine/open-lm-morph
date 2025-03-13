# To set up the yaml file, please visit https://github.com/mosaicml/llm-foundry.
export CUDA_VISIBLE_DEVICES=0

MODEL_NAME=scale_open_lm_313m_v4
CHECKPOINT_PATH=/home/song/open-lm-shape/logs/open_lm_ex_313m_v4_40N/checkpoints/epoch_2.pt
CATEGORY=reading_comprehension

python eval_openlm_ckpt.py \
--eval-yaml local_yaml/agi_eval_lsat_lr.yaml \
--model $MODEL_NAME \
--checkpoint $CHECKPOINT_PATH \
--category $CATEGORY

python eval_openlm_ckpt.py \
--eval-yaml local_yaml/agi_eval_lsat_rc.yaml \
--model $MODEL_NAME \
--checkpoint $CHECKPOINT_PATH \
--category $CATEGORY

python eval_openlm_ckpt.py \
--eval-yaml local_yaml/agi_eval_sat_en.yaml \
--model $MODEL_NAME \
--checkpoint $CHECKPOINT_PATH \
--category $CATEGORY

python eval_openlm_ckpt.py \
--eval-yaml local_yaml/bigbench_understanding_fables.yaml \
--model $MODEL_NAME \
--checkpoint $CHECKPOINT_PATH \
--category $CATEGORY

python eval_openlm_ckpt.py \
--eval-yaml local_yaml/boolq.yaml \
--model $MODEL_NAME \
--checkpoint $CHECKPOINT_PATH \
--category $CATEGORY

python eval_openlm_ckpt.py \
--eval-yaml local_yaml/coqa.yaml \
--model $MODEL_NAME \
--checkpoint $CHECKPOINT_PATH \
--category $CATEGORY

python eval_openlm_ckpt.py \
--eval-yaml local_yaml/pubmed_qa_labeled.yaml \
--model $MODEL_NAME \
--checkpoint $CHECKPOINT_PATH \
--category $CATEGORY

python eval_openlm_ckpt.py \
--eval-yaml local_yaml/squad.yaml \
--model $MODEL_NAME \
--checkpoint $CHECKPOINT_PATH \
--category $CATEGORY

