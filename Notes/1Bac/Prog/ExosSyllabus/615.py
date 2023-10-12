lst = []
total = 0

while(True):
    note = int(input("Note : "))
    
    if note < 0:
        break
    
    total += note
    lst.append(note)
    lst.sort()
    print("nombre de notes entrées :", len(lst))
    print("note la plus élevée", lst[len(lst)- 1])
    print("note la plus basse : ", lst[0])
    print("moyenne de toutes les notes", total/len(lst))