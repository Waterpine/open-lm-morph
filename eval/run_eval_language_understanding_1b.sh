# To set up the yaml file, please visit https://github.com/mosaicml/llm-foundry.
export CUDA_VISIBLE_DEVICES=1

MODEL_NAME=scale_open_lm_1b_v8
CHECKPOINT_PATH=/home/song/open-lm-shape/logs/open_lm_ex_1.5b_v8/checkpoints/epoch_16.pt
CATEGORY=language_understanding

python eval_openlm_ckpt.py \
--eval-yaml local_yaml_1b/bigbench_conceptual_combinations.yaml \
--model $MODEL_NAME \
--checkpoint $CHECKPOINT_PATH \
--category $CATEGORY

python eval_openlm_ckpt.py \
--eval-yaml local_yaml_1b/bigbench_conlang_translation.yaml \
--model $MODEL_NAME \
--checkpoint $CHECKPOINT_PATH \
--category $CATEGORY

python eval_openlm_ckpt.py \
--eval-yaml local_yaml_1b/bigbench_language_identification.yaml \
--model $MODEL_NAME \
--checkpoint $CHECKPOINT_PATH \
--category $CATEGORY

python eval_openlm_ckpt.py \
--eval-yaml local_yaml_1b/hellaswag.yaml \
--model $MODEL_NAME \
--checkpoint $CHECKPOINT_PATH \
--category $CATEGORY

python eval_openlm_ckpt.py \
--eval-yaml local_yaml_1b/lambada_openai.yaml \
--model $MODEL_NAME \
--checkpoint $CHECKPOINT_PATH \
--category $CATEGORY

python eval_openlm_ckpt.py \
--eval-yaml local_yaml_1b/lambada_openai_small.yaml \
--model $MODEL_NAME \
--checkpoint $CHECKPOINT_PATH \
--category $CATEGORY

python eval_openlm_ckpt.py \
--eval-yaml local_yaml_1b/winograd_wsc.yaml \
--model $MODEL_NAME \
--checkpoint $CHECKPOINT_PATH \
--category $CATEGORY

python eval_openlm_ckpt.py \
--eval-yaml local_yaml_1b/winogrande.yaml \
--model $MODEL_NAME \
--checkpoint $CHECKPOINT_PATH \
--category $CATEGORY

