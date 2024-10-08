#!/bin/bash
#SBATCH -J openlm                   # Job name
#SBATCH -o openlm.out               # Name of stdout output file
#SBATCH -e openlm.err               # Name of stderr error file
#SBATCH -p gpu-a100                 # Queue (partition) name
#SBATCH -N 1                        # Total # of nodes (must be 1 for serial)
#SBATCH -t 02:30:00                 # Run time (hh:mm:ss)
#SBATCH --mail-type=all             # Send email at begin and end of job
#SBATCH -A Deep-Learning-at-Sca     # Project/Allocation name (req'd if you have more than 1)
#SBATCH --mail-user=email_address

module load cuda/11.4
conda activate lm

export CUDA_VISIBLE_DEVICES=0,1
torchrun --nproc-per-node=2 -m open_lm.main \
  --model scale_open_lm_14m_v1 \
  --train-data /work/09681/songbian60/ls6/dclm_output_192B/{00000001..0000016}.tar \
  --train-num-samples 268435456 \
  --workers 1 \
  --dataset-resampled \
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
  --epochs 1 \
  --z-loss-coefficient 1e-4 \
  --name open_lm_ex_$RANDOM \
  --resume latest \
  --delete-previous-checkpoint \
#  --report-to wandb \
#  --wandb-project-name open_lm_example \
#  --logs /users/Master/logs/