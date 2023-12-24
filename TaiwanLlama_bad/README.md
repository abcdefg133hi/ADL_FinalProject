# Taiwanese Judge Bad

## Setting
- QLoRA with alpha=16, r=64.
- Prompt: 你是法官，USER會描述案例，請給出公正、有用、安全、詳細和禮貌的判決，USER: {instruction} ASSISTANT:

## Data
- 1905 training data from the lawplus. (train.json)
- 10 testing data from the Internet. (test.json)

## Extract the main texts from the samples.json 
```
python3 extract_mainText.py \
    --input_file <input_file_name> \
    --output_file <output_file_name>
```

## Train
```
bash ./train.sh
```

## Inference
```
bash ./run.sh  \
    --model_path ${1} \
    --adapter_path ${2} \
    --input_file ${3} \
    --output_file ${4}
```

## Demo
```
python3 demo.py \
    --model_path <model_path> \
    --adapter_path <adapter_path>
```
