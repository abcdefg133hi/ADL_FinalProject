# Chinese Llama 法官

## Setting
- QLoRA with alpha=16, r=64.
- All the words here are in 簡體字. The same validation file as the one in TaiwanLlama.
- Traning time: About 2 min/ 1 epoch.
- Prompt: 你现在是法官，我会给你一个事件，你必须要给出判决。USER: {instruction} ASSISTANT::

## Training and Prediction
```
python3 train_and_predict.py --train_file "train.json" --epochs 3 --output_file "output.json" --valid_file "valid.json" --model_name_or_path "FlagAlpha/Llama2-Chinese-7b-Chat"
```
- Training Epochs: 3 is recommended. (1,2 would be bad.)

## Data
- About 80 training data from the Internet. (train.json)
- About 20 validation data from the Internet. (valid.json)

## Performance
- Not bad, but I think more data are needed.
- "output.json" is the prediction for valid.json.

## Change to readble JSON file
```
python3 transform_to_proper_json.py --input [INPUT] -- output [OUPUT]
```

## Train / Predict
- To do.


