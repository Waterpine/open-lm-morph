# To set up the yaml file, please visit https://github.com/mosaicml/llm-foundry.
export CUDA_VISIBLE_DEVICES=3

MODEL_NAME=scale_open_lm_164m_v7
CHECKPOINT_PATH=/home/song/open-lm-shape/logs/open_lm_ex_164m_v7_40N/checkpoints/epoch_2.pt
CATEGORY=world_knowledge

python eval_openlm_ckpt.py \
--eval-yaml local_yaml/arc_challenge.yaml \
--model $MODEL_NAME \
--checkpoint $CHECKPOINT_PATH \
--category $CATEGORY

python eval_openlm_ckpt.py \
--eval-yaml local_yaml/arc_easy.yaml \
--model $MODEL_NAME \
--checkpoint $CHECKPOINT_PATH \
--category $CATEGORY

python eval_openlm_ckpt.py \
--eval-yaml local_yaml/bigbench_misconceptions.yaml \
--model $MODEL_NAME \
--checkpoint $CHECKPOINT_PATH \
--category $CATEGORY

python eval_openlm_ckpt.py \
--eval-yaml local_yaml/bigbench_movie_recommendation.yaml \
--model $MODEL_NAME \
--checkpoint $CHECKPOINT_PATH \
--category $CATEGORY

python eval_openlm_ckpt.py \
--eval-yaml local_yaml/bigbench_qa_wikidata.yaml \
--model $MODEL_NAME \
--checkpoint $CHECKPOINT_PATH \
--category $CATEGORY

python eval_openlm_ckpt.py \
--eval-yaml local_yaml/jeopardy_all.yaml \
--model $MODEL_NAME \
--checkpoint $CHECKPOINT_PATH \
--category $CATEGORY

python eval_openlm_ckpt.py \
--eval-yaml local_yaml/jeopardy_small.yaml \
--model $MODEL_NAME \
--checkpoint $CHECKPOINT_PATH \
--category $CATEGORY

python eval_openlm_ckpt.py \
--eval-yaml local_yaml/mmlu.yaml \
--model $MODEL_NAME \
--checkpoint $CHECKPOINT_PATH \
--category $CATEGORY

python eval_openlm_ckpt.py \
--eval-yaml local_yaml/mmlu_expand.yaml \
--model $MODEL_NAME \
--checkpoint $CHECKPOINT_PATH \
--category $CATEGORY

python eval_openlm_ckpt.py \
--eval-yaml local_yaml/triviaqa.yaml \
--model $MODEL_NAME \
--checkpoint $CHECKPOINT_PATH \
--category $CATEGORY \
