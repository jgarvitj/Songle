import pickle

file1 = open("songsdata.csv", 'r')
id_songName = {}
id_composer = {}
composer_id = {}
songName_id = {}

doc = file1.readline()
class Id_Channel:
    strline = []
    i = 0
    for line in file1:
        strline = line.split(',')
        id_songName[strline[0]] = strline[5]
        id_composer[strline[0]] = strline[4]
        #composer_id[strline[4]] = strline[0]
        #songName_id[strline[5]] = strline[0]

    #print(songName_id)    
    file1.close()
    output = open("id_songName.pkl", 'wb')
    pickle.dump(id_songName, output)
    output.close()


    #output = open("composer_id.pkl", 'wb')
    #pickle.dump(composer_id, output)
    #output.close()


    #output = open("songName_id.pkl", 'wb')
    #pickle.dump(songName_id, output)
    #output.close()


    output = open("id_composer.pkl", 'wb')
    pickle.dump(id_composer, output)
    #print(id_composer['TRVZVIU128F934434F'])
    output.close()
    
    print(id_composer)
