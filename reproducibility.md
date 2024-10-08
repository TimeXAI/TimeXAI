
# Reproducing Experiments
This file gives instructions on how to reproduce the findings in the TimeXAI paper. These experiments will be organized by structure of the paper, so please reference those sections.

## Training TimeXAI
Scripts used to train TimeXAI models are included in `experiments/<dataset>/bc_model_ptype.py`. Within these scripts, you can change hyperparameter choices and see usage for setting up the model, training function, loss functions, and more. Before training, please replace the path to the trained time series predictor that you wish to explain. Then, run:
```
python bc_model_ptype.py
```
Additional arguments can be included to train ablation models (please see scripts for more details).

## R1: Attribution experiments
All attribution ground-truth evaluations are performed in `experiments/evaluation/saliency_exp_synth.py`. The usage for this script is as follows:
```
python3 saliency_exp_synth.py \
    --exp_method <EXP_METHOD> \ 
    --dataset <DATASET> \
    --split_no -1 \
    --model_path <MODEL_PATH>
```
`EXP_METHOD` is replaced with the explainability method you wish to evaluate (see the script for options). Use `ours` for TimeXAI.
`DATASET` is replaced with the name of the dataset on which you wish to evaluate the method (see the script for options). `MODEL_PATH` is the path to the model to explain. Use the path to a time series explainer for all other explainers, but if evaluating TimeXAI, use the path to the TimeXAI trained model.


## R2: Occlusion experiments
All occlusion experiments are facilitated through `experiments/evaluation/occlusion_exp.py`. The usage for this script is as follows:
```
python3 occlusion_exp.py \
    --exp_method <EXP_METHOD> \
    --dataset <DATASET> \
    --split_no -1 \
    --model_path <MODEL_PATH> \
```
Usage is the same as for `saliency_exp_synth.py`, but this script performs the occlusion experiment as explained in the paper.

### Baseline notes: WinIT

Train generator models with:

```bash
python experiments/evaluation/winit_wrapper.py \
    --dataset scs_better \
    --data_path <path to dataset directory> \
    --models_path <path to models directory>
```

Evaluate:

```bash
python experiments/evaluation/saliency_exp_synth.py \
    --dataset scs_better \
    --data_path <path to to dataset directory>  \
    --model_path <path to models>/Scomb_transformer_split\=1_cpu.pt \
    --exp_method winit
```
