# To set up the yaml file, please visit https://github.com/mosaicml/llm-foundry.
export CUDA_VISIBLE_DEVICES=2
python eval_openlm_ckpt.py \
--eval-yaml in_memory_eval.yaml \
--model scale_open_lm_80m_v1 \
--checkpoint /home/song/open-lm-shape/logs/open_lm_ex_80m_v1/checkpoints/epoch_8.pt \
# --positional_embedding_type head_rotary \
