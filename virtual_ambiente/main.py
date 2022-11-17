from events.birthdate import events_birthdate
from time import sleep


while True:
    events_birthdate()
    sleep(86400) # Vai contar 24h a partir do momento em que for iniciado.