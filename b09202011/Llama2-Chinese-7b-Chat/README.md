# Taiwan Llama 法官

## Setting
- QLoRA with alpha=8, r=4.
- Prompt: 你現在是法官，我會給你一個事件，你必須要給出判決。USER: {instruction} ASSISTANT:
- Traning time: V100, About 2 min/ 1 epoch.

## Training and Prediction
```
python3 train_and_predict.py --train_file "train.json" --epochs 1 --output_file "output.json" --valid_file "valid.json"
```
- Recommend training epochs: 3.

## Data
- About 370 training data from the Internet. (train.json)
- About 20 validation data from the Internet. (valid.json)

## Performance
- Not bad, but I think more data are needed.
- "output.json" is the prediction for valid.json.
- It is better than Llama2-Chinese-7b-Chat.

## Change to readble JSON file
```
python3 transform_to_proper_json.py --input [INPUT] -- output [OUPUT]
```

## Train
```
python3 train.py --peft_path [Your Adapter Path] --train_file "train.json" --epochs 1 --save_path [Your Adapter Path]
```

## Predict
```
python3 predict.py --peft_path [Your Adapter Path] --valid_file "valid.json" --output_file "output.json"
```


## Demo
```
python3 demo.py --peft_path [Your Adapter Path]
```

# Model Version
- ChineseLlama\_370\_not\_revise: Training with 370 training data without unified output format.
- ChineseLlama\_370\_revise: Training with 370 training data without unified output format.

