# To set up the yaml file, please visit https://github.com/mosaicml/llm-foundry.
python eval_openlm_ckpt.py \
--eval-yaml in_memory_eval.yaml \
--model open_lm_411m_v2  \
--checkpoint /home/madracks-users/song/open-lm-shape/logs/open_lm_ex_21904/checkpoints/epoch_2.pt
# --positional_embedding_type head_rotary