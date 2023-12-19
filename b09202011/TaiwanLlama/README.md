# Taiwan Llama 法官

## Setting
- QLoRA with alpha=8, r=4.
- Prompt: 你現在是法官，我會給你一個事件，你必須要給出判決。USER: {instruction} ASSISTANT:
- Traning time: V100, About 2 min/ 1 epoch.

## Training and Prediction
```
python3 train_and_predict.py --train_file "train.json" --epochs 1 --output_file "output.json" --valid_file "valid.json"
```
- Recommend training epochs: 1. (2,3 are both okay but a little overfitting.)

## Data
- About 200 training data from the Internet. (train.json)
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

## Download Adapter (Under Test)
```
chmod 744 download.sh
./download.sh
```

## Demo
```
python3 demo.py --peft_path [Your Adapter Path]
```
It seems that the model will have a more stable prediction when the input provides enough information. For example:
- 小天毆打小霸王，使得小霸王重傷 -> 判處小天違反刑法第276條～殺人罪，並科以刑期貳年。
- 立法委員因海鮮店佔用騎樓擺設桌椅營業，警員取締佔用騎樓之職務時，在於公務員依法執行職務時當場侮辱 -> 刑法第135條～公務員侮辱罪；處拘役 拘役處伍日，如易科罰金，以參以低估。緩刑貳年，如付保護費。如易服勞役，以參易科役。但如附帶條件，禁止再犯罰則。緩刑伍年；如付保護費。如易服勞役，以參易科役。如仍有爭執，應為偵查。
- 柯南今天搶奪小蘭的錢包 -> 判處柯南猶如隱形搶匪，依刑法搶奪罪嫌，判處有期徒刑。依刑法第320條，判處柯南有期徒刑處徒刑。

