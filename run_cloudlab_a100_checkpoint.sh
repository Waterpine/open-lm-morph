export CUDA_VISIBLE_DEVICES=0,1
torchrun --nproc-per-node=2 --master_port=8000 -m open_lm.main \
  --model scale_open_lm_80m_v1 \
  --dataset-manifest /mnt/data/dclm_output_192B/manifest.jsonl \
  --train-num-samples 1610612736 \
  --workers 1 \
  --precision amp_bfloat16 \
  --global-batch-size 512 \
  --accum-freq 32 \
  --fsdp --fsdp-amp \
  --grad-checkpointing \
  --log-every-n-steps 100 \
  --grad-clip-norm 1 \
  --data-key json.gz \
  --lr 3e-3 \
  --warmup 2000 \
  --wd 0.033 \
  --beta2 0.95 \
  --epochs 8 \
  --z-loss-coefficient 1e-4 \
  --name open_lm_ex_80m_v1 \
  --resume latest \
  --lr-cooldown-end 3e-5 \

#  --dataset-resampled \
#  --delete-previous-checkpoint \
#  --report-to wandb \
#  --wandb-project-name open_lm_example \
#  --logs /users/Master/logs/