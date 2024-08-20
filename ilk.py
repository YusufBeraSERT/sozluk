meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "HELLO": "Selam verme eylemine denir",
            "TETRIS": "bazı şekilli parçaların birbirleri ile doğru birleşmesi ile kazanılan birer oyun",
            }
            
word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    while True:
        word = input("Lütfen tekrardan deneyin: ")
        if word in meme_dict.keys():
            print(meme_dict[word])
            break
