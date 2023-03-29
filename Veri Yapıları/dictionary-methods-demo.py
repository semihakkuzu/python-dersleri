'''
player 1:
    id          : 1
    name        : Cristiano Ronaldo
    yearOfBirth : 1985
    nationality : Portugal
    current_team: Portugal
    history     : Juventus, Real Madrid, Portugal

Player 2:
    id          :2
    name        : Lionel Messi
    yearOfBirth : 1987
    nationality : Argentina
    current_team: Barcelona
    history     : Barcelona, Argentina, Portugal
'''
players = {
    
    '1': 
        {'name': 'Cristiano Ronaldo', 
        'yearOfBirth': '1985', 
        'nationality': 'Portugal', 
        'current_team': 'Portugal', 
        'history': ['Juventus', ' Real Madrid', ' Portugal']},

    '2': 
        {'name': 'Lionel Messi', 
        'yearOfBirth': '1987', 
        'nationality': 'Argentina', 
        'current_team': 'Barcelona', 
        'history': ['Barcelona', ' Argentina', ' Portugal']}
}
#id = input('oyuncu id: ')
#name = input('oyuncu ad: ')
#yearOfBirth = input('doğum yılı:')
#nationality = input('memleket: ')
#current_team = input('mevcut takım: ')
#history = input('geçmiş: ')

#players = {
#    id : {
#        "name": name,
#        "yearOfBirth" : yearOfBirth,
#        "nationality" : nationality,
#        "current_team" : current_team,
#        "history" : history.split(',')
#    
#    }
#}
# id = input('Player Id: ')
# player = playerObj[id]
# print(f'id:{id} adı: {player["name"]} doğum yılı: {player["yearOfBirth"]} ülke: {player["nationality"]} mevcut_takım:{player["current_team"]} geçmiş takımlar:{player["history"]}')

id = input('oyuncu id:')
player = players.get(id)
print(player)