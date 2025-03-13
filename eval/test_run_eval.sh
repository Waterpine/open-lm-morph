# To set up the yaml file, please visit https://github.com/mosaicml/llm-foundry.
export CUDA_VISIBLE_DEVICES=0

MODEL_NAME=scale_open_lm_164m_v1
CHECKPOINT_PATH=/home/song/open-lm-shape/logs/open_lm_ex_164m_v1/checkpoints/epoch_8.pt
CATEGORY=world_knowledge

python eval_openlm_ckpt.py \
--eval-yaml local_yaml/bigbench_movie_recommendation.yaml \
--model $MODEL_NAME \
--checkpoint $CHECKPOINT_PATH \
--category $CATEGORY


