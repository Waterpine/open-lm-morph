export CUDA_VISIBLE_DEVICES=0,1,2,3
torchrun --nproc-per-node=4 --master_port=8100 -m open_lm.main \
  --model m1b_neox \
  --dataset-manifest /mnt/data/dclm_output_192B/manifest.jsonl \
  --train-num-samples 100000 \
  --workers 1 \
  --precision amp_bfloat16 \
  --global-batch-size 256 \
  --accum-freq 16 \
  --fsdp --fsdp-amp \
  --grad-checkpointing \
  --log-every-n-steps 100 \
  --grad-clip-norm 1 \
  --data-key json.gz \
  --lr 3e-3 \
  --warmup 5000 \
  --wd 0.033 \
  --beta2 0.95 \
  --epochs 16 \
  --z-loss-coefficient 1e-4 \
  --name open_lm_ex_$RANDOM \
  --resume latest \
  --lr-cooldown-end 3e-5 \

#  --dataset-resampled \
#  --delete-previous-checkpoint \
#  --report-to wandb \
#  --wandb-project-name open_lm_example \
#  --logs /users/Master/logs/