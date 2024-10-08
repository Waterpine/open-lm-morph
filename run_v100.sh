export CUDA_VISIBLE_DEVICES=0,1,2,3
torchrun --nproc-per-node=4 -m open_lm.main \
  --model scale_open_lm_25m_v1 \
  --train-data /home/madracks-users/song/dclm_output_debug_2B/{00000001..00000100}.tar \
  --workers 1 \
  --dataset-resampled \
  --train-num-samples 1677721600 \
  --precision fp16 \
  --global-batch-size 512 \
  --accum-freq 32 \
  --fsdp \
  --grad-checkpointing \
  --log-every-n-steps 100 \
  --grad-clip-norm 1 \
  --data-key json.gz \
  --lr 3e-3 \
  --warmup 2000 \
  --wd 0.033 \
  --beta2 0.95 \
  --epochs 1 \
  --z-loss-coefficient 1e-4 \
  --name open_lm_ex_$RANDOM \
  --resume latest \
  --delete-previous-checkpoint \
#  --fsdp --fsdp-amp \
#  --precision amp_bfloat16 \
#  --report-to wandb \
#  --wandb-project-name open_lm_example \
#  --logs /users/Master/logs/