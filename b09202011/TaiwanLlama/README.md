# Taiwan Llama 法官

## Setting
- QLoRA with alpha=16, r=64.
- Prompt: 你現在是法官，我會給你一個事件，你必須要給出判決。USER: {instruction} ASSISTANT:
- Traning time: About 1 min/ 1 epoch.

## Training and Prediction
```
python3 train_and_predict.py --train_file "train.json" --epochs 1 --output_file "output.json" --valid_file "valid.json"
```
- Recommend training epochs: 1. (2,3 are both okay but a little overfitting.)

## Data
- About 100 training data from the Internet. (train.json)
- About 20 validation data from the Internet. (valid.json)

## Performance
- Not bad, but I think more data are needed.
- "output.json" is the prediction for valid.json.
- It is better than Llama2-Chinese-7b-Chat.

## Change to readble JSON file
```
python3 transform_to_proper_json.py --input [INPUT] -- output [OUPUT]
```

## Train / Predict
- To do.

