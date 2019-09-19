# RAWR Skill in ASK Python SDK (using Classes)


## Audio for Alexa

https://developer.amazon.com/docs/quick-reference/play-audio-quick-reference.htmlk


## Best quality audio conversion : 
ffmpeg install : https://www.binarycomputer.solutions/install-ffmpeg-centos/#centos-7-quick
Reference : https://developer.amazon.com/docs/custom-skills/speech-synthesis-markup-language-ssml-reference.html#audio

```bash
ffmpeg -i <input-file> -ac 2 -codec:a libmp3lame -b:a 48k -ar 24000 -write_xing 0 <output-file>
```

example : 
`ffmpeg -i lion.mp3 -ac 2 -codec:a libmp3lame -b:a 48k -ar 24000 -write_xing 0 lion_01.mp3`


## AWS Work

```bash
aws s3 ls s3://animal-sound-clips
aws s3 cp lion_01.mp3 s3://animal-sound-clips

curl -O https://www.google.com/logos/fnbx/animal_sounds/panda.mp3
curl -O https://www.google.com/logos/fnbx/animal_sounds/bat.mp3
curl -O https://www.google.com/logos/fnbx/animal_sounds/dog.mp3
curl -O https://www.google.com/logos/fnbx/animal_sounds/humpback-whale.mp3
curl -O https://www.google.com/logos/fnbx/animal_sounds/leopard.mp3
curl -O https://www.google.com/logos/fnbx/animal_sounds/pig.mp3
curl -O https://www.google.com/logos/fnbx/animal_sounds/robin.mp3
curl -O https://www.google.com/logos/fnbx/animal_sounds/raccoon.mp3
curl -O https://www.google.com/logos/fnbx/animal_sounds/owl.mp3
curl -O https://www.google.com/logos/fnbx/animal_sounds/hedgehog.mp3
curl -O https://www.google.com/logos/fnbx/animal_sounds/turkey.mp3

ffmpeg -i lion.mp3 -ac 2 -codec:a libmp3lame -b:a 48k -ar 24000 -write_xing 0 lion_01.mp3
ffmpeg -i panda.mp3 -ac 2 -codec:a libmp3lame -b:a 48k -ar 24000 -write_xing 0 panda_01.mp3
ffmpeg -i bat.mp3 -ac 2 -codec:a libmp3lame -b:a 48k -ar 24000 -write_xing 0  bat_01.mp3
ffmpeg -i dog.mp3 -ac 2 -codec:a libmp3lame -b:a 48k -ar 24000 -write_xing 0  dog_01.mp3
ffmpeg -i humpback-whale.mp3 -ac 2 -codec:a libmp3lame -b:a 48k -ar 24000 -write_xing 0  humpback-whale_01.mp3
ffmpeg -i leopard.mp3 -ac 2 -codec:a libmp3lame -b:a 48k -ar 24000 -write_xing 0  leopard_01.mp3
ffmpeg -i pig.mp3 -ac 2 -codec:a libmp3lame -b:a 48k -ar 24000 -write_xing 0  pig_01.mp3
ffmpeg -i robin.mp3 -ac 2 -codec:a libmp3lame -b:a 48k -ar 24000 -write_xing 0  robin_01.mp3
ffmpeg -i raccoon.mp3 -ac 2 -codec:a libmp3lame -b:a 48k -ar 24000 -write_xing 0  raccoon_01.mp3
ffmpeg -i owl.mp3 -ac 2 -codec:a libmp3lame -b:a 48k -ar 24000 -write_xing 0  owl_01.mp3
ffmpeg -i hedgehog.mp3 -ac 2 -codec:a libmp3lame -b:a 48k -ar 24000 -write_xing 0  hedgehog_01.mp3
ffmpeg -i turkey.mp3 -ac 2 -codec:a libmp3lame -b:a 48k -ar 24000 -write_xing 0  turkey_01.mp3

aws s3 cp bat_01.mp3 s3://animal-sound-clips
aws s3 cp panda_01.mp3 s3://animal-sound-clips
aws s3 cp bat_01.mp3 s3://animal-sound-clips
aws s3 cp dog_01.mp3 s3://animal-sound-clips
aws s3 cp humpback-whale_01.mp3 s3://animal-sound-clips
aws s3 cp leopard_01.mp3 s3://animal-sound-clips
aws s3 cp pig_01.mp3 s3://animal-sound-clips
aws s3 cp robin_01.mp3 s3://animal-sound-clips
aws s3 cp raccoon_01.mp3 s3://animal-sound-clips
aws s3 cp owl_01.mp3 s3://animal-sound-clips
aws s3 cp hedgehog_01.mp3 s3://animal-sound-clips
aws s3 cp turkey_01.mp3 s3://animal-sound-clips
```